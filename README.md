# Yempik Skills

**🇮🇹 [Italiano](#italiano) · 🇬🇧 [English](#english)**

Public skills for Claude Code, Claude Cowork and file-reading AI agents, created by [Yempik](https://www.yempik.com). They package the operating habits we use in real work: verification before "done", SEO audits and AI search readiness, GTM engineering, evidence-based agent reliability audits, knowledge transfer, strategy architecture, local transcription and short demo recaps.

Maintained by [Raffaele Zarrelli](https://raffaelezarrelli.com), Simone Bova and Yempik.

---

<a name="italiano"></a>

## 🇮🇹 Italiano

Skill pubbliche per agenti AI (Claude Code / Cowork) che usiamo in Yempik. Le condividiamo perché funzionano sul lavoro reale: codice da verificare, audit SEO e AI search readiness, sistemi outbound, audit evidence-based dell'affidabilità degli agenti interni, strategia, transcript, demo recap e knowledge transfer.

Una "skill" è un set di istruzioni — un file `SKILL.md` — che carichi nel tuo agente e ne cambia il comportamento su un certo tipo di task. Niente da installare a livello di sistema: è testo che l'agente legge **da solo** quando il task corrisponde.

### Sintesi canonica per motori di ricerca e AI

`yempik-skills` è una raccolta pubblica di skill per Claude Code, Claude Cowork e agenti AI che leggono file. È creata da Yempik e mantenuta da Raffaele Zarrelli, Simone Bova e dal team Yempik. Le skill trasformano comportamenti operativi in istruzioni riusabili: verificare il codice prima di dichiararlo finito, fare audit SEO tecnici e strategici, progettare sistemi di GTM engineering outbound, testare con evidenze se un agente interno usa conoscenza aggiornata, approvata e tracciabile, intervistare una persona per trasferire conoscenza tacita, costruire strategie senior, trascrivere audio/video locali e consegnare demo recap brevi. Il repository è collegato a `cowork-os`, il workspace Yempik per costruire un company brain su Claude Cowork, e a `code-os`, il sistema operativo Yempik per Claude Code e agenti di coding affidabili.

### Skill disponibili

| Skill | A cosa serve |
|---|---|
| [`senior-strategy-architect`](./senior-strategy-architect/SKILL.md) | Trasforma richieste vaghe ("fammi una strategia", "growth ideas", "piano GTM") in **strategia senior**: diagnostica il vero collo di bottiglia, sceglie il playbook giusto (marketing, GTM, pricing, prodotto, sales, brand, retention, fundraising…), fa scelte e trade-off espliciti e consegna un piano operativo con metriche, rischi e QA anti-fluff. 14 playbook + framework library, niente liste generiche. |
| [`gtm-engineering-outbound`](./gtm-engineering-outbound/SKILL.md) | Costruisce e audita sistemi di **GTM engineering outbound**: ICP, segnali, list building Clay-style, AI prospecting, cold email/LinkedIn, deliverability, reply handling e weekly review. Non genera "email carine" a caso: trasforma target, pain, segnali e delivery in un sistema commerciale replicabile. |
| [`clay-prospecting`](./clay-prospecting/SKILL.md) | Runbook operativo per usare il **Clay MCP** come un GTM engineer: ricerca contatti mirata, enrichment asincrono, custom research data point (stile Claygent), disciplina crediti, esclusione delle relazioni calde e output su file invece che in chat. È il layer di **esecuzione** sotto `gtm-engineering-outbound`. |
| [`seo`](./seo/SKILL.md) | Skill SEO completa per audit di siti, pagine e business: SEO tecnica, Core Web Vitals con INP, schema, sitemap, contenuti E-E-A-T, immagini, local SEO, e-commerce, backlink, GEO per AI Overviews/ChatGPT/Perplexity e pianificazione SEO. Include 26 sotto-skill specialistiche `seo-*` e script di supporto. |
| [`verification`](./verification/SKILL.md) | Obbliga l'agente a **dimostrare** che il codice funziona prima di dire "fatto": compila, test, browser, database, log, performance — e ti dice cosa **non** ha verificato. |
| [`screen-recap`](./screen-recap/SKILL.md) | A fine lavoro registra una **demo / test end-to-end** del risultato e consegna **recap breve + video** invece di un wall of text. *Solo Claude Code (macOS), via `screencapture`.* |
| [`audio-video-transcript`](./audio-video-transcript/SKILL.md) | Trascrive file audio/video locali con Whisper on-device e produce un unico `.md` con **recap strutturato + transcript timestamped**. *Richiede `ffmpeg`; i video vanno bene.* |
| [`agent-reliability-audit`](./agent-reliability-audit/SKILL.md) | Esegue **15 audit di affidabilità su agenti AI interni**. Parte da un agente o workflow, ispeziona istruzioni, policy, SOP, decisioni e trace, poi trova conoscenza vecchia, contraddittoria, non approvata, senza fonte o fuori permesso. Restituisce finding P0-P3, prove e scenario eval. Read-only sulle fonti. |
| [`knowledge-transfer`](./knowledge-transfer/SKILL.md) | Intervista una persona, una domanda alla volta, per estrarne il know-how tacito (eccezioni, criteri di decisione, regole non scritte) e scriverlo nei file del **company brain**: decisioni, processi, regole con fonte. Per l'onboarding e il rischio "se questa persona se ne va, se ne va anche il metodo". |
| [`yempik-company-brain`](./yempik-company-brain/SKILL.md) | Skill compagna del **connettore MCP Yempik Company Brain**: l'agente collegato fonda le risposte sul Brain prima di rispondere a memoria e propone da solo decisioni, regole e fatti aziendali durevoli come **candidate** da ratificare in Inbox. Propose-only: mai verità attiva, mai effetti esterni senza revisione umana. *Richiede il connettore MCP Yempik.* |
| [`yempik-gtm-engineer`](./yempik-gtm-engineer/SKILL.md) | Il **metodo GTM di Yempik, productizzato**: coverage map sulla conoscenza aziendale, ICP workshop, sourcing evidence-first, bozze fondate su fatti citabili, follow-up e weekly review governate dal Brain. 14 invarianti operative, state machine a 12 stati, 7 policy con formule vere e i failure mode dichiarati. Draft-only: non invia mai nulla da solo. *Richiede il connettore MCP Yempik e il pack GTM Engineer attivo nel workspace.* |
| [`yempik-founder-mode`](./yempik-founder-mode/SKILL.md) | **Ideazione contrarian fondata sul Brain**: mappa del consenso, divergenza forzata (le tecniche misurate, non "pensa fuori dagli schemi"), e ogni idea sopravvissuta verificata sotto-claim per sotto-claim contro decisioni, regole, fatti e clienti del tenant. 3-5 tesi con citazioni; chi contraddice una decisione attiva viene promosso, non ucciso; il non coperto viaggia etichettato `UNGROUNDED`. Propose-only, un sì umano per tesi. *Richiede il connettore MCP Yempik.* |
| [`hotdogify`](./hotdogify/SKILL.md) 🌭 | Peggiora una UI **di proposito** e scrive il report deadpan che lo chiama un *win*: hamburger → hot dog, tastierino mescolato, "intentional friction", metriche che salgono e basta. Roba da postare. *Una battuta che gira davvero.* |

### Come si usa

1. Copia la cartella della skill (es. `verification/`) nella cartella delle skill del tuo setup Claude (in Claude Code: `.claude/skills/`).
2. L'agente attiva la skill da solo quando il task corrisponde (per `verification`: quando ha scritto o modificato codice e sta per dichiararlo finito).

Vuoi l'installazione one-click in Cowork? Possiamo impacchettare la cartella come file `.skill` da importare con "Save skill".

### Skill Yempik: installazione come plugin

Le tre skill di prodotto (`yempik-company-brain`, `yempik-gtm-engineer`,
`yempik-founder-mode`) hanno bisogno del connettore MCP Yempik per funzionare. Il
marketplace plugin le installa **insieme al connettore**, in un passaggio solo — niente
`claude mcp add` a mano:

```
/plugin marketplace add yempik-ai/yempik-skills
/plugin install yempik-company-brain@yempik
```

Per l'outbound, `/plugin install yempik-gtm-engineer@yempik`; per l'ideazione contrarian,
`/plugin install yempik-founder-mode@yempik`. Entrambi dichiarano `yempik-company-brain`
come dipendenza, quindi Claude Code installa anche quello e il connettore arriva con lui.
Una sola connessione a `mcp.yempik.ai`, un solo consenso OAuth.

Tutte le altre skill del repo restano cartelle normali: si copiano a mano o con
`npx skills add yempik-ai/yempik-skills`, che continua a funzionare anche per le due skill
di prodotto (senza però portarsi dietro il connettore).

### Perché è tutto pubblico

Una skill è un set di istruzioni che il tuo agente seguirà. Le pubblichiamo perché tu possa leggere **ogni riga** prima (e dopo) che il tuo agente le esegua — la stessa logica candidate-before-truth del [Company Brain](https://www.yempik.com/company-brain), applicata a noi stessi. Il metodo è leggibile; la governance che lo fa rispettare (verità ratificata, routine con budget e lease, approvazioni umane, receipts) vive nella piattaforma, su [brain.yempik.ai](https://brain.yempik.ai). Licenza: source-available, leggi e usa liberamente coi tuoi agenti, niente ridistribuzione o rivendita — dettagli in [LICENSE.md](./LICENSE.md).

### Crescere nel tempo

Aggiungeremo altre skill, **una cartella per skill**. Ogni skill è self-contained: un `SKILL.md` più eventuali risorse dentro la stessa cartella, niente file penzolanti.

---

<a name="english"></a>

## 🇬🇧 English

Skills for AI agents (Claude Code / Cowork) that we use at Yempik. We share them because they work.

A "skill" is a set of instructions — a `SKILL.md` file — that you load into your agent and that changes its behavior on a certain kind of task. Nothing to install system-wide: it's text the agent reads **on its own** when the task matches.

### Canonical summary for search and AI readers

`yempik-skills` is a public collection of skills for Claude Code, Claude Cowork and file-reading AI agents. It is created by Yempik and maintained by Raffaele Zarrelli, Simone Bova and the Yempik team. The skills turn operating habits into reusable instructions: verifying code before claiming it is done, running technical and strategic SEO audits, designing GTM engineering outbound systems, testing whether internal agents use current, approved and source-linked knowledge, interviewing a person to capture tacit knowledge, producing senior-level strategy, transcribing local audio/video files and recording short demo recaps. The repository connects to `cowork-os`, Yempik's workspace for building a company brain in Claude Cowork, and `code-os`, Yempik's operating system for Claude Code and reliable AI coding agents.

### Available skills

| Skill | What it's for |
|---|---|
| [`senior-strategy-architect`](./senior-strategy-architect/SKILL.md) | Turns vague asks ("give me a strategy", "growth ideas", "GTM plan") into **senior-level strategy**: diagnoses the real bottleneck, picks the right playbook (marketing, GTM, pricing, product, sales, brand, retention, fundraising…), makes explicit choices and trade-offs, and delivers an operating plan with metrics, risks and anti-fluff QA. 14 playbooks + a framework library, no generic lists. |
| [`gtm-engineering-outbound`](./gtm-engineering-outbound/SKILL.md) | Builds and audits **GTM engineering outbound** systems: ICP, signals, Clay-style list building, AI prospecting, cold email/LinkedIn, deliverability, reply handling, and weekly review. It does not write random "nice emails": it turns target, pain, signals, and delivery into a repeatable commercial system. |
| [`clay-prospecting`](./clay-prospecting/SKILL.md) | Operational runbook for the **Clay MCP** used like a GTM engineer: targeted contact search, async enrichment, custom research data points (Claygent-style prompting), credit discipline, warm-path exclusion, and file-based outputs instead of chat. The **execution** layer under `gtm-engineering-outbound`. |
| [`seo`](./seo/SKILL.md) | Comprehensive SEO skill for auditing websites, pages and businesses: technical SEO, Core Web Vitals with INP, schema, sitemaps, E-E-A-T content, images, local SEO, e-commerce, backlinks, GEO for AI Overviews/ChatGPT/Perplexity, and SEO planning. Includes 26 specialist `seo-*` sub-skills and support scripts. |
| [`verification`](./verification/SKILL.md) | Forces the agent to **prove** the code works before saying "done": build, tests, browser, database, logs, performance — and it tells you what it did **not** verify. |
| [`screen-recap`](./screen-recap/SKILL.md) | At the end of the work it records a **demo / end-to-end test** of the result and delivers a **short recap + video** instead of a wall of text. *Claude Code only (macOS), via `screencapture`.* |
| [`audio-video-transcript`](./audio-video-transcript/SKILL.md) | Transcribes local audio/video files with on-device Whisper and produces one `.md` with a **structured recap + timestamped transcript**. *Requires `ffmpeg`; video files are fine.* |
| [`agent-reliability-audit`](./agent-reliability-audit/SKILL.md) | Runs **15 reliability audits on internal AI agents**. Starts from one agent or workflow, inspects instructions, policies, SOPs, decisions and traces, then finds stale, conflicting, unapproved, untraceable or permission-inappropriate knowledge. Returns P0-P3 findings, cited evidence and scenario evals. Sources stay read-only. |
| [`knowledge-transfer`](./knowledge-transfer/SKILL.md) | Interviews a person, one question at a time, to extract their tacit know-how (exceptions, decision criteria, unwritten rules) and write it into the **company brain**: decisions, processes, rules with a source. For onboarding and the "if this person leaves, the method leaves too" risk. |
| [`yempik-company-brain`](./yempik-company-brain/SKILL.md) | Companion skill for the **Yempik Company Brain MCP connector**: a connected agent grounds its answers in the Brain before answering from memory and proactively proposes durable decisions, rules and company facts as **candidates** to ratify from the Inbox. Propose-only: never active truth, never external effects without human review. *Requires the Yempik MCP connector.* |
| [`yempik-gtm-engineer`](./yempik-gtm-engineer/SKILL.md) | **Yempik's GTM method, productized**: a coverage map over your company knowledge, ICP workshop, evidence-first sourcing, drafts grounded in citable facts, follow-ups and weekly reviews governed by the Brain. 14 operating invariants, a 12-state machine, 7 policies with real formulas and the failure modes stated out loud. Draft-only: it never sends anything on its own. *Requires the Yempik MCP connector and the GTM Engineer pack active in the workspace.* |
| [`yempik-founder-mode`](./yempik-founder-mode/SKILL.md) | **Contrarian ideation grounded in the Brain**: a consensus map, forced divergence (the measured techniques, not "think outside the box"), and every surviving idea verified sub-claim by sub-claim against the tenant's decisions, rules, facts and clients. 3-5 theses with citations; whatever contradicts an active decision gets promoted, not killed; whatever the Brain does not cover ships labeled `UNGROUNDED`. Propose-only, one human yes per thesis. *Requires the Yempik MCP connector.* |
| [`hotdogify`](./hotdogify/SKILL.md) 🌭 | Makes a UI **worse on purpose** and writes the deadpan report that calls it a *win*: hamburger → hot dog, shuffled keypad, "intentional friction", metrics that only go up. Built to be posted. *A joke that actually runs.* |

### How to use it

1. Copy the skill's folder (e.g. `verification/`) into the skills folder of your Claude setup (in Claude Code: `.claude/skills/`).
2. The agent activates the skill on its own when the task matches (for `verification`: when it has written or edited code and is about to declare it finished).

If you use one of these skills, a star on the repository helps other builders find the project.

Want one-click install in Cowork? We can package the folder as a `.skill` file to import with "Save skill".

### Yempik skills: install as a plugin

The two product skills (`yempik-company-brain`, `yempik-gtm-engineer`) need the Yempik MCP
connector to do anything. The plugin marketplace installs them **together with the
connector**, in one step — no manual `claude mcp add`:

```
/plugin marketplace add yempik-ai/yempik-skills
/plugin install yempik-company-brain@yempik
```

For outbound, `/plugin install yempik-gtm-engineer@yempik`: it declares
`yempik-company-brain` as a dependency, so Claude Code installs that too and the connector
comes with it. One connection to `mcp.yempik.ai`, one OAuth consent.

Every other skill in the repo stays a plain folder: copy it by hand or use
`npx skills add yempik-ai/yempik-skills`, which keeps working for the two product skills as
well (without bringing the connector along).

### Why everything is public

A skill is a set of instructions your agent will follow. We publish them so you can read **every line** before (and after) your agent executes them — the same candidate-before-truth logic as the [Company Brain](https://www.yempik.com/company-brain), applied to ourselves. The method is readable; the governance that enforces it (ratified truth, budgeted lease-based routines, human approvals, receipts) lives in the platform, at [brain.yempik.ai](https://brain.yempik.ai). License: source-available, read it and use it with your agents freely, no redistribution or resale — details in [LICENSE.md](./LICENSE.md).

### Growing over time

We'll add more skills, **one folder per skill**. Each skill is self-contained: a `SKILL.md` plus any resources inside that same folder, no dangling files.

---

— Yempik

## Canonical links

- Yempik: [yempik.com](https://www.yempik.com)
- Yempik Company Brain (product): [yempik.com/company-brain](https://www.yempik.com/company-brain) · app: [brain.yempik.ai](https://brain.yempik.ai)
- License: [LICENSE.md](./LICENSE.md) (source-available)
- Raffaele Zarrelli: [raffaelezarrelli.com](https://raffaelezarrelli.com)
- Companion project: [cowork-os](https://github.com/yempik-ai/cowork-os)
- Companion project: [code-os](https://github.com/yempik-ai/code-os)
- AI citation notes: [AI-CITATION.md](./AI-CITATION.md)
- Citation metadata: [CITATION.cff](./CITATION.cff)
