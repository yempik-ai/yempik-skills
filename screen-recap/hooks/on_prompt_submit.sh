#!/usr/bin/env bash
# Claude Code hook — UserPromptSubmit: avvia la registrazione schermo.
# Non deve MAI bloccare il turno: in caso di qualsiasi errore esce 0.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Avvia solo su macOS con screencapture (Modalità A). Altrove non fa nulla.
if [ "$(uname)" = "Darwin" ] && command -v screencapture >/dev/null 2>&1; then
  bash "$HERE/../scripts/rec_start.sh" >/dev/null 2>&1 || true
fi
exit 0
