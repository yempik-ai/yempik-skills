#!/usr/bin/env bash
# Screen Recap — stop the screen recording (macOS / Claude Code).
# Reads the state written by rec_start.sh, stops the process cleanly and prints the final path.
set -euo pipefail

STATE_DIR="${TMPDIR:-/tmp}"
STATE_FILE="$STATE_DIR/claude_screen_recap.state"

if [ ! -f "$STATE_FILE" ]; then
  echo "No recording in progress (state file missing)." >&2
  exit 1
fi

REC_PID="$(sed -n '1p' "$STATE_FILE")"
OUT_FILE="$(sed -n '2p' "$STATE_FILE")"

if [ -n "${REC_PID:-}" ] && kill -0 "$REC_PID" 2>/dev/null; then
  # SIGINT = like pressing ctrl-c: screencapture finalizes and closes the file correctly.
  kill -INT "$REC_PID" 2>/dev/null || true
  # Wait for a clean shutdown (max ~10s).
  for _ in $(seq 1 50); do
    kill -0 "$REC_PID" 2>/dev/null || break
    sleep 0.2
  done
fi

rm -f "$STATE_FILE"

if [ ! -s "$OUT_FILE" ]; then
  echo "ERR: recording file missing or empty: $OUT_FILE" >&2
  echo "     Most likely cause: 'Screen Recording' permission not granted to the app." >&2
  exit 4
fi

FINAL="$OUT_FILE"
# If ffmpeg is present, create a lighter/more portable .mp4 next to the .mov.
if command -v ffmpeg >/dev/null 2>&1; then
  MP4="${OUT_FILE%.mov}.mp4"
  if ffmpeg -y -loglevel error -i "$OUT_FILE" -vcodec h264 -movflags +faststart "$MP4" 2>/dev/null; then
    FINAL="$MP4"
  fi
fi

echo "[REC] Recording stopped."
echo "      Video: $FINAL"
