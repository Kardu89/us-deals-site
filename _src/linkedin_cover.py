#!/usr/bin/env python3
"""LinkedIn cover for the GESA group page, direction D: deep navy gradient, oversized outlined GESA letters,
orange rule, headline. 1128x191, rendered at 2x into assets/gesa-linkedin-cover.png.
Run from the repo root: python3 _src/linkedin_cover.py  (needs Playwright + Chromium and Inter Display installed)."""
import json, os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
L = json.load(open(os.path.join(HERE, "gesa_letters.json")))
W, H = 1128, 191

cap = 186                               # letter cap height in px; bottom is cropped by the frame
s = cap / L["height"]
lw = L["width"] * s
lx, ly = W - 18 - lw, H + 30 - cap      # right-aligned, bottom running off the edge

page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:#0E1830}}
.b{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:"Inter Display","Inter",sans-serif}}
.t{{position:absolute;left:388px;top:56px;color:#fff}}
.t p{{margin:0}}
.r{{width:40px;height:3px;background:#F28C28;margin-bottom:16px}}
.h{{font-size:21px;line-height:1.18;font-weight:300;letter-spacing:-.01em}}
.h b{{font-weight:700}}
.s{{margin-top:11px!important;font-size:11px;color:#C9D2E3;letter-spacing:.02em}}
.s i{{font-style:normal;color:#F28C28;padding:0 6px}}
</style></head><body><div class="b">
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;inset:0">
 <defs><linearGradient id="bg" x1="0" x2="1"><stop offset="0" stop-color="#0E1830"/><stop offset="1" stop-color="#1F3157"/></linearGradient></defs>
 <rect width="{W}" height="{H}" fill="url(#bg)"/>
 <path d="{L["d"]}" transform="translate({lx:.1f} {ly:.1f}) scale({s:.5f})" fill="none" stroke="#33497A" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
</svg>
<div class="t"><div class="r"></div>
 <p class="h">The bridge between the US and<br><b>the Caucasus &amp; Central Asia</b></p>
 <p class="s">Real estate<i>&middot;</i>Trade finance<i>&middot;</i>Advisory</p>
</div></div></body></html>'''

os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
tmp = os.path.join(HERE, "_cover.html")
open(tmp, "w").write(page)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    pg.goto("file://" + tmp)
    pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(ROOT, "assets", "gesa-linkedin-cover.png"), clip={"x": 0, "y": 0, "width": W, "height": H})
    b.close()
os.remove(tmp)
print("ok")
