#!/usr/bin/env bash
set -euo pipefail

# ScrapeGraphAI Extension Installer for Codex SEO
# Wraps everything in main() to prevent partial execution on network failure

MCP_ENDPOINT="https://mcp.scrapegraphai.com/mcp"

main() {
    CODEX_ROOT="${CODEX_HOME:-${HOME}/.codex}"
    SKILLS_ROOT="${CODEX_ROOT}/skills"
    SKILL_DIR="${SKILLS_ROOT}/seo-scrapegraph"
    AGENT_DIR="${CODEX_ROOT}/agents"
    SEO_SKILL_DIR="${SKILLS_ROOT}/seo"
    SETTINGS_FILE="${CODEX_ROOT}/settings.json"

    echo "════════════════════════════════════════"
    echo "║  ScrapeGraphAI Extension - Installer ║"
    echo "║   For Codex SEO                     ║"
    echo "════════════════════════════════════════"
    echo ""

    # Check prerequisites
    if [ ! -d "${SEO_SKILL_DIR}" ]; then
        echo "x Codex SEO is not installed."
        echo "  Install it first: curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/codex-seo/main/install.sh | bash"
        exit 1
    fi
    echo "v Codex SEO detected"

    if ! command -v python3 >/dev/null 2>&1; then
        echo "x python3 is required but not installed."
        exit 1
    fi
    echo "v python3 detected"

    # ScrapeGraphAI is a hosted Streamable HTTP MCP server: no Node.js runtime,
    # no npm package, no proxy binary. Codex connects to the endpoint directly.

    # Prompt for credentials
    echo ""
    echo "ScrapeGraphAI API key required."
    echo "Get one at: https://scrapegraphai.com/dashboard"
    echo "Free tier: 500 credits on signup"
    echo ""

    read -rsp "ScrapeGraphAI API key: " SGAI_API_KEY
    echo ""
    if [ -z "${SGAI_API_KEY}" ]; then
        echo "x API key cannot be empty."
        exit 1
    fi
    export SGAI_API_KEY

    # Determine script directory (works for both ./install.sh and curl|bash)
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # Check if running from the repo, from an installed Codex SEO suite, or standalone.
    if [ -f "${SCRIPT_DIR}/../../skills/seo-scrapegraph/SKILL.md" ]; then
        REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
        SKILL_SOURCE="${REPO_ROOT}/skills/seo-scrapegraph/SKILL.md"
        AGENT_SOURCE="${REPO_ROOT}/agents/seo-scrapegraph.toml"
    elif [ -f "${SCRIPT_DIR}/../../../seo-scrapegraph/SKILL.md" ]; then
        SKILL_SOURCE="$(cd "${SCRIPT_DIR}/../../../seo-scrapegraph" && pwd)/SKILL.md"
        AGENT_SOURCE="${AGENT_DIR}/seo-scrapegraph.toml"
    elif [ -f "${SCRIPT_DIR}/skills/seo-scrapegraph/SKILL.md" ]; then
        SKILL_SOURCE="${SCRIPT_DIR}/skills/seo-scrapegraph/SKILL.md"
        AGENT_SOURCE="${SCRIPT_DIR}/agents/seo-scrapegraph.toml"
    else
        echo "x Cannot find extension source files."
        echo "  Run this script from the codex-seo repo: ./extensions/scrapegraph/install.sh"
        exit 1
    fi

    # Install skill
    echo ""
    echo "-> Installing ScrapeGraphAI skill..."
    mkdir -p "${SKILL_DIR}"
    cp "${SKILL_SOURCE}" "${SKILL_DIR}/SKILL.md"

    echo "-> Installing ScrapeGraphAI agent..."
    mkdir -p "${AGENT_DIR}"
    if [ -f "${AGENT_SOURCE}" ] && [ "${AGENT_SOURCE}" != "${AGENT_DIR}/seo-scrapegraph.toml" ]; then
        cp "${AGENT_SOURCE}" "${AGENT_DIR}/seo-scrapegraph.toml"
    elif [ -f "${AGENT_DIR}/seo-scrapegraph.toml" ]; then
        echo "  v Codex TOML agent already installed"
    else
        echo "  Warning: Codex TOML agent not found; reinstall the core Codex SEO suite if delegation is unavailable."
    fi

    # Merge MCP config into settings.json
    echo "-> Configuring MCP server..."

    # The key travels through the environment, never through the script body, so a
    # key containing quotes or newlines cannot break out into executable Python.
    SETTINGS_FILE="${SETTINGS_FILE}" MCP_ENDPOINT="${MCP_ENDPOINT}" python3 -c "
import json, os

settings_path = os.environ['SETTINGS_FILE']
api_key = os.environ['SGAI_API_KEY']

# Read existing settings or create new
if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        settings = json.load(f)
else:
    settings = {}

# Ensure mcpServers key exists
if 'mcpServers' not in settings:
    settings['mcpServers'] = {}

# Add ScrapeGraphAI server config (hosted Streamable HTTP, header auth)
settings['mcpServers']['scrapegraph'] = {
    'url': os.environ['MCP_ENDPOINT'],
    'headers': {
        'X-API-Key': api_key
    }
}

# Write back
os.makedirs(os.path.dirname(settings_path), exist_ok=True)
with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=2)

print('  v MCP server configured in settings.json')
" || {
        echo "  Warning: Could not auto-configure MCP server."
        echo "  Add the scrapegraph server manually to ~/.codex/settings.json"
        echo "  See: extensions/scrapegraph/docs/SCRAPEGRAPH-SETUP.md"
    }

    echo ""
    echo "v ScrapeGraphAI extension installed successfully!"
    echo ""
    echo "Usage:"
    echo "  1. Restart Codex CLI"
    echo "  2. Run commands:"
    echo "     /seo scrapegraph crawl https://example.com"
    echo "     /seo scrapegraph map https://example.com"
    echo "     /seo scrapegraph scrape https://example.com/page"
    echo "     /seo scrapegraph extract https://example.com/page \"pull title and meta description\""
    echo "     /seo scrapegraph search \"query\" https://example.com"
    echo ""
    echo "Documentation: extensions/scrapegraph/README.md"
    echo "To uninstall: ./extensions/scrapegraph/uninstall.sh"
}

main "$@"
