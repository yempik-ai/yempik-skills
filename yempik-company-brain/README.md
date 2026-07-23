# yempik-company-brain

**🇮🇹** Skill compagna del connettore MCP **Yempik Company Brain** ([brain.yempik.ai](https://brain.yempik.ai)).
Quando il connettore è collegato, l'agente con questa skill: fonda le risposte sul Brain
prima di rispondere a memoria (*ground-first*) e propone da solo la conoscenza aziendale
durevole — decisioni confermate, regole, cambi di pricing, fatti cliente — come **candidate**
in attesa di revisione umana (*capture proactively*). È sicura per costruzione: proporre non
attiva mai verità e non ha effetti esterni; un umano ratifica o rifiuta dalla Inbox.

**🇬🇧** Companion skill for the **Yempik Company Brain** MCP connector
([brain.yempik.ai](https://brain.yempik.ai)). With the connector attached, an agent running
this skill grounds its answers in the Brain before answering from memory (*ground-first*)
and proactively proposes durable company knowledge — confirmed decisions, rules, pricing
changes, client facts — as **candidates** pending human review (*capture proactively*).
Safe by construction: proposing never activates truth and has no external effects; a human
ratifies or rejects from the Inbox.

## Install

```bash
npx skills add yempik-ai/yempik-skills
```

Or copy this folder into your agent's skills directory (Claude Code: `.claude/skills/`).

**Requires:** the Yempik MCP connector connected and authorized
(`claude mcp add --transport http yempik https://mcp.yempik.ai/mcp`) with at least the
`brain:read` and `brain:propose` scopes.
