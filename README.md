# npm package search API — examples

Search the npm registry — version, description, license, downloads, quality score, links.

**Live page, full schema & pricing → [quanticdata.io/collectors/npm-registry-api/](https://quanticdata.io/collectors/npm-registry-api/)**

Searches the npm registry and delivers one row per package: name, version, description, keywords, license, publisher, homepage/repository links, last-publish date, the registry quality score and weekly/monthly download counts. Reads the registry's own public search endpoint — no token, no rate ceiling to manage.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/npm_packages/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "react state management", "max_results": 20}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — Search text — package name, keyword, author:… or scope.
- `max_results` (integer) — How many packages to deliver at most (1–100). You pay only for delivered packages.

## Output — one row per package

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `name` | string | Package name. |
| `version` | string | Latest version. |
| `description` | string | Package description. |
| `keywords` | string[] | Declared keywords. |
| `license` | string | License (SPDX). |
| `publisher` | string | Last publisher. |
| `homepage` | string | Homepage URL. |
| `repository` | string | Repository URL. |
| `npm_url` | string | npmjs.com package URL. |
| `published_at` | string | Last publish (ISO 8601). |
| `quality_score` | number | Registry final score 0–1. |
…and 3 more fields — full schema on the [live page](https://quanticdata.io/collectors/npm-registry-api/).

## Pricing

**$0.0003 per delivered package** ($0.3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 6,666 packages — no card required.

## Links

- This collector: https://quanticdata.io/collectors/npm-registry-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
