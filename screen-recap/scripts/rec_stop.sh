#!/usr/bin/env bash
# Screen Recap — ferma la registrazione schermo (macOS / Claude Code, "Modalità A").
# Legge lo stato scritto da rec_start.sh, ferma il processo in modo pulito e stampa il path finale.
set -euo pipefail

STATE_DIR="${TMPDIR:-/tmp}"
STATE_FILE="$STATE_DIR/claude_screen_recap.state"

if [ ! -f "$STATE_FILE" ]; then
  echo "Nessuna registrazione in corso (state file assente)." >&2
  exit 1
fi

REC_PID="$(sed -n '1p' "$STATE_FILE")"
OUT_FILE="$(sed -n '2p' "$STATE_FILE")"

if [ -n "${REC_PID:-}" ] && kill -0 "$REC_PID" 2>/dev/null; then
  # SIGINT = come premere ctrl-c: screencapture finalizza e chiude il file in modo corretto.
  kill -INT "$REC_PID" 2>/dev/null || true
  # Attendi la chiusura pulita (max ~10s).
  for _ in $(seq 1 50); do
    kill -0 "$REC_PID" 2>/dev/null || break
    sleep 0.2
  done
fi

rm -f "$STATE_FILE"

if [ ! -s "$OUT_FILE" ]; then
  echo "ERR: file di registrazione mancante o vuoto: $OUT_FILE" >&2
  echo "     Causa piu' probabile: permesso 'Registrazione schermo' non concesso all'app." >&2
  exit 4
fi

FINAL="$OUT_FILE"
# Se c'è ffmpeg, crea un .mp4 piu' leggero/portabile accanto al .mov.
if command -v ffmpeg >/dev/null 2>&1; then
  MP4="${OUT_FILE%.mov}.mp4"
  if ffmpeg -y -loglevel error -i "$OUT_FILE" -vcodec h264 -movflags +faststart "$MP4" 2>/dev/null; then
    FINAL="$MP4"
  fi
fi

echo "[REC] Registrazione fermata."
echo "      Video: $FINAL"
