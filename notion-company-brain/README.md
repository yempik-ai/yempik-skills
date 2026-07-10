# notion-company-brain

Turn Notion into the **team layer of a file-first company brain**, with governance: files are the source of truth for strategy, Notion is where the team reads and works, an agent keeps them aligned through the official Notion MCP.

Born from a real client implementation (an Italian SME whose team lives in Notion). The connection took minutes; the rules are what made it safe. This skill is those rules, generalized.

**The 5 rules:**

1. No silent push: every write is draft + human confirmation.
2. Only consolidated content reaches Notion. Hypotheses stay in files.
3. One source of truth per data type: the CRM wins on pipeline, files win on strategy.
4. The agent never deletes anything. It can only propose.
5. Every write lands in an audit log, with source and date.

**Install:** copy the `notion-company-brain/` folder into your skills directory (Claude Code: `.claude/skills/`; Claude Cowork: Settings → Capabilities).

**Works with:** [cowork-os](https://github.com/yempik-ai/cowork-os), our open-source file-first company brain. Guide (Italian): yempik.com/notion-come-company-brain

Built by [Yempik](https://www.yempik.com). Governance first, sync second.
