#!/usr/bin/env python3
"""Outlines the word GESA from Inter Display ExtraBold into one SVG path (_src/gesa_letters.json),
so the site hero and the LinkedIn cover use the exact same letterforms without loading a font."""
import json, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = "/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf"
TRACK = -0.04  # letter-spacing in em

f = TTFont(FONT)
gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
asc = f["OS/2"].sCapHeight
pen = SVGPathPen(gs)
x = 0
for ch in "GESA":
    name = cmap[ord(ch)]
    # flip y (font units are y-up), baseline at cap height so the path starts at y=0
    gs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, asc)))
    x += gs[name].width + TRACK * upm
width = x - TRACK * upm
out = {"d": pen.getCommands(), "width": round(width), "height": asc}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gesa_letters.json"), "w"))
print(out["width"], out["height"], len(out["d"]))
