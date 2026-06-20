#!/usr/bin/env bash
# Screen Recap — avvia la registrazione schermo (macOS / Claude Code, "Modalità A").
# Avvia `screencapture` in background e salva lo stato per rec_stop.sh.
# Uso: rec_start.sh [cartella_output]
set -euo pipefail

STATE_DIR="${TMPDIR:-/tmp}"
STATE_FILE="$STATE_DIR/claude_screen_recap.state"

# Cartella di output: 1° argomento, altrimenti ./recordings nella cwd.
OUT_DIR="${1:-$PWD/recordings}"

# Questo script funziona solo su macOS con screencapture (CLI locale).
if [ "$(uname)" != "Darwin" ] || ! command -v screencapture >/dev/null 2>&1; then
  echo "ERR: serve macOS con 'screencapture' (Modalità A / Claude Code locale)." >&2
  echo "     Sembri in Cowork (sandbox Linux): usa la Modalità B -> scripts/build_gif.sh." >&2
  exit 3
fi

# Se c'è già una registrazione viva, non avviarne un'altra.
if [ -f "$STATE_FILE" ]; then
  OLD_PID="$(sed -n '1p' "$STATE_FILE" 2>/dev/null || true)"
  if [ -n "${OLD_PID:-}" ] && kill -0 "$OLD_PID" 2>/dev/null; then
    echo "Registrazione gia' in corso (PID $OLD_PID). File: $(sed -n '2p' "$STATE_FILE")"
    exit 0
  fi
fi

mkdir -p "$OUT_DIR"
TS="$(date +%Y%m%d_%H%M%S)"
OUT_FILE="$OUT_DIR/recap_$TS.mov"

# -v: registra video  | -k: mostra i click  | -x: non riprodurre suoni.
# stdin da /dev/null per evitare che il processo in background si fermi sull'input del TTY.
# Si ferma con SIGINT (vedi rec_stop.sh), che equivale a premere ctrl-c.
screencapture -v -k -x "$OUT_FILE" </dev/null &
REC_PID=$!

printf '%s\n%s\n' "$REC_PID" "$OUT_FILE" > "$STATE_FILE"

echo "[REC] Registrazione avviata (PID $REC_PID)"
echo "      File: $OUT_FILE"
echo "      Permesso necessario: Impostazioni di Sistema -> Privacy e sicurezza -> Registrazione schermo"
echo "      (se il video risulta nero, il permesso non e' attivo per l'app che lancia Claude Code)"
