# [Brand] website (test version)

Static site, no build step. English only.

## Files
- index.html, real-estate.html, trade-finance.html, consulting.html, about.html, contact.html, 404.html
- style.css (one stylesheet), favicon.svg, robots.txt (blocks indexing while in test)

## Placeholders to replace later
- `[Brand]` - brand name (search and replace across all files)
- `XX` - email, phone, WhatsApp, team profiles, France and US track record, typical deal size, final form questions

## Publishing
GitHub Pages: repo Settings -> Pages -> Deploy from branch -> main / root.
Netlify (like K+A): import the repo, no build command, publish directory `.`. Forms already carry `data-netlify="true"`;
switch on Form detection and email notifications in Netlify.

## Before going live
- Remove `<meta name="robots" content="noindex, nofollow">` from every page and replace robots.txt
- Add canonical URLs, Open Graph tags, sitemap.xml once the domain is chosen
