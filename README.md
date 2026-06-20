# Yempik Skills

Skill per agenti AI (Claude Code / Cowork) che usiamo in Yempik. Le condividiamo perché funzionano.

Una "skill" è un set di istruzioni — un file `SKILL.md` — che carichi nel tuo agente e ne cambia il comportamento su un certo tipo di task. Niente da installare a livello di sistema: è testo che l'agente legge **da solo** quando il task corrisponde.

## Skill disponibili

| Skill | A cosa serve |
|---|---|
| [`verification`](./verification/SKILL.md) | Obbliga l'agente a **dimostrare** che il codice funziona prima di dire "fatto": compila, test, browser, database, log, performance — e ti dice cosa **non** ha verificato. |
| [`screen-recap`](./screen-recap/SKILL.md) | A fine lavoro registra una **demo / test end-to-end** del risultato e consegna **recap breve + video** invece di un wall of text. *Solo Claude Code (macOS), via `screencapture`.* |

## Come si usa

1. Copia la cartella della skill (es. `verification/`) nella cartella delle skill del tuo setup Claude (in Claude Code: `.claude/skills/`).
2. L'agente attiva la skill da solo quando il task corrisponde (per `verification`: quando ha scritto o modificato codice e sta per dichiararlo finito).

Vuoi l'installazione one-click in Cowork? Possiamo impacchettare la cartella come file `.skill` da importare con "Save skill".

## Crescere nel tempo

Aggiungeremo altre skill, **una cartella per skill**. Ogni skill è self-contained: un solo `SKILL.md`, niente file penzolanti.

---

— Yempik
