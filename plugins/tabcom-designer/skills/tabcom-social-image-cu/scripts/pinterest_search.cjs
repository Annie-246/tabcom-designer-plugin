// Fallback when the `pinterest` MCP tools are not loaded in the current session:
// talks to the installed pinterest-mcp-server over stdio and downloads results.
// Usage: node pinterest_search.cjs "<keyword>" <limit> <downloadDir>
const { spawn } = require("child_process");
const [keyword, limitArg, dir] = process.argv.slice(2);
if (!keyword || !dir) { console.error('usage: node pinterest_search.cjs "<keyword>" <limit> <downloadDir>'); process.exit(2); }

const p = spawn("pinterest-mcp-server", [], { shell: true, env: { ...process.env, MCP_PINTEREST_DOWNLOAD_DIR: dir } });
let buf = "";
const send = (o) => p.stdin.write(JSON.stringify(o) + "\n");
p.stdout.on("data", (d) => {
  buf += d;
  let i;
  while ((i = buf.indexOf("\n")) >= 0) {
    const line = buf.slice(0, i); buf = buf.slice(i + 1);
    let m; try { m = JSON.parse(line); } catch { continue; }
    if (m.id === 1) {
      send({ jsonrpc: "2.0", method: "notifications/initialized" });
      send({ jsonrpc: "2.0", id: 2, method: "tools/call", params: { name: "pinterest_search_and_download",
        arguments: { keyword, limit: Number(limitArg || 12), headless: true } } });
    } else if (m.id === 2) {
      for (const c of (m.result && m.result.content) || []) if (c.text) console.log(c.text);
      if (m.error) console.error(JSON.stringify(m.error));
      p.kill(); process.exit(m.error ? 1 : 0);
    }
  }
});
send({ jsonrpc: "2.0", id: 1, method: "initialize",
  params: { protocolVersion: "2024-11-05", capabilities: {}, clientInfo: { name: "tabcom-social-image", version: "1" } } });
setTimeout(() => { console.error("TIMEOUT"); p.kill(); process.exit(1); }, 240000);
