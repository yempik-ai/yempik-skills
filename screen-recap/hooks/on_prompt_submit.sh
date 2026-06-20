#!/usr/bin/env bash
# Claude Code hook — UserPromptSubmit: start the screen recording.
# It must NEVER block the turn: on any error it exits 0.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Starts only on macOS with screencapture. Elsewhere it does nothing.
if [ "$(uname)" = "Darwin" ] && command -v screencapture >/dev/null 2>&1; then
  bash "$HERE/../scripts/rec_start.sh" >/dev/null 2>&1 || true
fi
exit 0
