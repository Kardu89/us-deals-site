#!/usr/bin/env python3
"""LinkedIn cover for GESA group: 1128x191 (rendered at 2x). Navy, dot map cropped to 20-58N, orange arcs."""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))  # run from _src; writes banner.html + gesa-linkedin-cover.png here
ROWS = [r.strip() for r in open(os.path.join(HERE, "map_rows.txt")) if r.strip()]
LON0, LAT0, STEP = -128.0, 66.0, 1.6
W, H = 1128, 191
NCOL = len(ROWS[0])
CW = W / NCOL                      # px per grid cell
LAT_TOP = 58.5                     # latitude shown at the top edge
y_off = (LAT0 - LAT_TOP) / STEP * CW


def xy(lon, lat):
    return ((lon - LON0) / STEP + 0.5) * CW, ((LAT0 - lat) / STEP + 0.5) * CW - y_off


dots = []
for j, row in enumerate(ROWS):
    for i, ch in enumerate(row):
        if ch == "1":
            cx, cy = (i + 0.5) * CW, (j + 0.5) * CW - y_off
            if -4 < cy < H + 4:
                dots.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{CW*0.27:.2f}"/>')

US = {"New York": (-74.01, 40.71), "Miami": (-80.19, 25.76), "Tampa": (-82.46, 27.95)}
REG = {"Tbilisi": (44.79, 41.72), "Yerevan": (44.51, 40.18), "Baku": (49.87, 40.41),
       "Tashkent": (69.24, 41.30), "Almaty": (76.95, 43.24), "Astana": (71.43, 51.17)}
ALL = {**US, **REG}
arcs = []
for k, (a, b, cy) in enumerate([("New York", "Tbilisi", -20), ("Miami", "Tashkent", -60), ("New York", "Astana", -45), ("Tampa", "Baku", -50)]):
    x1, y1 = xy(*ALL[a]); x2, y2 = xy(*ALL[b])
    arcs.append(f'<path d="M{x1:.1f},{y1:.1f} Q{(x1+x2)/2:.1f},{cy} {x2:.1f},{y2:.1f}"/>')
cities = "".join(
    f'<circle cx="{xy(*p)[0]:.1f}" cy="{xy(*p)[1]:.1f}" r="11" fill="url(#g)"/><circle cx="{xy(*p)[0]:.1f}" cy="{xy(*p)[1]:.1f}" r="2.6" fill="#F28C28"/>'
    for p in ALL.values())

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <radialGradient id="g"><stop offset="0" stop-color="#F28C28" stop-opacity=".8"/><stop offset="1" stop-color="#F28C28" stop-opacity="0"/></radialGradient>
 <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#14213D" stop-opacity="0"/><stop offset="1" stop-color="#14213D" stop-opacity=".55"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="#14213D"/>
<g fill="#3A4D78" opacity=".8">{"".join(dots)}</g>
<g fill="none" stroke="#F28C28" stroke-width="1.4" stroke-linecap="round" opacity=".9">{"".join(arcs)}</g>
{cities}
<rect width="{W}" height="{H}" fill="url(#fade)"/>
</svg>'''

# text block sits over the Atlantic, centred so it survives the mobile crop
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:#14213D}}
.b{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:"Inter Display","Inter",sans-serif}}
.t{{position:absolute;left:388px;top:104px;color:#fff}}
.t p{{margin:0}}
.k{{font-size:9.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#C9D2E3;display:flex;align-items:center;gap:8px;margin-bottom:9px!important}}
.k:before{{content:"";width:20px;height:1.5px;background:#F28C28}}
.h{{font-size:20px;line-height:1.18;font-weight:300;letter-spacing:-.01em}}
.h b{{font-weight:700}}
.s{{margin-top:10px!important;font-size:10.5px;color:#C9D2E3;letter-spacing:.02em}}
.s i{{font-style:normal;color:#F28C28;padding:0 5px}}
</style></head><body><div class="b">{svg}
<div class="t">
 <p class="h">The bridge between the US and<br><b>the Caucasus &amp; Central Asia</b></p>
 <p class="s">Real estate<i>&middot;</i>Trade finance<i>&middot;</i>Advisory</p>
</div></div></body></html>'''

out_html = os.path.join(HERE, "banner.html")
open(out_html, "w").write(page)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    pg.goto("file://" + out_html)
    pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(HERE, "gesa-linkedin-cover.png"), clip={"x": 0, "y": 0, "width": W, "height": H})
    b.close()
print("ok")
