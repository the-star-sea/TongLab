# TongLab

Public GitHub Pages site for Tong Lab.

Live site:
- https://the-star-sea.github.io/TongLab/

Current sections:
- Home
- People
- Projects
- Blogs
- Contact

## X news sync

The site now keeps a cached news block under `_data/x_news.json` and renders it on the homepage and `/pages/Blogs`.

How it works:
- `scripts/sync_x_news.py` fetches an RSS version of Stone's X timeline at build time
- `.github/workflows/sync-x-news.yml` refreshes that cache every 12 hours and on manual runs
- Jekyll reads `_data/x_news.json` and renders it through `_includes/x-news-feed.html`

Notes:
- This is intentionally feed-based and static-site friendly, so GitHub Pages does not need direct X API credentials
- If you have a preferred RSS bridge, set repository secret `X_NEWS_FEED_URL` to override the default public-instance list
- If feed fetching fails, the site keeps the last cached copy instead of breaking the build
