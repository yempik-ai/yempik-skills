# screen-recap (Claude Code)

Skill che, a fine lavoro, registra **solo una demo / test end-to-end del risultato** e restituisce un **recap breve + il video**, invece di un wall of text.

**Solo per Claude Code** (CLI locale su macOS): la shell gira sul Mac, quindi `screencapture` registra lo schermo davvero. In ambienti sandbox (Cowork) non funziona — la versione Cowork è stata rimossa di proposito.

## Idea
Non si registra il lavoro già fatto: si registra una **dimostrazione fatta adesso**, mirata, ~20–90 secondi.
```
sviluppo (NON registrato) → rec_start → demo/test E2E → rec_stop → recap + video
```

## Struttura
```
screen-recap/
├── SKILL.md                  # istruzioni per Claude (le legge da sola)
├── README.md                 # questo file
├── scripts/
│   ├── rec_start.sh          # avvia la registrazione (screencapture in background)
│   └── rec_stop.sh           # ferma e finalizza .mov/.mp4
└── hooks/                    # OPZIONALE: full-session automatico
    ├── on_prompt_submit.sh
    ├── on_stop.sh
    └── settings.example.json
```

## Prerequisito macOS — una tantum
*Impostazioni di Sistema → Privacy e sicurezza → Registrazione schermo* → abilita **Terminal** (o iTerm / VS Code) e riavvia l'app.
Senza, `screencapture` produce un video **nero**: è il problema #1, non un bug.

## Uso (default = solo la demo)
1. `bash scripts/rec_start.sh` — avvia (output in `./recordings`).
2. Esegui **solo** la demo/test. Per un sito: `npm run dev` → percorri il flusso su `http://localhost:3000`.
3. `bash scripts/rec_stop.sh` — stop, stampa il path del video.
4. Recap di 3–6 righe + path.

## Alternativa avanzata — full-session automatico (sconsigliato)
Per registrare l'intero task in automatico, aggancia gli hook:
1. In `hooks/settings.example.json` sostituisci `/ABSOLUTE/PATH/screen-recap` col path reale.
2. Incolla il blocco `hooks` in `~/.claude/settings.json` o `<progetto>/.claude/settings.json`.
3. `UserPromptSubmit` avvia, `Stop` ferma.

Sconsigliato perché i task lunghi producono video enormi e illeggibili. Il modello di default (solo la demo) è quasi sempre quello giusto.

## Limiti noti
- Niente Cowork (sandbox Linux, niente `screencapture`).
- Mac gestito da MDM: il permesso Registrazione schermo va sbloccato dall'IT.
- Task di solo codice senza output visibile: niente da mostrare → di default salta il video.
- Stop via `SIGINT`: è il modo corretto per far finalizzare il file a `screencapture`. Da verificare sul tuo Mac al primo giro reale.
