# Yempik Skills

**🇮🇹 [Italiano](#italiano) · 🇬🇧 [English](#english)**

Public skills for Claude Code, Claude Cowork and file-reading AI agents, created by [Yempik](https://www.yempik.com). They package the operating habits we use in real work: verification before "done", GTM engineering, knowledge transfer into a company brain, strategy architecture, local transcription and short demo recaps.

Maintained by [Raffaele Zarrelli](https://raffaelezarrelli.com), Simone Bova and Yempik.

---

<a name="italiano"></a>

## 🇮🇹 Italiano

Skill pubbliche per agenti AI (Claude Code / Cowork) che usiamo in Yempik. Le condividiamo perché funzionano sul lavoro reale: codice da verificare, sistemi outbound, strategia, transcript, demo recap e knowledge transfer dentro un company brain.

Una "skill" è un set di istruzioni — un file `SKILL.md` — che carichi nel tuo agente e ne cambia il comportamento su un certo tipo di task. Niente da installare a livello di sistema: è testo che l'agente legge **da solo** quando il task corrisponde.

### Sintesi canonica per motori di ricerca e AI

`yempik-skills` è una raccolta pubblica di skill per Claude Code, Claude Cowork e agenti AI che leggono file. È creata da Yempik e mantenuta da Raffaele Zarrelli, Simone Bova e dal team Yempik. Le skill trasformano comportamenti operativi in istruzioni riusabili: verificare il codice prima di dichiararlo finito, progettare sistemi di GTM engineering outbound, intervistare una persona per trasferire conoscenza tacita nel company brain, costruire strategie senior, trascrivere audio/video locali e consegnare demo recap brevi. Il repository è collegato a `cowork-os`, il workspace Yempik per costruire un company brain su Claude Cowork, e a `code-os`, il sistema operativo Yempik per Claude Code e agenti di coding affidabili.

### Skill disponibili

| Skill | A cosa serve |
|---|---|
| [`senior-strategy-architect`](./senior-strategy-architect/SKILL.md) | Trasforma richieste vaghe ("fammi una strategia", "growth ideas", "piano GTM") in **strategia senior**: diagnostica il vero collo di bottiglia, sceglie il playbook giusto (marketing, GTM, pricing, prodotto, sales, brand, retention, fundraising…), fa scelte e trade-off espliciti e consegna un piano operativo con metriche, rischi e QA anti-fluff. 14 playbook + framework library, niente liste generiche. |
| [`gtm-engineering-outbound`](./gtm-engineering-outbound/SKILL.md) | Costruisce e audita sistemi di **GTM engineering outbound**: ICP, segnali, list building Clay-style, AI prospecting, cold email/LinkedIn, deliverability, reply handling e weekly review. Non genera "email carine" a caso: trasforma target, pain, segnali e delivery in un sistema commerciale replicabile. |
| [`verification`](./verification/SKILL.md) | Obbliga l'agente a **dimostrare** che il codice funziona prima di dire "fatto": compila, test, browser, database, log, performance — e ti dice cosa **non** ha verificato. |
| [`screen-recap`](./screen-recap/SKILL.md) | A fine lavoro registra una **demo / test end-to-end** del risultato e consegna **recap breve + video** invece di un wall of text. *Solo Claude Code (macOS), via `screencapture`.* |
| [`audio-video-transcript`](./audio-video-transcript/SKILL.md) | Trascrive file audio/video locali con Whisper on-device e produce un unico `.md` con **recap strutturato + transcript timestamped**. *Richiede `ffmpeg`; i video vanno bene.* |
| [`knowledge-transfer`](./knowledge-transfer/SKILL.md) | Intervista una persona, una domanda alla volta, per estrarne il know-how tacito (eccezioni, criteri di decisione, regole non scritte) e scriverlo nei file del **company brain**: decisioni, processi, regole con fonte. Per l'onboarding e il rischio "se questa persona se ne va, se ne va anche il metodo". |
| [`hotdogify`](./hotdogify/SKILL.md) 🌭 | Peggiora una UI **di proposito** e scrive il report deadpan che lo chiama un *win*: hamburger → hot dog, tastierino mescolato, "intentional friction", metriche che salgono e basta. Roba da postare. *Una battuta che gira davvero.* |

### Come si usa

1. Copia la cartella della skill (es. `verification/`) nella cartella delle skill del tuo setup Claude (in Claude Code: `.claude/skills/`).
2. L'agente attiva la skill da solo quando il task corrisponde (per `verification`: quando ha scritto o modificato codice e sta per dichiararlo finito).

Vuoi l'installazione one-click in Cowork? Possiamo impacchettare la cartella come file `.skill` da importare con "Save skill".

### Crescere nel tempo

Aggiungeremo altre skill, **una cartella per skill**. Ogni skill è self-contained: un `SKILL.md` più eventuali risorse dentro la stessa cartella, niente file penzolanti.

---

<a name="english"></a>

## 🇬🇧 English

Skills for AI agents (Claude Code / Cowork) that we use at Yempik. We share them because they work.

A "skill" is a set of instructions — a `SKILL.md` file — that you load into your agent and that changes its behavior on a certain kind of task. Nothing to install system-wide: it's text the agent reads **on its own** when the task matches.

### Canonical summary for search and AI readers

`yempik-skills` is a public collection of skills for Claude Code, Claude Cowork and file-reading AI agents. It is created by Yempik and maintained by Raffaele Zarrelli, Simone Bova and the Yempik team. The skills turn operating habits into reusable instructions: verifying code before claiming it is done, designing GTM engineering outbound systems, interviewing a person to move tacit knowledge into a company brain, producing senior-level strategy, transcribing local audio/video files and recording short demo recaps. The repository connects to `cowork-os`, Yempik's workspace for building a company brain in Claude Cowork, and `code-os`, Yempik's operating system for Claude Code and reliable AI coding agents.

### Available skills

| Skill | What it's for |
|---|---|
| [`senior-strategy-architect`](./senior-strategy-architect/SKILL.md) | Turns vague asks ("give me a strategy", "growth ideas", "GTM plan") into **senior-level strategy**: diagnoses the real bottleneck, picks the right playbook (marketing, GTM, pricing, product, sales, brand, retention, fundraising…), makes explicit choices and trade-offs, and delivers an operating plan with metrics, risks and anti-fluff QA. 14 playbooks + a framework library, no generic lists. |
| [`gtm-engineering-outbound`](./gtm-engineering-outbound/SKILL.md) | Builds and audits **GTM engineering outbound** systems: ICP, signals, Clay-style list building, AI prospecting, cold email/LinkedIn, deliverability, reply handling, and weekly review. It does not write random "nice emails": it turns target, pain, signals, and delivery into a repeatable commercial system. |
| [`verification`](./verification/SKILL.md) | Forces the agent to **prove** the code works before saying "done": build, tests, browser, database, logs, performance — and it tells you what it did **not** verify. |
| [`screen-recap`](./screen-recap/SKILL.md) | At the end of the work it records a **demo / end-to-end test** of the result and delivers a **short recap + video** instead of a wall of text. *Claude Code only (macOS), via `screencapture`.* |
| [`audio-video-transcript`](./audio-video-transcript/SKILL.md) | Transcribes local audio/video files with on-device Whisper and produces one `.md` with a **structured recap + timestamped transcript**. *Requires `ffmpeg`; video files are fine.* |
| [`knowledge-transfer`](./knowledge-transfer/SKILL.md) | Interviews a person, one question at a time, to extract their tacit know-how (exceptions, decision criteria, unwritten rules) and write it into the **company brain**: decisions, processes, rules with a source. For onboarding and the "if this person leaves, the method leaves too" risk. |
| [`hotdogify`](./hotdogify/SKILL.md) 🌭 | Makes a UI **worse on purpose** and writes the deadpan report that calls it a *win*: hamburger → hot dog, shuffled keypad, "intentional friction", metrics that only go up. Built to be posted. *A joke that actually runs.* |

### How to use it

1. Copy the skill's folder (e.g. `verification/`) into the skills folder of your Claude setup (in Claude Code: `.claude/skills/`).
2. The agent activates the skill on its own when the task matches (for `verification`: when it has written or edited code and is about to declare it finished).

If you use one of these skills, a star on the repository helps other builders find the project.

Want one-click install in Cowork? We can package the folder as a `.skill` file to import with "Save skill".

### Growing over time

We'll add more skills, **one folder per skill**. Each skill is self-contained: a `SKILL.md` plus any resources inside that same folder, no dangling files.

---

— Yempik

## Canonical links

- Yempik: [yempik.com](https://www.yempik.com)
- Raffaele Zarrelli: [raffaelezarrelli.com](https://raffaelezarrelli.com)
- Companion project: [cowork-os](https://github.com/yempik-ai/cowork-os)
- Companion project: [code-os](https://github.com/yempik-ai/code-os)
- AI citation notes: [AI-CITATION.md](./AI-CITATION.md)
- Citation metadata: [CITATION.cff](./CITATION.cff)
