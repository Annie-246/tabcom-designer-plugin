#!/usr/bin/env node
// One-command installer: adds the marketplace, installs the plugin, turns on background auto-update.
// marketplace.json cannot enable auto-update for installers, so this sets it in the user's settings.json.
const { execSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const URL_ = "https://github.com/Annie-246/tabcom-designer-plugin.git"; // HTTPS: the owner/repo form clones over SSH and fails without SSH keys
const MARKET = "tabcom-plugins";
const PLUGIN = "tabcom-designer";

const run = (cmd) => execSync(cmd, { stdio: "inherit" });

try {
  execSync("claude --version", { stdio: "ignore" });
} catch {
  console.error("Không tìm thấy lệnh `claude`. Cài Claude Code trước: https://claude.com/claude-code");
  process.exit(1);
}

run(`claude plugin marketplace add ${URL_}`);
run(`claude plugin install ${PLUGIN}@${MARKET}`);

const file = path.join(process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude"), "settings.json");
let settings = {};
if (fs.existsSync(file)) {
  try {
    settings = JSON.parse(fs.readFileSync(file, "utf8"));
  } catch {
    console.error(`Plugin đã cài, nhưng không đọc được ${file} nên chưa bật auto-update.`);
    console.error("Bật tay: trong Claude Code gõ /plugin, vào tab Marketplaces, chọn tabcom-plugins, chọn Enable auto-update.");
    process.exit(1);
  }
}
settings.extraKnownMarketplaces ??= {};
settings.extraKnownMarketplaces[MARKET] = {
  ...settings.extraKnownMarketplaces[MARKET],
  source: { source: "git", url: URL_ },
  autoUpdate: true,
};
fs.mkdirSync(path.dirname(file), { recursive: true });
const tmp = `${file}.tmp`;
fs.writeFileSync(tmp, JSON.stringify(settings, null, 2) + "\n");
fs.renameSync(tmp, file);

console.log(`\nXong. Auto-update đã bật. Khởi động lại Claude Code rồi gọi /${PLUGIN}:${PLUGIN}`);
