# Changelog

## [Unreleased]

### Changed

- Site crawling now runs on ScrapeGraphAI. **Breaking:** the skill is
  `seo-scrapegraph`, the command is `/seo scrapegraph`, and the extension lives
  at `extensions/scrapegraph/`. Uninstall the previous crawling extension, then
  run `./extensions/scrapegraph/install.sh`.
- ScrapeGraphAI is a hosted Streamable HTTP MCP server, so the extension no
  longer requires Node.js, an npm package, or a proxy binary. The installer
  writes a `url` plus `X-API-Key` header entry rather than a spawned `npx`
  command with an env block.
- The shared cache artifact is `scrapegraph.json` with `cache_type: scrapegraph`.
- Crawling is asynchronous: `crawl_start` returns an id, then `crawl_get` and
  `crawl_pages` read results. `search` is web-wide and scoped with a `site:`
  operator. There is no `map` endpoint; the skill uses a links-only scrape or
  crawl and prefers the XML sitemap where one exists.

### Added

- `extract` command for schema-typed page extraction (meta, JSON-LD, product,
  and E-E-A-T fields). The previous crawling extension had no counterpart.

### Fixed

- `configured_mcp_server()` recognised credentials only in an `env` block, so a
  header-authenticated hosted server always reported as unconfigured. It now
  accepts either, and returns key names only.
- The installer passed the API key by interpolating it into embedded Python
  source, where a key containing quotes could break out of the string literal.
  It now travels through the environment.
- Set the exec bit on `extensions/scrapegraph/install.sh` and `uninstall.sh`,
  which the README has always told users to run directly.

### Verified

- `bash -n` on both shell scripts, `py_compile` on changed Python, and a
  compile check of the installers' embedded Python blocks.
- Installer and uninstaller run end-to-end against a scratch `CODEX_HOME`,
  including an API key containing quotes, backslashes, and `$(...)`.
- `run_skill_workflow.py --skill seo-scrapegraph` reports `mcp_configured` when
  the header is present and `setup_required` once removed, with no credential
  in any emitted artifact.
- `seo-dataforseo`, `seo-maps`, and `seo-image-gen` still resolve through the
  unchanged env-based path.

## [1.9.6+codex.5] - 2026-04-28

### Fixed

- Hardened installer bootstrap JSON transport on macOS, Linux, and PowerShell by writing the bootstrap payload to a dedicated JSON file instead of scraping mixed stdout/stderr.
- Added structured JSON error output when bootstrap fails before environment verification, so platform failures produce actionable diagnostics instead of raw tracebacks.
- Added PowerShell fallback parsing through Python for large or deeply nested bootstrap payloads.
- Truncated captured subprocess logs inside bootstrap JSON to keep installer parsing stable.
- Updated public install refs to `v1.9.6-codex.5` so users receive the macOS Python 3.14 bootstrap fix from `main`.

## [1.9.6+codex.1] - 2026-04-27

### Added

- Synced Codex SEO to `AgriciDaniel/claude-seo` `main` at `a9cf338`.
- Added Codex plugin manifest at `.codex-plugin/plugin.json`.
- Expanded to 26 specialist workflows and 24 Codex TOML agent profiles.
- Added upstream backlink, cluster, local, maps, Google APIs, SXO, drift, ecommerce, FLOW, DataForSEO, image-gen, and site-crawling workflows.
- Added upstream API/helper scripts for Google, backlinks, drift, DataForSEO, FLOW sync, reports, and verification.
- Added contract tests for plugin metadata, skill cache guidance, installer coverage, TOML agents, and FLOW sync safety.

### Changed

- Canonical skill tree is now `skills/`; `skills/seo/SKILL.md` is the main orchestrator.
- Installers default to `https://github.com/AgriciDaniel/codex-seo`.
- New credentials and runtime caches use `~/.config/codex-seo/` and `~/.cache/codex-seo/`.
- Legacy `~/.config/claude-seo/` and `~/.cache/claude-seo/` files are read only as migration fallback.
- Community footer is config-gated and disabled by default for Codex/API/client deliverables.

### Fixed

- Fixed cross-platform virtualenv Python resolution in `bootstrap_environment.py`.
- Fixed `run_headless_audit.py` `data_only` scoping for wrapper-driven audits.
- Hardened URL validation for private, loopback, reserved, multicast, unspecified, and metadata hosts.

### Verified

- `python -m pytest tests/`
- script compile/help checks for all Python scripts
- `bash -n install.sh uninstall.sh`
- PowerShell parse check for `install.ps1` and `uninstall.ps1`
- deterministic smoke runs for core, audit/page, and setup-required workflows
