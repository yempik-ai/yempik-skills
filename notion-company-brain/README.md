# notion-company-brain

Turn Notion into the **team layer of a file-first company brain**, with governance: files are the source of truth for strategy, Notion is where the team reads and works, an agent keeps them aligned through the official Notion MCP.

Timely, too: with Notion 3.6 (July 2026), Claude is one of the first **External Agents** you can assign work to inside Notion, and Notion MCP usage grew 10x in a month. More agents writing into shared workspaces means the governance problem this skill solves is about to hit everyone.

Born from a real client implementation (an Italian SME whose team lives in Notion). The connection took minutes; the rules are what made it safe. This skill is those rules, generalized.

**The 5 rules:**

1. No silent push: every write is draft + human confirmation.
2. Only consolidated content reaches Notion. Hypotheses stay in files.
3. One source of truth per data type: the CRM wins on pipeline, files win on strategy.
4. The agent never deletes anything. It can only propose.
5. Every write lands in an audit log, with source and date.

**Install:** copy the `notion-company-brain/` folder into your skills directory (Claude Code: `.claude/skills/`; Claude Cowork: Settings → Capabilities). Skills are an open standard: this also works with other agents that support the format (Codex, Cursor, Gemini CLI, and more).

**Works with:** [cowork-os](https://github.com/yempik-ai/cowork-os), our open-source file-first company brain. Guide (Italian): yempik.com/notion-come-company-brain

Built by [Yempik](https://www.yempik.com). Governance first, sync second.
