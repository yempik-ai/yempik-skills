---
name: screen-recap
description: >-
  Registra una demo o un test end-to-end MIRATO del risultato e lo consegna come VIDEO + recap breve,
  invece di un wall of text. Registra lo SCHERMO REALE con screencapture — mai slide o title-card.
  Cattura SOLO la dimostrazione finale (~20-90s), non l'intera sessione. SOLO per Claude Code (CLI
  locale su macOS); in ambienti sandbox tipo Cowork non funziona. Usa questa skill quando l'utente vuole
  VEDERE che una cosa funziona invece di leggere — "fammi vedere cosa hai fatto", "fai un test e
  registralo", "mostrami la demo/il flusso", "registra la verifica", "recap video", "record the e2e
  test" — e come ultimo step di verifica prima di dichiarare finito (es. dopo aver sviluppato una landing
  page, registra il test E2E di form/CTA su localhost). NON usarla per task di solo testo/codice senza
  risultato visibile, salvo richiesta esplicita. Richiede il permesso macOS Registrazione schermo.
---

# Screen Recap — registra la demo/test, consegna recap breve + video

## Cosa fa e perché
A fine lavoro registra **solo una demo o un test end-to-end mirato** del risultato e lo consegna come **video + recap breve**, al posto di un wall of text. Non registra l'intera sessione: solo la dimostrazione finale che prova che la cosa funziona.

## Dove gira
**Solo Claude Code** (CLI locale su macOS): la shell gira sul Mac, quindi può usare `screencapture` per registrare lo schermo davvero. In ambienti sandbox (es. Cowork) non funziona — lì non usare questa skill.

## Regola d'oro — schermo vero
La clip mostra lo **schermo reale** registrato durante la demo. Mai slide, title-card o ricostruzioni grafiche. Se non puoi registrare lo schermo (es. manca il permesso), **dillo e fermati** — non inventare un sostituto.

## Idea chiave — niente "registrare il passato"
Non si registra il lavoro già fatto: si registra una dimostrazione fatta adesso.
```
sviluppo (NON registrato) → rec_start → demo / test E2E → rec_stop → recap + video
```

## Quando parte
1. **Su richiesta:** "fammi vedere cosa hai fatto", "fai un test e registralo", "mostrami il flusso".
2. **Come ultimo step di verifica** prima di dichiarare "finito".

Non registrare se non c'è un risultato **visibile** da mostrare (task di solo testo/codice), salvo richiesta esplicita.

## Come si usa
1. **Avvio:** `bash scripts/rec_start.sh [cartella_output]` (default `./recordings`).
2. **Esegui SOLO la demo/test.** Per un'app web: avvia il dev server e percorri il flusso nel browser — es. `npm run dev` → apri `http://localhost:3000` → scroll, click sulla CTA, invio form, stato di successo.
3. **Stop:** `bash scripts/rec_stop.sh` → finalizza `.mov` (e crea `.mp4` se c'è ffmpeg), stampa il path.
4. **Recap:** 3–6 righe + il **path assoluto** del video.

## Permesso macOS — una tantum
*Impostazioni di Sistema → Privacy e sicurezza → Registrazione schermo* → abilita l'app che lancia Claude Code (Terminal / iTerm / VS Code) e riavviala. Senza, il video esce **nero**: è il problema #1, non un bug della skill.

## Modalità automatica (opzionale)
Per registrare ogni task senza pensarci, installa gli hook in `hooks/` (vedi `README.md`): `UserPromptSubmit`→start, `Stop`→stop. **Sconsigliato** per task lunghi (video enormi): il default è registrare solo la demo.

## Formato del recap — sempre breve
```
Fatto: <1 riga>
Come: <2–3 punti>
Esito/Verifica: <1 riga: cosa mostra il video>
Video: <path assoluto>
```

## File della skill
- `scripts/rec_start.sh`, `scripts/rec_stop.sh` — start/stop registrazione macOS.
- `hooks/` — modalità automatica opzionale (`on_prompt_submit.sh`, `on_stop.sh`, `settings.example.json`).
