# GESA Group website (test version)

US to the Caucasus & Central Asia. Static site, English only.

## How it is built
- Sources are in `_src/` (GitHub Pages does not serve folders starting with `_`).
- Edit `_src/build.py` (pages and texts), `_src/style.css`, or add an Insights article as `_src/news/<YYYY-MM-DD>-<slug>.json` (format: `_src/NEWS_GUIDE.md`).
- Then run `python3 _src/build.py` and commit everything. The generated HTML files sit in the repo root.

## Placeholders to replace
- `XX` - email, phone, WhatsApp, team, US track record, typical deal size, final form questions

## Photos
Hotlinked from Pexels (free licence). Replace with own photos later.

## Hosting
GitHub Pages from `main` / root. For Netlify: no build command, publish directory `.`; forms already carry `data-netlify="true"`.

## Before going live
Remove the `noindex` meta tag from every page, replace robots.txt, add canonical and Open Graph tags and a sitemap once the domain is chosen.
