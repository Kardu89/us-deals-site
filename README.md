# GESA Group website (test version)

US to the Caucasus (Georgia, Armenia, Azerbaijan). Static site, English only.

## How it is built
- Sources are in `_src/` (GitHub Pages does not serve folders starting with `_`).
- Edit `_src/build.py` (pages and texts), `_src/style.css`, or add an Insights article as `_src/news/<YYYY-MM-DD>-<slug>.json` (format: `_src/NEWS_GUIDE.md`).
- Then run `python3 _src/build.py` and commit everything. The generated HTML files sit in the repo root.

## Placeholders to replace
- `XX` - team, US track record, typical deal size, final form questions

## Photos
Hotlinked from Pexels (free licence). Replace with own photos later.

## Hosting
Hosted on Netlify from `main` (no build command, publish directory `.`; see `netlify.toml`). Forms use Netlify Forms (AJAX POST to `/`); notifications go to the address set in Netlify → Forms → Notifications. The GitHub Pages copy shows a test-mode message instead of sending.

**Deploys cost Netlify credits (free plan, 300 a month shared with other sites).** Netlify builds only when the latest commit message contains `[deploy]` (see `ignore` in `netlify.toml`); other pushes wait for the next `[deploy]` commit. Batch changes and publish at most once every 3 days.

## Before going live
Remove the `noindex` meta tag from every page, replace robots.txt, add canonical and Open Graph tags and a sitemap once the domain is chosen.
