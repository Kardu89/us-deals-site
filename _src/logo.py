#!/usr/bin/env python3
"""GESA Group logo, option 1 (wordmark: GESA + orange dash + GROUP) on the navy gradient.
Writes assets/gesa-logo.png (800x800, for LinkedIn) and favicon.svg (navy square, white G, orange dash).
Run from the repo root: python3 _src/logo.py  (needs Playwright + Chromium, fontTools, Inter Display)."""
import json, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
L = json.load(open(os.path.join(HERE, "gesa_letters.json")))

# --- favicon: just the G
f = TTFont("/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf")
gs, cap = f.getGlyphSet(), f["OS/2"].sCapHeight
pen = SVGPathPen(gs)
gs[f.getBestCmap()[ord("G")]].draw(TransformPen(pen, (1, 0, 0, -1, 0, cap)))
s = 17 / cap                                   # G cap height 17 units in a 32-unit icon
fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#14213D"/>'
       f'<path d="{pen.getCommands()}" fill="#fff" transform="translate({16 - 1500 * s / 2:.2f} 5) scale({s:.5f})"/>'
       f'<rect x="10" y="25" width="12" height="2.4" fill="#F28C28"/></svg>')
open(os.path.join(ROOT, "favicon.svg"), "w").write(fav)

# --- 800x800 logo
W = 800
ww = 500                                       # wordmark width
wh = ww * L["height"] / L["width"]
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0}}
.lg{{width:{W}px;height:{W}px;display:grid;place-items:center;background:linear-gradient(135deg,#0E1830,#1F3157)}}
.in{{display:grid;justify-items:start;gap:32px}}
.g{{display:flex;align-items:center;gap:24px}}
.g span:first-child{{width:68px;height:10px;background:#F28C28}}
.g span:last-child{{font:600 54px "Inter";letter-spacing:.42em;color:#C9D2E3;margin-right:-.42em}}
</style></head><body><div class="lg"><div class="in">
<svg width="{ww}" height="{wh:.0f}" viewBox="0 -20 {L["width"]} {L["height"] + 40}"><path d="{L["d"]}" fill="#fff"/></svg>
<div class="g"><span></span><span>GROUP</span></div></div></div></body></html>'''
tmp = os.path.join(HERE, "_logo.html")
open(tmp, "w").write(page)
os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": W})
    pg.goto("file://" + tmp); pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(ROOT, "assets", "gesa-logo.png"))
    b.close()
os.remove(tmp)
print("ok")
