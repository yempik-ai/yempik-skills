# ScrapeGraphAI Extension for Codex SEO

Full-site crawling, scraping, AI extraction, and site mapping powered by [ScrapeGraphAI](https://scrapegraphai.com/). Enables comprehensive site-wide SEO analysis with JavaScript rendering support.

## Prerequisites

- [Codex SEO](https://github.com/AgriciDaniel/codex-seo) installed
- ScrapeGraphAI API key ([dashboard](https://scrapegraphai.com/dashboard) -- free tier: 500 credits on signup)

No Node.js runtime is required. ScrapeGraphAI runs as a hosted Streamable HTTP MCP
server, so Codex connects to it directly with no proxy binary to install.

## Installation

### macOS / Linux

```bash
./extensions/scrapegraph/install.sh
```

### Windows (PowerShell)

```powershell
.\extensions\scrapegraph\install.ps1
```

The installer will prompt for your ScrapeGraphAI API key and configure the MCP server automatically.

## Commands

| Command | Purpose | Credits |
|---------|---------|---------|
| `/seo scrapegraph crawl <url>` | Full-site crawl with content extraction | 2 + per-page scrape cost |
| `/seo scrapegraph map <url>` | Discover site structure (links only) | 1 per page walked |
| `/seo scrapegraph scrape <url>` | Single-page deep scrape with JS rendering | 1 (markdown) to 25 (branding) |
| `/seo scrapegraph extract <url> <prompt>` | Schema-typed extraction from a page | 5 |
| `/seo scrapegraph search <query> <url>` | Web search scoped with `site:` | 2 per result, 5 with a prompt |

Enabling `stealth` for anti-bot evasion adds +5 credits to any operation.

## Integration with Codex SEO

When installed, other Codex SEO skills automatically leverage ScrapeGraphAI:

- **`/seo audit`**: Uses a links-only crawl to discover all pages, then a content crawl for deep analysis
- **`/seo technical`**: Broken link detection across entire site
- **`/seo sitemap`**: Compare XML sitemap vs actual crawlable pages
- **`/seo content`**: Thin content detection at scale
- **`/seo schema`**: Schema-typed `extract` for JSON-LD coverage across pages

## Cost

| Plan | Credits/month | Price |
|------|--------------|-------|
| Free | 500 (one-time) | $0 |
| Starter | 10,000 | $20/mo |
| Growth | 100,000 | $100/mo |
| Pro | 750,000 | $500/mo |
| Enterprise | Ad-hoc | Custom |

Credit top-ups never expire and stack on a subscription: $5 / 1,000, $40 / 10,000, $150 / 50,000.

Call the `credits` tool to read the live balance before an expensive crawl.

## Troubleshooting

**MCP not connecting?**
- Check sanitized workflow status: `python scripts/run_skill_workflow.py --skill seo-scrapegraph --json https://example.com`
- Manual config: See [SCRAPEGRAPH-SETUP.md](docs/SCRAPEGRAPH-SETUP.md)

**Credits exhausted?**
- Check usage: https://scrapegraphai.com/dashboard
- Top up or upgrade the plan

**Site blocking crawls?**
- Some sites block automated crawling via robots.txt or Cloudflare
- Retry with `fetchConfig.stealth: true` (+5 credits)
- Try `scrape` (single page) instead of `crawl` (full site)
- Fall back to `fetch_page.py` for basic HTML retrieval

## Uninstall

```bash
./extensions/scrapegraph/uninstall.sh      # macOS/Linux
.\extensions\scrapegraph\uninstall.ps1     # Windows
```

## Links

- [ScrapeGraphAI Documentation](https://docs.scrapegraphai.com/)
- [ScrapeGraphAI MCP Server](https://docs.scrapegraphai.com/services/mcp-server/introduction)
- [Codex SEO](https://github.com/AgriciDaniel/codex-seo)
