---
name: seo-scrapegraph
description: >
  Full-site crawling, scraping, AI extraction, and site mapping via ScrapeGraphAI MCP.
  Use when user says "crawl site", "map site", "full crawl",
  "find all pages", "broken links", "site structure",
  "discover pages", "JS rendering", or needs site-wide analysis.
user-invokable: true
argument-hint: "[command] <url>"
license: MIT
compatibility: "Requires ScrapeGraphAI MCP server"
metadata:
  author: AgriciDaniel
  version: "1.7.2"
  category: seo
---

# ScrapeGraphAI Extension for Codex SEO
## Shared Data Cache

**Step 0 -- Check shared data cache:**

Before gathering, check `.seo-cache/` for reusable context from related SEO skills.
Reference: `../seo/references/shared-data-cache.md` for schemas and dependency map.

Check these cache files when present:
- `.seo-cache/site-meta.json` for domain, business type, industry, and crawl context
- `.seo-cache/audit-scores.json` for prior full-audit priorities
- `.seo-cache/pages/{url-slug}/page-analysis.json` for page-level context when a URL is provided

- If found: parse and use clearly valid fields (note "Using cached [X] from [date]")
- If missing, corrupt, or irrelevant: continue with fresh evidence
- If the user says "refresh" or "re-run": ignore cache reads and overwrite on write

This skill requires the ScrapeGraphAI extension to be installed:
```bash
./extensions/scrapegraph/install.sh
```

**Check availability:** Before using any ScrapeGraphAI tool, verify the MCP server
is connected by checking if `scrape` or any other tool from the `scrapegraph`
server is available. If tools are not available, inform the user the extension is
not installed and provide install instructions.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `/seo scrapegraph crawl <url>` | Full-site crawl with content extraction |
| `/seo scrapegraph map <url>` | Discover site structure (URLs only, cheap) |
| `/seo scrapegraph scrape <url>` | Single-page scrape with JS rendering |
| `/seo scrapegraph extract <url> <prompt>` | Schema-typed extraction from a page |
| `/seo scrapegraph search <query> <url>` | Search the web, scoped to a site |

## Commands

### crawl -- Full-Site Crawl

Crawl an entire website starting from the given URL. Returns page content,
metadata, and links for all discovered pages.

**MCP Tools:** `crawl_start`, then `crawl_get` / `crawl_pages`

Crawling is asynchronous. `crawl_start` returns a crawl `id`; poll `crawl_get(id)`
for status and read results in batches with `crawl_pages(id, cursor, limit)`.
`crawl_stop`, `crawl_resume`, and `crawl_delete` manage a run in flight -- stop a
crawl as soon as you have enough pages rather than letting it bill to completion.

**Parameters (`crawl_start`):**
- `url` (required): Starting URL to crawl
- `maxPages`: Max pages to crawl (default: 50)
- `maxDepth`: Max link depth from start URL (default: 2)
- `maxLinksPerPage`: Links followed per page (default: 10)
- `includePatterns`: Array of glob patterns to include (e.g., `["/blog/*"]`)
- `excludePatterns`: Array of glob patterns to exclude (e.g., `["/admin/*", "/api/*"]`)
- `allowExternal`: Follow links off the starting domain (default: false)
- `formats`: Output formats -- `[{"type": "markdown"}]`, `{"type": "html"}`, `{"type": "links"}`
- `fetchConfig.mode`: `auto` (default), `fast` (no JS), or `js` (force rendering)
- `fetchConfig.stealth`: Anti-bot evasion for protected sites (adds credits per page)

**SEO Usage Patterns:**
1. **Comprehensive audit crawl**: Crawl full site, extract all pages for subagent analysis
2. **Section-focused crawl**: Use `includePatterns` to audit only `/blog/*` or `/products/*`
3. **Broken link detection**: Crawl with `[{"type": "links"}]` format, check all hrefs for 404s
4. **Content inventory**: Extract all page titles, meta descriptions, H1s at scale
5. **SPA/JS-rendered sites**: `fetchConfig.mode: "js"` renders JavaScript, solving the Issue #11 problem

**Example orchestration for `/seo audit`:**
```
1. crawl_start(url, maxPages=200, formats=[{"type": "links"}], fetchConfig={"mode": "fast"})
   -> cheap URL discovery pass (see `map` below)
2. Filter to top 50 most important pages (homepage, key sections)
3. crawl_start(url, maxPages=50, includePatterns=[...]) -> get full content
4. crawl_pages(id) to page through results
5. Feed content to seo-technical, seo-content, seo-schema agents
```

**Cost awareness:**
- Free tier: 500 credits, one-time on signup
- `crawl` = 2 credits to start, plus the per-page `scrape` cost of the chosen format
- Markdown is the cheapest format (1 credit/page); `stealth` adds +5 per page
- Always inform user of estimated credit usage before large crawls
- `credits` returns the live balance -- check it before a crawl you cannot afford to fail halfway

### map -- Site Structure Discovery

Discover URLs on a website cheaply, without paying for full content extraction.

**MCP Tools:** `scrape` with `[{"type": "links"}]`, or `crawl_start` with the same format

ScrapeGraphAI has no dedicated map endpoint. Two honest substitutes:
- **Single hop:** `scrape(url, formats=[{"type": "links"}])` returns every link on one
  page. Cheapest possible discovery; good for a homepage or hub page.
- **Site-wide:** `crawl_start(url, formats=[{"type": "links"}], fetchConfig={"mode": "fast"})`
  walks the site and returns links only. Costs per page crawled, so bound it with
  `maxPages` and `maxDepth`.

Prefer the XML sitemap via `seo-sitemap` when the site publishes one -- it is free,
complete, and authoritative. Reach for a link crawl to find what the sitemap *omits*.

**SEO Usage Patterns:**
1. **Sitemap comparison**: Map site, compare discovered URLs vs XML sitemap
2. **Orphan page detection**: URLs in sitemap but not linked from any page
3. **Crawl budget analysis**: Total indexable pages vs pages linked from homepage
4. **URL pattern analysis**: Identify URL structure patterns, duplicates, parameter bloat
5. **Pre-audit discovery**: Run the link pass first, then targeted crawl on key sections

**Output:** Array of URLs. Present as:
```
Site: example.com
Pages discovered: 342

URL Pattern Breakdown:
  /blog/*          - 128 pages (37%)
  /products/*      - 89 pages (26%)
  /category/*      - 45 pages (13%)
  /pages/*         - 32 pages (9%)
  / (root pages)   - 48 pages (14%)
```

### scrape -- Single-Page Deep Scrape

Scrape a single page with full JavaScript rendering. More thorough than
`fetch_page.py` because it executes JS and waits for dynamic content.

**MCP Tool:** `scrape`

**Parameters:**
- `url` (required): Page URL to scrape
- `formats`: Output formats -- `markdown`, `html`, `links`, `images`, `screenshot`,
  `summary`, `branding`, `json`
- `fetchConfig.mode`: `auto` (default), `fast` (no JS), `js` (force rendering)
- `fetchConfig.wait`: Milliseconds to wait for dynamic content
- `fetchConfig.scrolls`: Scroll passes, for lazy-loaded content below the fold
- `fetchConfig.timeout`: Request timeout in ms (default: 60000)
- `fetchConfig.stealth`: Anti-bot evasion (+5 credits)
- `fetchConfig.country`: Geo-route the request for locale-specific pages

**SEO Usage Patterns:**
1. **SPA content extraction**: Scrape JS-rendered React/Vue/Angular pages
2. **Dynamic content audit**: Use `scrolls` for lazy-loaded content below the fold
3. **Paywall/login detection**: Identify content behind authentication walls
4. **Screenshot capture**: Use `screenshot` format for visual analysis
5. **Locale checks**: Use `country` to see what a market actually gets served

**When to use scrape vs fetch_page.py:**
| Scenario | Use |
|----------|-----|
| Static HTML page | `fetch_page.py` (no API cost) |
| JS-rendered SPA | `scrape` (renders JS) |
| Need response headers | `fetch_page.py` (returns headers) |
| Need clean markdown | `scrape` (better extraction) |
| Rate-limited/blocked | `scrape` with `stealth` (handles anti-bot) |

### extract -- Schema-Typed Page Extraction

Pull structured, typed data out of a page with an AI prompt and a JSON schema.
There is no `fetch_page.py` equivalent: this returns validated fields, not HTML
you still have to parse.

**MCP Tool:** `extract`

**Parameters:**
- `url` (or `html` / `markdown` if you already scraped the page)
- `prompt` (required): What to pull out
- `schema`: JSON schema the response must conform to
- `mode`: `normal` (default), `reader`, or `prune` for noisier pages
- `fetchConfig`: Same rendering controls as `scrape`

**SEO Usage Patterns:**
1. **Meta inventory at scale**: title, meta description, H1, canonical as typed fields
2. **Schema audit**: pull JSON-LD `@type` and required properties per page
3. **Product data**: price, availability, rating, review count for e-commerce audits
4. **Author/E-E-A-T signals**: byline, credentials, publish and update dates
5. **Competitor teardown**: same schema across competitor pages for a comparison table

**Cost:** 5 credits per extraction (+5 with `stealth`). Reuse one `scrape` result across
several extractions by passing `markdown` instead of `url` when you already have content.

### search -- Web Search With Extraction

Search the web and get extracted content back from the results.

**MCP Tool:** `search`

**Parameters:**
- `query` (required): Search query. Scope to one site with a `site:` operator,
  e.g. `site:example.com pricing`
- `numResults`: Max results (default: 3)
- `prompt`: Optional extraction prompt applied to each result
- `schema`: JSON schema for typed results
- `timeRange`: `past_hour`, `past_24_hours`, `past_week`, `past_month`, `past_year`
- `locationGeoCode`: Geo-target the search for local SERP work

> [!note]
> This is a web-wide search, not a site-scoped index. Use `site:example.com` in the
> query to restrict it. Results depend on what the search engine has indexed, so a
> page that exists but is unindexed will not appear -- that absence is itself an
> SEO finding worth reporting.

**SEO Usage Patterns:**
1. **Index coverage check**: `site:example.com <topic>` -- if nothing returns, the page may be unindexed
2. **Content gap validation**: Search for a keyword on the site to check if content exists
3. **Internal linking opportunities**: Find pages mentioning a topic that could link to each other
4. **Competitor content research**: Search a competitor site for specific topics
5. **Freshness checks**: Use `timeRange` to see what the site published recently

**Cost:** 2 credits per result, or 5 per result when `prompt` is set.

## Cross-Skill Integration

### With seo-audit (full audit)
When ScrapeGraphAI is available during `/seo audit`:
1. Use a links-only crawl to discover site URLs
2. Compare with XML sitemap (seo-sitemap) to find orphan/missing pages
3. Select top pages for deep analysis
4. Feed crawled content to all subagents (technical, content, schema, geo)
5. Report total crawlable pages, URL patterns, and crawl depth

### With seo-technical
- Broken link detection: crawl all internal links, check for 404s
- Redirect chain mapping: follow all redirects, flag chains > 2 hops
- Mixed content detection: check HTTP resources on HTTPS pages
- Canonical verification: compare canonical URLs with actual URLs

### With seo-sitemap
- Sitemap coverage: % of crawled pages present in sitemap
- Orphan pages: pages found by crawl but missing from sitemap
- Stale sitemap entries: URLs in sitemap that return 404/410

### With seo-content
- Content extraction: feed clean markdown to E-E-A-T analysis
- Thin content detection: identify pages with < 300 words at scale
- Duplicate content: compare content across pages for near-duplicates

### With seo-schema
- Schema extraction: use `extract` with a JSON-LD schema across all crawled pages
- Schema coverage: % of pages with structured data
- Schema validation: batch-validate extracted schemas

## Error Handling

| Error | Cause | Resolution |
|-------|-------|-----------|
| `SGAI_API_KEY not set` | MCP not configured | Run `./extensions/scrapegraph/install.sh` |
| `401 Unauthorized` | Bad or revoked key | Re-run the installer with a key from the dashboard |
| `402 Payment Required` | Credits exhausted | Check `credits`, top up at scrapegraphai.com/dashboard |
| `429 Too Many Requests` | Rate limited | Wait 60s, lower `maxPages` / `maxLinksPerPage` |
| Timeout | Page too slow to render | Raise `fetchConfig.timeout`, or use `mode: "fast"` |
| `403 Forbidden` | Site blocks crawling | Retry with `fetchConfig.stealth: true`; respect robots.txt |

**Graceful fallback:** If ScrapeGraphAI is unavailable, inform the user and suggest:
1. Use `fetch_page.py` for single-page analysis (no API cost)
2. Use `WebFetch` tool for basic HTML retrieval
3. Install ScrapeGraphAI: `./extensions/scrapegraph/install.sh`

## Write to shared data cache

After completing all work, write a concise JSON summary to `.seo-cache/` when the workflow produced durable findings.
Use the schemas and naming rules in `../seo/references/shared-data-cache.md`; include at least `cache_type`, `analyzed_at`, source URL/domain, key findings, issues, recommendations, and tool limitations. Add `.seo-cache/` to `.gitignore` if it is missing.
