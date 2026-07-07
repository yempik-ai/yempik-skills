# Senior Strategy Architect Skill

A custom Claude Skill for producing senior-level strategies across marketing, go-to-market,
business, growth, product, brand, sales, pricing, content, retention, fundraising, competitive,
marketplace, partnership, and community contexts.

## What it does

The skill gives Claude a repeatable strategy operating system:

- route the user's vague request to the right strategic domain;
- ask only high-leverage questions when context is missing;
- diagnose the true bottleneck before prescribing tactics;
- select useful frameworks without turning the answer into theory;
- force explicit choices, trade-offs, metrics, and next actions;
- block generic advice and rewrite weak outputs before finalizing.

## How to install

For Claude.ai, upload this skill as a zip file through the product's custom Skills settings.
For Claude Code, place the `senior-strategy-architect` directory wherever your Claude Code custom
skills are discovered in your environment.

## Design notes

- `SKILL.md` is intentionally compact so it can be loaded quickly.
- Detailed content lives in `references/` and `playbooks/`, which Claude should read only when useful.
- The package includes eval prompts under `evals/` to test whether the skill triggers and improves output.
- The skill is written in English for broad model compatibility, but it instructs Claude to reply in the user's language.

## Safety and accuracy

This skill does not fetch external data on its own. If a strategy depends on current market facts,
competitor pricing, platform rules, legal/regulatory context, or live trends, Claude should use available
research tools or clearly state what is assumed.
