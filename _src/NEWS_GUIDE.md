# GESA Group Insights: how to add a news note

GESA Group is the bridge between the United States and the Caucasus & Central Asia
(Georgia, Armenia, Azerbaijan, Kazakhstan, Uzbekistan). Insights publishes POSITIVE news
about business ties between these countries: US with any of the five, and the five with each other.

## Rhythm and approval
- One note every 4 days, plus one LinkedIn post on the GESA group company page
  (https://www.linkedin.com/company/gesa-group, admin id 86365036).
- Nothing is published (site or LinkedIn) without Kardu's explicit "yes" for that note.

## What qualifies
- Trade, investment, finance, infrastructure, transport/Middle Corridor, energy, minerals,
  aviation, real estate or company deals linking the US and the region, or linking
  the region's countries with each other. Prefer stories from the last ~2 weeks.
- Skip politics, conflict, sanctions stories and anything negative. Never touch sanctioned
  parties or Russia-related deals.
- Reputable sources only (official ministries/agencies, Reuters, Bloomberg, RFE/RL, Euronews,
  Eurasianet, Times of Central Asia, Astana Times, Kun.uz, Spot.uz, Trend, Report.az,
  Civil.ge, bne IntelliNews). Open the original and check every number and its period.
- Do not repeat a story already in `news/` (check slugs and titles).

## Writing rules
- English, own words, no copied sentences, no hype, no emojis.
- Every figure must come from the listed sources. State targets as targets, not as money invested.
- Always include a short "risk" line (what is not yet done or uncertain).
- Title may use `<b>…</b>` for the bold half (site style: light + bold). Use HTML entities
  (&rsquo; &ndash; &amp;) in titles and text. No double quotes inside "dek".

## File format: `_src/news/YYYY-MM-DD-<slug>.json`
```json
{
  "slug": "short-kebab-slug",
  "date": "YYYY-MM-DD",            // publication date on our site
  "status": "published",           // or "draft" (not built)
  "countries": ["United States", "Uzbekistan"],
  "title": "Plain part <b>bold part</b>",
  "dek": "One-sentence summary.",
  "figs": [["54", "label"], ["USD 12bn", "label"], ["8+", "label"]],
  "sections": [{"h": "What happened", "p": ["paragraph", "paragraph"]}],
  "why": ["What it means for business, 2-3 bullets"],
  "risk": "One sentence.",
  "sources": [{"title": "...", "outlet": "...", "date": "20 October 2026", "url": "https://..."}],
  "linkedin": "Full LinkedIn post text (80-150 words, key number first, source line, 3-5 hashtags)",
  "linkedin_status": "awaiting approval | posted YYYY-MM-DD | not planned"
}
```

## Build and publish
1. `python3 _src/build.py` from the repo root (generates insights.html, insights-<slug>.html,
   updates the home page block "News from the bridge").
2. Check the new page exists and has the right h1.
3. Commit (`Insights: <title>`) and push to `main`. GitHub Pages updates in 1-2 minutes:
   https://kardu89.github.io/us-deals-site/insights.html
4. Bump `CSSV` in build.py only when style.css changes.
