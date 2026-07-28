# Changelog

All notable changes to the Yempik GTM Engineer skill are recorded here. Versions follow
[Semantic Versioning](https://semver.org/).

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
