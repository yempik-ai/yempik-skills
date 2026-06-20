#!/usr/bin/env bash
# Claude Code hook — Stop: ferma la registrazione se ancora attiva (safety net).
# Idealmente la registrazione viene gia' fermata da Claude prima di scrivere il recap;
# questo hook chiude eventuali registrazioni rimaste aperte. Non blocca mai il turno.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$HERE/../scripts/rec_stop.sh" >/dev/null 2>&1 || true
exit 0
