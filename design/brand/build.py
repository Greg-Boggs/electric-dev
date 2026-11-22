#!/usr/bin/env python3
"""
Build the Electric Dev brand SVGs.

The mark is drawn by hand below. The wordmark is set in the style guide's
fonts (Source Serif 4 and IBM Plex Sans, weights 400 and 600) and converted to
outlines, so the SVGs need no web fonts. The business name is still open: change
NAME and DOMAIN, run this script, then run SVGO (see README.md).

Needs: python3 -m pip install fonttools brotli uharfbuzz
Run from design/brand/:  python3 build.py
"""
import io
import os

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

NAME = "Electric Dev"   # working name
DOMAIN = "electricdev.net"

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "svg")

# Palette, from the style guide's tokens.css
DEEP_WATER = "#0B2540"
DEEP_WATER_2 = "#12304F"
CURRENT = "#00707A"
SHALLOWS = "#7FC8CF"
BEACON = "#FFB547"
SLATE = "#475A70"
FOG = "#A9B8CA"
FOAM = "#E6EAF0"
WHITE = "#FFFFFF"
MIST = "#F5F8FB"


# ---------------------------------------------------------------- type
class Face:
    def __init__(self, file, wght):
        vf = TTFont(os.path.join(FONTS, file))
        self.tt = instancer.instantiateVariableFont(vf, {"wght": wght})
        buf = io.BytesIO()
        self.tt.flavor = None
        self.tt.save(buf)
        self.hbfont = hb.Font(hb.Face(hb.Blob(buf.getvalue())))
        self.upem = self.tt["head"].unitsPerEm
        self.glyphs = self.tt.getGlyphSet()

    def cap_height(self):
        return self.tt["OS/2"].sCapHeight

    def path(self, text, size, x=0.0, baseline=0.0, tracking=0.0):
        """Outline `text` at `size` px, left edge x, on `baseline`. Returns (d, width)."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True, "liga": True})
        s = size / self.upem
        track = tracking * self.upem  # tracking in em
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        cx = 0.0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = self.tt.getGlyphName(info.codepoint)
            t = TransformPen(pen, (s, 0, 0, -s, x + (cx + pos.x_offset) * s, baseline - pos.y_offset * s))
            self.glyphs[name].draw(t)
            cx += pos.x_advance + track
        cx -= track
        return pen.getCommands(), cx * s

    def ink(self, text, size, tracking=0.0):
        """Ink bounds (xmin, ymin, xmax, ymax) in px, y down, baseline at 0."""
        bp = BoundsPen(None)
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True, "liga": True})
        s = size / self.upem
        cx = 0.0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = self.tt.getGlyphName(info.codepoint)
            self.glyphs[name].draw(TransformPen(bp, (s, 0, 0, -s, (cx + pos.x_offset) * s, 0)))
            cx += pos.x_advance + tracking * self.upem
        return bp.bounds


SERIF_600 = Face("source-serif-4-latin-wght-normal.woff2", 600)
SANS_400 = Face("ibm-plex-sans-latin-wght-normal.woff2", 400)
SANS_600 = Face("ibm-plex-sans-latin-wght-normal.woff2", 600)


# ---------------------------------------------------------------- the mark
# "Log bracket": a bracket that reads as an E, with one amber line inside.
# Drawn on a 48-unit grid. Bracket stroke is 8 units; the amber pill is 8 tall.
# The bracket is the machine; the amber pill is the beacon: the one live line,
# the moment a fix is happening (amber is the style guide's status color).
BRACKET = (
    "M16 8h20a4 4 0 0 1 0 8H16v16h20a4 4 0 0 1 0 8H16a8 8 0 0 1-8-8V16a8 8 0 0 1 8-8z"
)
PILL = "M24 20h8a4 4 0 0 1 0 8h-8a4 4 0 0 1 0-8z"  # x 20..36, y 20..28
TILE_R = 12


FREE = "translate(-9 -3) scale(1.125)"  # tileless mark: bracket 36 tall, flush left


def mark(bracket, pill, tile=None, tile_stroke=None):
    out = []
    if tile:
        extra = f' stroke="{tile_stroke}" stroke-width="1"' if tile_stroke else ""
        inset = 0.5 if tile_stroke else 0
        size = 48 - 2 * inset
        out.append(
            f'<rect x="{inset}" y="{inset}" width="{size}" height="{size}" rx="{TILE_R - inset}" fill="{tile}"{extra}/>'
        )
    out.append(f'<path fill="{bracket}" d="{BRACKET}"/>')
    out.append(f'<path fill="{pill}" d="{PILL}"/>')
    return "".join(out)


def svg(w, h, body, title, origin=(0, 0)):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(origin[0])} {fmt(origin[1])} {fmt(w)} {fmt(h)}" '
        f'width="{fmt(w)}" height="{fmt(h)}" role="img" aria-labelledby="t">'
        f'<title id="t">{title}</title>{body}</svg>\n'
    )


def fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def write(name, content):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


# ---------------------------------------------------------------- lockups
WORD_SIZE = 30          # px at a 48px mark
WORD_TRACK = -0.01      # em, same as the style guide's headings
GAP = 14                # mark to wordmark


def wordmark_metrics(face=SERIF_600, size=WORD_SIZE, track=WORD_TRACK):
    xmin, ymin, xmax, ymax = face.ink(NAME, size, track)
    return xmin, ymin, xmax, ymax


def horizontal(word_fill, bracket, pill, tile, tile_stroke=None, face=SERIF_600, title=None):
    xmin, ymin, xmax, ymax = wordmark_metrics(face)
    cap = face.cap_height() * WORD_SIZE / face.upem
    baseline = 24 + cap / 2  # center caps on the mark
    mark_w = 48 if tile else 36
    x0 = mark_w + GAP - xmin
    d, _ = face.path(NAME, WORD_SIZE, x0, baseline, WORD_TRACK)
    width = x0 + xmax
    m = mark(bracket, pill, tile, tile_stroke)
    if not tile:
        m = f'<g transform="{FREE}">{m}</g>'
    body = m + f'<path fill="{word_fill}" d="{d}"/>'
    return svg(width, 48, body, title or NAME)


def stacked(word_fill, domain_fill, bracket, pill, tile, tile_stroke=None):
    size = 30
    xmin, ymin, xmax, ymax = SERIF_600.ink(NAME, size, WORD_TRACK)
    dsize = 15
    dxmin, dymin, dxmax, dymax = SANS_400.ink(DOMAIN, dsize, 0.02)
    word_w = xmax - xmin
    dom_w = dxmax - dxmin
    width = max(word_w, dom_w, 64)
    mark_scale = 64 / 48
    mx = (width - 64) / 2
    word_base = 64 + 18 - ymin  # 18px gap under mark, ymin is negative (cap top)
    wx = (width - word_w) / 2 - xmin
    d, _ = SERIF_600.path(NAME, size, wx, word_base, WORD_TRACK)
    dom_base = word_base + ymax + 10 - dymin
    dx = (width - dom_w) / 2 - dxmin
    dd, _ = SANS_400.path(DOMAIN, dsize, dx, dom_base, 0.02)
    height = dom_base + dymax
    m = mark(bracket, pill, tile, tile_stroke)
    if not tile:
        m = f'<g transform="{FREE}">{m}</g>'
    body = (
        f'<g transform="translate({fmt(mx)} 0) scale({fmt(mark_scale)})">{m}</g>'
        f'<path fill="{word_fill}" d="{d}"/><path fill="{domain_fill}" d="{dd}"/>'
    )
    return svg(width, height, body, f"{NAME}, {DOMAIN}")


def wordmark_only(fill):
    xmin, ymin, xmax, ymax = SERIF_600.ink(NAME, WORD_SIZE, WORD_TRACK)
    d, _ = SERIF_600.path(NAME, WORD_SIZE, -xmin, -ymin, WORD_TRACK)
    return svg(xmax - xmin, ymax - ymin, f'<path fill="{fill}" d="{d}"/>', NAME)


def domain_lockup(fill_word, fill_tld):
    """electricdev.net set in Plex Sans 600, with .net in a second color."""
    size = 30
    full = DOMAIN
    xmin, ymin, xmax, ymax = SANS_600.ink(full, size, -0.005)
    base_name = full.split(".")[0]
    d1, w1 = SANS_600.path(base_name, size, -xmin, -ymin, -0.005)
    d2, _ = SANS_400.path("." + full.split(".", 1)[1], size, -xmin + w1, -ymin, -0.005)
    _, _, xmax2, _ = SANS_400.ink("." + full.split(".", 1)[1], size, -0.005)
    width = w1 + xmax2
    body = f'<path fill="{fill_word}" d="{d1}"/><path fill="{fill_tld}" d="{d2}"/>'
    return svg(width, ymax - ymin, body, DOMAIN)


def og_image():
    """1200x630 social card: deep water, free mark, wordmark, domain. No tagline."""
    W, H = 1200, 630
    size = 84
    xmin, ymin, xmax, ymax = SERIF_600.ink(NAME, size, WORD_TRACK)
    mark_px = 136
    gap = 40
    total = mark_px + gap + (xmax - xmin)
    x = (W - total) / 2
    cap = SERIF_600.cap_height() * size / SERIF_600.upem
    cy = 290
    d, _ = SERIF_600.path(NAME, size, x + mark_px + gap - xmin, cy + cap / 2, WORD_TRACK)
    dsize = 30
    dxmin, dymin, dxmax, dymax = SANS_400.ink(DOMAIN, dsize, 0.02)
    dd, _ = SANS_400.path(DOMAIN, dsize, x + mark_px + gap - dxmin, cy + cap / 2 + 60, 0.02)
    s = mark_px / 48
    rings = "".join(
        f'<circle cx="1080" cy="560" r="{r}" fill="none" stroke="{SHALLOWS}" stroke-opacity="{o}" stroke-width="2"/>'
        for r, o in ((120, 0.18), (200, 0.13), (280, 0.09), (360, 0.06))
    )
    body = (
        f'<rect width="{W}" height="{H}" fill="{DEEP_WATER}"/>{rings}'
        f'<g transform="translate({fmt(x)} {fmt(cy - mark_px / 2)}) scale({fmt(s)})">{mark(WHITE, BEACON, DEEP_WATER_2)}</g>'
        f'<path fill="{WHITE}" d="{d}"/><path fill="{FOG}" d="{dd}"/>'
    )
    return svg(W, H, body, f"{NAME}, {DOMAIN}")


# ---------------------------------------------------------------- other concepts
def concept_signal():
    # A: one line that runs like a current and ends in a beacon dot.
    body = (
        f'<rect width="48" height="48" rx="{TILE_R}" fill="{DEEP_WATER}"/>'
        f'<path fill="none" stroke="{SHALLOWS}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" '
        f'd="M9 30c4 0 5-12 9.5-12S24 30 28.5 30 31 24 33 24"/>'
        f'<circle cx="38" cy="24" r="4.5" fill="{BEACON}"/>'
    )
    return svg(48, 48, body, "Concept A: signal line")


def concept_rings():
    # C: tide rings radiating from a beacon in the lower left.
    body = (
        f'<rect width="48" height="48" rx="{TILE_R}" fill="{DEEP_WATER}"/>'
        f'<path fill="none" stroke="{SHALLOWS}" stroke-width="4.5" stroke-linecap="round" '
        f'd="M13 24.5A10.5 10.5 0 0 1 23.5 35M13 15a20 20 0 0 1 20 20"/>'
        f'<circle cx="14" cy="34" r="5" fill="{BEACON}"/>'
    )
    return svg(48, 48, body, "Concept C: beacon rings")


def main():
    # Mark
    write("mark-tile.svg", svg(48, 48, mark(WHITE, BEACON, DEEP_WATER), NAME))
    write("mark-reverse.svg", svg(32, 32, mark(WHITE, BEACON), NAME, (8, 8)))
    write("mark-navy.svg", svg(32, 32, mark(DEEP_WATER, DEEP_WATER), NAME, (8, 8)))
    write("mark-white.svg", svg(32, 32, mark(WHITE, WHITE), NAME, (8, 8)))
    write("mark-tile-raised.svg", svg(48, 48, mark(WHITE, BEACON, DEEP_WATER_2, "#4A6684"), NAME))
    # Favicon: same tile; at 16px the grid lands on whole-ish pixels
    write("favicon.svg", svg(48, 48, mark(WHITE, BEACON, DEEP_WATER), NAME))

    # Lockups
    write("lockup.svg", horizontal(DEEP_WATER, WHITE, BEACON, DEEP_WATER))
    write("lockup-reverse.svg", horizontal(WHITE, WHITE, BEACON, None))
    write("lockup-navy.svg", horizontal(DEEP_WATER, DEEP_WATER, DEEP_WATER, None))
    write("lockup-white.svg", horizontal(WHITE, WHITE, WHITE, None))
    write("lockup-sans.svg", horizontal(DEEP_WATER, WHITE, BEACON, DEEP_WATER, face=SANS_600))
    write("lockup-stacked.svg", stacked(DEEP_WATER, SLATE, WHITE, BEACON, DEEP_WATER))
    write("lockup-stacked-reverse.svg", stacked(WHITE, FOG, WHITE, BEACON, None))
    write("wordmark.svg", wordmark_only(DEEP_WATER))
    write("domain.svg", domain_lockup(DEEP_WATER, CURRENT))

    # Social card
    write("og-image.svg", og_image())

    # Other concepts, for comparison only
    write("concept-a-signal.svg", concept_signal())
    write("concept-c-rings.svg", concept_rings())


if __name__ == "__main__":
    main()
