# Yempik Skills

**🇮🇹 [Italiano](#italiano) · 🇬🇧 [English](#english)**

---

<a name="italiano"></a>

## 🇮🇹 Italiano

Skill per agenti AI (Claude Code / Cowork) che usiamo in Yempik. Le condividiamo perché funzionano.

Una "skill" è un set di istruzioni — un file `SKILL.md` — che carichi nel tuo agente e ne cambia il comportamento su un certo tipo di task. Niente da installare a livello di sistema: è testo che l'agente legge **da solo** quando il task corrisponde.

### Skill disponibili

| Skill | A cosa serve |
|---|---|
| [`verification`](./verification/SKILL.md) | Obbliga l'agente a **dimostrare** che il codice funziona prima di dire "fatto": compila, test, browser, database, log, performance — e ti dice cosa **non** ha verificato. |
| [`screen-recap`](./screen-recap/SKILL.md) | A fine lavoro registra una **demo / test end-to-end** del risultato e consegna **recap breve + video** invece di un wall of text. *Solo Claude Code (macOS), via `screencapture`.* |

### Come si usa

1. Copia la cartella della skill (es. `verification/`) nella cartella delle skill del tuo setup Claude (in Claude Code: `.claude/skills/`).
2. L'agente attiva la skill da solo quando il task corrisponde (per `verification`: quando ha scritto o modificato codice e sta per dichiararlo finito).

Vuoi l'installazione one-click in Cowork? Possiamo impacchettare la cartella come file `.skill` da importare con "Save skill".

### Crescere nel tempo

Aggiungeremo altre skill, **una cartella per skill**. Ogni skill è self-contained: un solo `SKILL.md`, niente file penzolanti.

---

<a name="english"></a>

## 🇬🇧 English

Skills for AI agents (Claude Code / Cowork) that we use at Yempik. We share them because they work.

A "skill" is a set of instructions — a `SKILL.md` file — that you load into your agent and that changes its behavior on a certain kind of task. Nothing to install system-wide: it's text the agent reads **on its own** when the task matches.

### Available skills

| Skill | What it's for |
|---|---|
| [`verification`](./verification/SKILL.md) | Forces the agent to **prove** the code works before saying "done": build, tests, browser, database, logs, performance — and it tells you what it did **not** verify. |
| [`screen-recap`](./screen-recap/SKILL.md) | At the end of the work it records a **demo / end-to-end test** of the result and delivers a **short recap + video** instead of a wall of text. *Claude Code only (macOS), via `screencapture`.* |

### How to use it

1. Copy the skill's folder (e.g. `verification/`) into the skills folder of your Claude setup (in Claude Code: `.claude/skills/`).
2. The agent activates the skill on its own when the task matches (for `verification`: when it has written or edited code and is about to declare it finished).

Want one-click install in Cowork? We can package the folder as a `.skill` file to import with "Save skill".

### Growing over time

We'll add more skills, **one folder per skill**. Each skill is self-contained: a single `SKILL.md`, no dangling files.

---

— Yempik
