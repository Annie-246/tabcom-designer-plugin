"""Generate one image with Codex CLI's image tool from a self-contained prompt, then fit it to the target size.

Usage:
  python -I codex_image.py --prompt prompt.md --out final.png --size 1080x1080 [--image ref1.png --image ref2.png ...]

Codex is told (inside the prompt) to only call image generation. This script:
  1. runs `codex exec -s read-only` with the prompt on stdin and the reference images attached,
  2. finds the image Codex saved under ~/.codex/generated_images/<session-id>/,
  3. scales it to cover the target size and center-crops (no distortion),
  4. prints session id, tokens used, image-generation count, shell-command count and Codex rate-limit usage.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

from PIL import Image

CODEX_HOME = os.path.join(os.path.expanduser("~"), ".codex")


def newest_session_file():
    files = glob.glob(os.path.join(CODEX_HOME, "sessions", "*", "*", "*", "*.jsonl"))
    return max(files, key=os.path.getmtime) if files else None


def fit(src, out, w, h):
    im = Image.open(src).convert("RGB")
    scale = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    left, top = (im.width - w) // 2, (im.height - h) // 2
    im = im.crop((left, top, left + w, top + h))
    try:
        im.save(out)
        return out
    except OSError:  # target open/locked in an image viewer on Windows -> keep the result under a new name
        root, ext = os.path.splitext(out)
        n = 2
        while os.path.exists(f"{root}_v{n}{ext}"):
            n += 1
        alt = f"{root}_v{n}{ext}"
        im.save(alt)
        return alt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="1080x1080")
    ap.add_argument("--image", action="append", default=[])
    a = ap.parse_args()
    w, h = (int(v) for v in a.size.lower().split("x"))

    before = newest_session_file()
    cmd = ["codex", "exec", "--skip-git-repo-check", "-s", "read-only"]
    for img in a.image:
        cmd += ["-i", img]
    cmd += ["-"]
    with open(a.prompt, encoding="utf-8") as f:
        res = subprocess.run(cmd, stdin=f, capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=900, shell=(os.name == "nt"))
    tokens = re.findall(r"tokens used\s*\n?\s*([\d,]+)", res.stdout + res.stderr)

    session = newest_session_file()
    if not session or session == before:
        sys.exit("ERROR: no new Codex session found.\n" + res.stdout[-2000:] + res.stderr[-2000:])
    sid = re.search(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\.jsonl$", session).group(1)
    text = open(session, encoding="utf-8", errors="replace").read()
    imggen = text.count('"image_generation_end"')
    shell = text.count('"exec_command_begin"')
    used = re.findall(r'"used_percent":([\d.]+)', text)[-2:]

    imgs = glob.glob(os.path.join(CODEX_HOME, "generated_images", sid, "*.png"))
    if not imgs:
        sys.exit(f"ERROR: Codex session {sid} produced no image.\n" + res.stdout[-2000:])
    src = max(imgs, key=os.path.getmtime)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    saved = fit(src, a.out, w, h)
    print(json.dumps({"out": saved, "raw": src, "session": sid, "tokens": tokens[-1] if tokens else None,
                      "image_generations": imggen, "shell_commands": shell,
                      "codex_used_percent_5h_7d": used}, ensure_ascii=False))
    if shell:
        print("WARNING: Codex ran shell commands; the prompt must forbid that.")


if __name__ == "__main__":
    main()
