"""Render a hand-drawn style black & white whiteboard wireframe from a JSON design brief.

Usage: python -I render_wireframe.py brief.json out.png

Coordinates in the brief are in post-canvas pixels (1080x1080 by default).
Element types: box, text, pill, card, person, line, arrow, note (note = outside the canvas, right panel).
"""
import json
import math
import random
import sys

from PIL import Image, ImageDraw, ImageFont

FONTS_DIR = __file__.replace("\\", "/").rsplit("/brand/", 1)[0] + "/assets/fonts/be-vietnam-pro/"
FONT = FONTS_DIR + "BeVietnamPro-Regular.ttf"   # full Vietnamese coverage (Windows handwriting fonts lack it)
FONT_BOLD = FONTS_DIR + "BeVietnamPro-Bold.ttf"
INK = (25, 25, 25)
FAINT = (120, 120, 120)

SCALE = 0.8          # canvas px -> board px
PAD = 60             # board padding around the canvas
NOTES_W = 560        # right panel for notes

random.seed(7)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, max(10, int(size)))


class Board:
    def __init__(self, canvas):
        self.cw, self.ch = canvas
        w = int(self.cw * SCALE) + PAD * 2 + NOTES_W
        h = int(self.ch * SCALE) + PAD * 2
        self.img = Image.new("RGB", (w, h), (250, 250, 248))
        self.d = ImageDraw.Draw(self.img)

    def p(self, x, y):
        return PAD + x * SCALE, PAD + y * SCALE

    def wobbly(self, pts, width=3, color=INK, dash=False):
        """Marker-like polyline: small random jitter, optional dashes."""
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(2, int(math.hypot(x1 - x0, y1 - y0) / 18))
            seg = []
            for i in range(n + 1):
                t = i / n
                seg.append((x0 + (x1 - x0) * t + random.uniform(-1.2, 1.2),
                            y0 + (y1 - y0) * t + random.uniform(-1.2, 1.2)))
            if dash:
                for i in range(0, len(seg) - 1, 2):
                    self.d.line([seg[i], seg[i + 1]], fill=color, width=width)
            else:
                self.d.line(seg, fill=color, width=width, joint="curve")

    def rect(self, x, y, w, h, width=3, dash=False, color=INK):
        a, b = self.p(x, y)
        c, e = self.p(x + w, y + h)
        self.wobbly([(a, b), (c, b), (c, e), (a, e), (a, b)], width, color, dash)

    def rounded(self, x, y, w, h, r, width=3):
        a, b = self.p(x, y)
        c, e = self.p(x + w, y + h)
        self.d.rounded_rectangle([a, b, c, e], radius=r * SCALE, outline=INK, width=width)

    def text(self, x, y, s, size, bold=False, color=INK, raw=False):
        s = s.replace("→", "->").replace("▲", "+")  # glyphs missing in Be Vietnam Pro
        pos = (x, y) if raw else self.p(x, y)
        self.d.text(pos, s, font=font(size * (1 if raw else SCALE), bold), fill=color)

    def num(self, x, y, n):
        cx, cy = self.p(x, y)
        r = 16
        self.d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=3)
        f = font(20, True)
        tw = self.d.textlength(str(n), font=f)
        self.d.text((cx - tw / 2, cy - 15), str(n), font=f, fill=INK)

    def arrow(self, pts, label=None, dash=False):
        bp = [self.p(*q) for q in pts]
        self.wobbly(bp, 3, INK, dash)
        (x0, y0), (x1, y1) = bp[-2], bp[-1]
        ang = math.atan2(y1 - y0, x1 - x0)
        for s in (2.6, -2.6):
            self.d.line([(x1, y1), (x1 - 18 * math.cos(ang + s * 0.25), y1 - 18 * math.sin(ang + s * 0.25))],
                        fill=INK, width=3)
        if label:
            sx, sy = bp[0]
            self.d.text((sx - 10, sy + 12), label, font=font(20), fill=FAINT)

    def person(self, x, y, w, h, label=None):
        """Simple sketch: beanbag blob + reclining stick figure, inside box (x,y,w,h)."""
        bx, by = self.p(x, y + h * 0.45)
        ex, ey = self.p(x + w, y + h)
        self.d.ellipse([bx, by, ex, ey], outline=INK, width=3)
        hx, hy = self.p(x + w * 0.55, y + h * 0.12)
        r = w * 0.09 * SCALE
        self.d.ellipse([hx - r, hy - r, hx + r, hy + r], outline=INK, width=3)
        neck = (hx, hy + r)
        hip = self.p(x + w * 0.45, y + h * 0.62)
        self.wobbly([neck, hip])
        self.wobbly([self.p(x + w * 0.52, y + h * 0.3), self.p(x + w * 0.75, y + h * 0.2), (hx + r, hy)])
        cup = self.p(x + w * 0.25, y + h * 0.38)
        self.wobbly([self.p(x + w * 0.5, y + h * 0.33), cup])
        self.d.rectangle([cup[0] - 12, cup[1] - 26, cup[0] + 12, cup[1] + 10], outline=INK, width=2)
        self.wobbly([hip, self.p(x + w * 0.75, y + h * 0.7), self.p(x + w * 0.85, y + h * 0.95)])
        self.wobbly([hip, self.p(x + w * 0.35, y + h * 0.85), self.p(x + w * 0.4, y + h * 0.98)])
        if label:
            self.text(x, y + h + 6, label, 20, color=FAINT)


def render(brief, out):
    canvas = brief.get("canvas", [1080, 1080])
    b = Board(canvas)
    b.rect(0, 0, canvas[0], canvas[1], width=5)
    m = brief.get("margin")
    if m:
        b.rect(m, m, canvas[0] - 2 * m, canvas[1] - 2 * m, width=2, dash=True, color=FAINT)
        b.text(m + 4, m - 34, f"lề {m}px", 22, color=FAINT)
    for g in brief.get("guides", []):
        if g["axis"] == "x":
            b.wobbly([b.p(g["at"], g.get("from", 0)), b.p(g["at"], g.get("to", canvas[1]))], 2, FAINT, True)
        else:
            b.wobbly([b.p(g.get("from", 0), g["at"]), b.p(g.get("to", canvas[0]), g["at"])], 2, FAINT, True)
        if g.get("label"):
            lx, ly = (g["at"] + 6, g.get("from", 0) + 6) if g["axis"] == "x" else (g.get("from", 0) + 6, g["at"] - 30)
            b.text(lx, ly, g["label"], 20, color=FAINT)

    for e in brief["elements"]:
        t = e["type"]
        if t == "box":
            b.rect(e["x"], e["y"], e["w"], e["h"], dash=e.get("dash", False))
            b.text(e["x"] + 10, e["y"] + 8, e.get("label", ""), e.get("size", 22), bold=True)
        elif t == "text":
            y = e["y"]
            for line in e["lines"]:
                b.text(e["x"], y, line, e["size"], bold=e.get("bold", False))
                y += e["size"] * e.get("leading", 1.25)
        elif t == "pill":
            b.rounded(e["x"], e["y"], e["w"], e["h"], e["h"] / 2)
            b.text(e["x"] + 28, e["y"] + e["h"] * 0.22, e["label"], e.get("size", 26), bold=True)
        elif t == "card":
            b.rounded(e["x"], e["y"], e["w"], e["h"], 24)
            y = e["y"] + 14
            for line in e["lines"]:
                b.text(e["x"] + 18, y, line, e.get("size", 22), bold=line == e["lines"][-1])
                y += e.get("size", 22) * 1.5
        elif t == "person":
            b.person(e["x"], e["y"], e["w"], e["h"], e.get("label"))
        elif t == "arrow":
            b.arrow([tuple(q) for q in e["points"]], e.get("label"), e.get("dash", False))
        if e.get("num"):
            b.num(e["x"] - 30 if "x" in e else e["points"][0][0], (e["y"] + 18) if "y" in e else e["points"][0][1], e["num"])
        if e.get("note"):
            nx = e["x"] + e.get("w", 0) + 12 if "x" in e else 0
            b.text(e.get("note_x", nx), e.get("note_y", e.get("y", 0)), e["note"], 18, color=FAINT)

    # notes panel
    x0 = PAD * 2 + canvas[0] * SCALE
    y = PAD
    b.text(x0, y, brief.get("title", "DESIGN BRIEF"), 30, bold=True, raw=True)
    y += 56
    for line in brief.get("notes", []):
        b.text(x0, y, line, 21, raw=True)
        y += 34
    b.img.save(out)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        render(json.load(f), sys.argv[2])
    print("saved", sys.argv[2])
