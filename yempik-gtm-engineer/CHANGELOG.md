# Changelog

All notable changes to the Yempik GTM Engineer skill are recorded here. Versions follow
[Semantic Versioning](https://semver.org/).

## 1.0.1 (2026-07-29)

Documentation only. No contract, policy or artefact shape changed.

- `SKILL.md`, "Before the first run": a stale-schema degradation note. A connector session
  opened before the current server deploy keeps the tool schema it cached, so
  `brain_resolve_question` can be missing the `recipe` parameter entirely. The note says to
  read that as a stale connector, ask for a refresh or reconnect, and never substitute a
  `product_strategy` coverage result for `gtm_readiness`, whose domains are the only ones
  that answer the three ratification gates.
- Server-side, with no effect on the pack: the routine tool descriptions now derive their
  supported-kind enumeration from the contract registry instead of naming one kind, so a
  client reading only the schema no longer sees a list that predates `gtm_followup_engine`
  and `gtm_weekly_review`.
- Compatible with routine contracts `gtm-followup-engine-v1` and `gtm-weekly-review-v1`, and
  with agent pack `gtm_engineer` version 1.0.1.

## 1.0.0 (2026-07-28)

Initial productization from the internal reference motion.

- `SKILL.md`: motion profile and non-goals, the setup gate (ICP plus exclusions, approved
  claims, send authorisation) checked through the `gtm_readiness` coverage recipe, the
  loading order, the 14 doctrine invariants, the permission boundary (`draft` and `write`
  yes, `send` and `delete` never), the two grounding channels, the routine flow, the
  rationalizations table, the red flags and the quick reference.
- `references/`: the translated kernel. Doctrine, configuration contract, policies 01 to 07,
  routines, connectors, permissions, failure modes, anti-patterns, open hypotheses, language
  adapters (`it`, `en`), market template, schemas and the state machine.
- `agents/`: two subagent cards, `account-researcher` (per-account signal and email discovery)
  and `reply-classifier` (the closed 8-class reply taxonomy).
- `assets/clay/`: site-scan prompt, scoring formula and the universe and suppression table
  templates.
- Compatible with routine contracts `gtm-followup-engine-v1` and `gtm-weekly-review-v1`, and
  with agent pack `gtm_engineer` version 1.0.0.

All company values were extracted into named configuration slots, all real entities were
anonymised, and the four hypotheses that read like rules ship with their counter-evidence
attached rather than as rules.
