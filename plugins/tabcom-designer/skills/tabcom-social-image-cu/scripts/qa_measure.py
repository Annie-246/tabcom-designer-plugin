"""Measure a rendered post: margins on each side and whether content is cropped by the canvas edge.

Usage: python -I qa_measure.py image.png [--min-margin 48]

Background colour is estimated from the four corners. "Solid content" = pixels that differ strongly from it.
For busy/full-bleed backgrounds the extents are not meaningful; then check visually instead.
Exit code 1 if any margin is below --min-margin.
"""
import argparse
import json

import numpy as np
from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--min-margin", type=int, default=48)
    ap.add_argument("--threshold", type=int, default=120)
    a = ap.parse_args()

    px = np.asarray(Image.open(a.image).convert("RGB")).astype(int)
    h, w, _ = px.shape
    k = max(8, min(h, w) // 40)
    corners = np.concatenate([px[:k, :k], px[:k, -k:], px[-k:, :k], px[-k:, -k:]]).reshape(-1, 3)
    bg = np.median(corners, 0)
    corner_spread = float(np.abs(corners - bg).sum(1).mean())
    solid = np.abs(px - bg).sum(2) > a.threshold
    ys, xs = np.where(solid)
    if len(xs) == 0:
        print(json.dumps({"error": "no content found"}))
        return 1
    m = {"left": int(xs.min()), "right": int(w - 1 - xs.max()), "top": int(ys.min()), "bottom": int(h - 1 - ys.max())}
    report = {
        "size": [w, h],
        "background_rgb": [int(v) for v in bg],
        "busy_background": corner_spread > 60,
        "margins_px": m,
        "below_min": [s for s, v in m.items() if v < a.min_margin],
    }
    print(json.dumps(report, ensure_ascii=False))
    return 1 if report["below_min"] and not report["busy_background"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
