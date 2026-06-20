#!/usr/bin/env bash
# Screen Recap — start the screen recording (macOS / Claude Code).
# Starts `screencapture` in the background and saves the state for rec_stop.sh.
# Usage: rec_start.sh [output_folder]
set -euo pipefail

STATE_DIR="${TMPDIR:-/tmp}"
STATE_FILE="$STATE_DIR/claude_screen_recap.state"

# Output folder: 1st argument, otherwise ./recordings in the cwd.
OUT_DIR="${1:-$PWD/recordings}"

# This script only works on macOS with screencapture (local CLI).
if [ "$(uname)" != "Darwin" ] || ! command -v screencapture >/dev/null 2>&1; then
  echo "ERR: needs macOS with 'screencapture' (local Claude Code)." >&2
  echo "     You seem to be in a Linux sandbox (e.g. Cowork): screen recording is not available here." >&2
  exit 3
fi

# If a recording is already live, don't start another one.
if [ -f "$STATE_FILE" ]; then
  OLD_PID="$(sed -n '1p' "$STATE_FILE" 2>/dev/null || true)"
  if [ -n "${OLD_PID:-}" ] && kill -0 "$OLD_PID" 2>/dev/null; then
    echo "Recording already in progress (PID $OLD_PID). File: $(sed -n '2p' "$STATE_FILE")"
    exit 0
  fi
fi

mkdir -p "$OUT_DIR"
TS="$(date +%Y%m%d_%H%M%S)"
OUT_FILE="$OUT_DIR/recap_$TS.mov"

# -v: record video  | -k: show clicks  | -x: don't play sounds.
# stdin from /dev/null so the background process doesn't stop waiting on TTY input.
# It stops with SIGINT (see rec_stop.sh), which is equivalent to pressing ctrl-c.
screencapture -v -k -x "$OUT_FILE" </dev/null &
REC_PID=$!

printf '%s\n%s\n' "$REC_PID" "$OUT_FILE" > "$STATE_FILE"

echo "[REC] Recording started (PID $REC_PID)"
echo "      File: $OUT_FILE"
echo "      Permission required: System Settings -> Privacy & Security -> Screen Recording"
echo "      (if the video comes out black, the permission is not enabled for the app that launches Claude Code)"
