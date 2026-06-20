#!/usr/bin/env bash
# Claude Code hook — Stop: stop the recording if still active (safety net).
# Ideally the recording is already stopped by Claude before writing the recap;
# this hook closes any recordings left open. It never blocks the turn.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$HERE/../scripts/rec_stop.sh" >/dev/null 2>&1 || true
exit 0
