# ScrapeGraphAI Setup Guide

## 1. Get Your API Key

1. Go to [scrapegraphai.com/dashboard](https://scrapegraphai.com/dashboard)
2. Create a free account (500 credits included on signup)
3. Navigate to **API Keys** in the dashboard
4. Copy your API key (starts with `sgai-`)

## 2. Run the Installer

The installer handles everything automatically:

```bash
./extensions/scrapegraph/install.sh
```

It will prompt for your API key and configure the MCP server.

## 3. Manual MCP Configuration

ScrapeGraphAI is a hosted Streamable HTTP MCP server, so there is no package to
install and no proxy command to spawn -- the client connects to the endpoint and
authenticates with a header.

If the installer fails, add this to `~/.codex/settings.json` manually:

```json
{
  "mcpServers": {
    "scrapegraph": {
      "url": "https://mcp.scrapegraphai.com/mcp",
      "headers": {
        "X-API-Key": "sgai-your-api-key-here"
      }
    }
  }
}
```

Codex also reads `~/.codex/config.toml`. The equivalent there is:

```toml
[mcp_servers.scrapegraph]
url = "https://mcp.scrapegraphai.com/mcp"
http_headers = { "X-API-Key" = "sgai-your-api-key-here" }
```

The endpoint accepts `X-API-Key`, `SGAI-APIKEY`, or `Authorization: Bearer sgai-...`.
Clients that read credentials from the environment instead of a header use
`SGAI_API_KEY`.

## 4. Verify Installation

Start Codex and try:

```
/seo scrapegraph map https://example.com
```

You should see a list of discovered URLs. If you get a "tool not available" error, restart Codex to reload MCP servers.

## 5. Understanding Credits

| Operation | Credits Used |
|-----------|-------------|
| `scrape` | 1 (markdown) to 25 (branding analysis) per page |
| `extract` | 5 per extraction |
| `search` | 2 per result, 5 per result with a prompt |
| `crawl` | 2 to start, plus the per-page `scrape` cost |
| `stealth` (any operation) | +5 |

**Free tier**: 500 credits granted once on signup. Paid plans refill monthly; top-ups never expire.

**Tip**: Run a links-only pass first (`formats: [{"type": "links"}]`, `mode: "fast"`) to
see how many pages a site has, then decide how many to crawl for full content.
Call the `credits` tool to check the balance before a large run.
