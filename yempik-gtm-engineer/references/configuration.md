# Configuration contract

Every value in this skill that changes between one company and the next lives here as a
named slot. Nothing else in the skill hard-codes a company value: the doctrine, the
policies and the routines refer to slots by name and quote the reference default in
parentheses.

The reference defaults come from a founder-led outbound motion in a vertical B2B micro-enterprise
market: low volume, high touch, email primary, human send authority, 26 accounts contacted over
two weeks. They are **evidence from one motion**, not benchmarks. Where a default was formalised
rather than observed it is marked `[INFERENCE]`, and an installer must re-derive it.

## How to read the tables

| Column | Meaning |
|---|---|
| Slot | The exact name to use when a policy or routine references the value. Do not coin variants. |
| Type | The shape of the value. |
| Reference default | What the reference motion used. |
| Consumed by | The files that read this slot. If you change the slot name, these files break. |

Three slots are **hard gates**: `icp_definition`, `approved_claims` and `writing_rules` must be
ratified by a human before the first run. An agent that writes copy without ratified claims
produces statements the company never authorised. See `setup-and-intake.md`.

---

## 1. Cadence and caps

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `max_first_touches_per_day` | integer | `3` | `doctrine.md` (D3) · `routines/followup-engine.md` (step 6) · `state-machine.yaml` (`outreach.caps`) |
| `touch_cap_per_account` | integer | `2` | `doctrine.md` (D2) · `policies/01-account-selection.md` · `policies/04-message-craft.md` · `state-machine.yaml` (global forbidden transitions) · `schemas/account.schema.json` (`touch_count_email.maximum`) |
| `followup_window_days` | integer or range | `4-5` `[INFERENCE]` (median of observed intervals, never a written rule) | `doctrine.md` (E3) · `policies/04-message-craft.md` · `routines/followup-engine.md` (step 5) |
| `followup_count` | integer | `1` (a single follow-up, then the email channel is closed) | `doctrine.md` (E3) · `policies/04-message-craft.md` |
| `scale_first_touches_per_day` | integer | `5`: the only thing `SCALE` is allowed to change | `policies/06-pipeline-and-decisions.md` |
| `reply_response_target` | duration | `1 working hour` for a reply expressing interest | `policies/05-reply-handling.md` · `routines/followup-engine.md` |
| `reactivation_stale_after_days` | integer | `30`: a deferral date more than this far in the past is escalated, not auto-reactivated | `routines/followup-engine.md (reactivation section)` |

## 2. Authority and permissions

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `send_authority` | enum `human_only` \| `agent_allowed` | `human_only`. The agent never sends, never accepts invitations, never publishes. | `doctrine.md` (D1) · `permissions.md` · `state-machine.yaml` · `red-lines.md` |
| `list_approval_required` | boolean | `true`: the shortlist is approved before the first touch | `state-machine.yaml` (`scoring.human_approval`) · `routines/universe-sourcing.md` (step 6 gate) · `schemas/experiment.schema.json` (`approved_by_founder`) |
| `enrichment_spend_approval` | enum `none` \| `notify` \| `required` | `required`: enrichment costs money and can violate the zero rule | `permissions.md` · `routines/universe-sourcing.md` |
| `escalation_owner` | role | the founder. Channel escalation (email → phone) is never the agent's decision. | `doctrine.md` (D2) · `policies/04-message-craft.md` · `red-lines.md` |
| `first_week_read_only` | boolean | `true`: run the daily routine read-only for one week before enabling drafts | `setup-and-intake.md` |

## 3. Language and register

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `customer_language` | locale | `it` (the reference motion); the skill ships `it` and `en` | `languages/it.md` · `languages/en.md` · `languages/it-exemplars.md` |
| `register` | free text | Formal, professional, dry. In the reference motion, the Italian formal address. | `languages/it.md` · `doctrine.md` (P1 slot) |
| `recovery_register` | free text | Warmer and colloquial in recovery messages after a no-show or a missed slot | `languages/it.md` · `doctrine.md` (P1 slot) · `policies/05-reply-handling.md` |
| `banned_tokens` | list | Language-specific. Reference motion (Italian): the em-dash, plus English loanwords toward the customer. Allowed exceptions were declared explicitly. | `languages/it.md` · `languages/en.md` · `anti-patterns.md` · `schemas/message.schema.json` (`compliance_checks`) |
| `allowed_exceptions` | list | Loanwords the founder already uses in their own writing, declared one by one | `languages/it.md` |
| `cta_wording` | free text | "a 25-minute call": an odd, specific number read as a measured request. **Never A/B tested.** | `policies/04-message-craft.md` · `doctrine.md` (P2 slot) |
| `cta_count_per_message` | integer | `1`: a hard constraint, not a preference. Universal, listed here only because the wording is not. | `doctrine.md` (D5) · `policies/04-message-craft.md` · `schemas/message.schema.json` |
| `subject_format` | template | `<product> × <account>: <promise>`: constant format, names the account and the promise. **Never A/B tested.** | `policies/04-message-craft.md` · `doctrine.md` (P3 slot) |
| `product_name` | string | The product being sold. Appears in the subject format and at the first product mention. | `policies/04-message-craft.md` · `languages/it-exemplars.md` |
| `tracked_link_policy` | template | A tracked product link at the first mention of the product, with the account domain as the per-account tracking value | `doctrine.md` (D5) · `schemas/message.schema.json` (`utm_content`) |

## 4. Targeting and segmentation

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `icp_definition` | ratified document | **Hard gate.** No default. Must exist and be human-ratified before install. | `setup-and-intake.md` · `state-machine.yaml` (`setup.exit`) · `policies/01-account-selection.md` |
| `exclusion_rules` | ratified list | **Hard gate.** Who is explicitly out. The reference motion's five permanent categories: warm relationship, special case, explicit refusal, dead channel, dated deferral. | `policies/01-account-selection.md` · `schemas/account.schema.json` (`exclusion_reason`) |
| `segment_definitions` | ordered list | Four ordered segments in the reference motion: centralised enterprise operators; networks and franchises; structured regional operators; adjacent ecosystem. Ordered, because the order is the work sequence. | `markets/_template.md` · `state-machine.yaml` (`segmentazione`) · `schemas/account.schema.json` (`segment_id`) |
| `warm_relationship_map` | list | **Must be populated before the first run**, not after. Anyone the founder sees in person, first-degree connections, active customers. | `doctrine.md` (D4) · `policies/01-account-selection.md` · `setup-and-intake.md` |
| `special_cases` | list | Accounts that never enter the automatic queue and are handled by hand | `policies/01-account-selection.md` |
| `approved_claims` | ratified list | **Hard gate.** What the agent may assert. Paired with a forbidden-claims list. | `setup-and-intake.md` · `anti-patterns.md` · `schemas/message.schema.json` (`claims_approved`) |
| `geography` | list | The sourcing territory. Two regions in the reference motion. | `routines/universe-sourcing.md` |

## 5. Signals, angles and scoring

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `angle_set` | closed enum | Four angles, closed: continuity across offices · replace the ecosystem · workflow ownership · published method. **Closed is the point:** four angles over 26 accounts still allows learning; 26 angles allows none. | `doctrine.md` (E2) · `policies/03-stakeholder-and-angle.md` · `markets/_template.md` · `schemas/account.schema.json` (`angle_id`) |
| `signal_types` | closed enum | published method · multiple offices · named incumbent system · declared volume · customer portal · existing engagement · verbalised pain | `policies/03-stakeholder-and-angle.md` · `schemas/account.schema.json` (`signal.type`) |
| `signal_to_angle_map` | mapping | Deterministic. Where signals coexist, the one most specific to the account wins. | `doctrine.md` (E2) · `policies/03-stakeholder-and-angle.md` · `markets/_template.md` |
| `scoring_weights` | weighted dimensions | Six dimensions, **non-uniform**, total 0-12: scale and complexity `0-2` · centralisation `0-2` · evidence of an existing system `0-2` · **pilotability `0-3`** · decision access `0-2` · change signal `0-1` | `policies/02-scoring.md` · `assets/clay/scoring-formula.md` · `schemas/account.schema.json` (`score_breakdown`) |
| `scoring_proxies` | list | Market-specific and the most expensive thing to regenerate. The reference market's seven observable proxies were re-derived after a spot-check found 0 of 20 sites declared portfolio size. | `markets/_template.md` · `policies/02-scoring.md` |
| `priority_bands` | banded thresholds | `9-12 → A` · `7-8 → B` · `5-6 → C` (only with a strong dynamic signal) · `<5 → not now` | `policies/02-scoring.md` · `schemas/account.schema.json` (`priority_band`) |
| `further_research_threshold` | integer | `7`: below this score, no spend on identifying the buying group | `policies/02-scoring.md` · `routines/universe-sourcing.md` (step 5) · `routines/universe-sourcing.md (step 5)` |
| `spot_check_sample_size` | integer | `20` sites, checked before scoring the whole universe | `policies/02-scoring.md` · `markets/_template.md` |
| `stakeholder_preference_order` | ordered list | named contact with a relevant operational role → relevant department mailbox → generic mailbox → certified mail → web form (not contactable). Treat the order as weak evidence: a monitored department mailbox beat an absent named contact. | `policies/03-stakeholder-and-angle.md` · `schemas/stakeholder.schema.json` |

## 6. Review thresholds and stop rules

All four thresholds below are marked `[INFERENCE]` in policy 06: they are a reasonable
formalisation of decisions that were actually taken by judgement. They were **not** in use
during the reference period. Treat them as starting points to calibrate, not as findings.

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `decision_window_accounts` | integer | `20` contacted accounts, rolling | `policies/06-pipeline-and-decisions.md` · `routines/weekly-review.md` |
| `reply_rate_floor` | ratio | `0.05` `[INFERENCE]`: below this, iterate on the list and the first line | `policies/06-pipeline-and-decisions.md` · `routines/weekly-review.md` |
| `positive_rate_floor` | ratio | `0.10` `[INFERENCE]`: at or above this with a meeting rate under 0.05, iterate on the CTA and reply handling | `policies/06-pipeline-and-decisions.md` · `routines/weekly-review.md` |
| `meeting_rate_scale` | ratio | `0.10` `[INFERENCE]`: at or above this, with calls that qualify, scale | `policies/06-pipeline-and-decisions.md` · `routines/weekly-review.md` |
| `meeting_rate_floor` | ratio | `0.05` `[INFERENCE]`: with a healthy positive rate, a meeting rate below this means iterate on the CTA, not on the list | `policies/06-pipeline-and-decisions.md` |
| `icp_review_reply_rate` | ratio | `0.15` `[INFERENCE]`: a high reply rate with calls that do not qualify means iterate on the ICP, not on the copy | `policies/06-pipeline-and-decisions.md` |
| `stop_rule_conversations` | integer | `10` qualified conversations without convergence on a payable workflow → stop and revisit the wedge. This one **was** written by the founder before the campaign; it is the only threshold in this section that is not an inference. | `policies/06-pipeline-and-decisions.md` · `routines/weekly-review.md` (step 5) |
| `min_sample_size_for_rule` | integer | `5` (platform contract default, range 1-30). The floor below which a learning candidate is not proposed as a rule; a single case never becomes a rule. Distinct from the statistical caveat: below a sample of `30`, `Experiment.statistical_caveat` stays mandatory regardless of this slot. | `schemas/experiment.schema.json` · `schemas/learning-delta-template.md` · `open-hypotheses.md` · `routines/weekly-review.md` |
| `variables_changed_per_week` | integer | `1`. Exactly one. At these volumes there is no statistical power for parallel tests. | `routines/weekly-review.md` (step 4) |
| `bottleneck_focus_per_week` | integer | `1`. Work the highest stage in the funnel that is losing more than its expected rate. | `policies/06-pipeline-and-decisions.md` |

## 7. Qualification and discovery

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `qualification_criteria` | list | Seven criteria that turn declared interest into evidence: an available real unit, a named operational owner, an observable workflow, exportable data, a named approver, budget or process, a baseline metric. | `routines/call-review.md` · `routines/discovery-call-prep.md` · `setup-and-intake.md` |
| `mandatory_discovery_questions` | ordered list | Market-specific. Re-derive per market from the operational process being sold into. | `routines/discovery-call-prep.md` · `markets/_template.md` |
| `first_purchase_scope` | free text | Deliberately small. In the reference motion: one real unit, one workflow, running in parallel with the existing system. This slot is what doctrine E8 tests an objection against. | `doctrine.md` (E8) · `policies/07-reason-codes.md` · `routines/call-review.md` |
| `opportunity_stage_ladder` | ordered enum | `call_held` → `pilot_verbal` → `pilot_signed` → `invoiced`. No skipping; each step needs a dated, verifiable event. | `doctrine.md` (D7) · `policies/06-pipeline-and-decisions.md` · `state-machine.yaml` (`opportunity`) |

## 8. Systems of record

| Slot | Type | Reference default | Consumed by |
|---|---|---|---|
| `evidence_of_record` | connector | The email connector. It is the truth about replies; files are a dated snapshot. | `doctrine.md` (D8) · `connectors.md` · `routines/followup-engine.md` (step 2) |
| `crm_system` | connector or `none` | A CRM connector. Optional: without it, the pipeline file becomes the only record and that must be declared. | `connectors.md` · `permissions.md` |
| `calendar_system` | connector or `none` | A calendar connector, read plus slot proposal. Never invitation send. | `connectors.md` · `permissions.md` |
| `enrichment_platform` | connector or `none` | Optional. Channel rule: up to ~20 rows use the conversational connector; above that use the platform with tables. | `connectors.md` · `routines/universe-sourcing.md` · `assets/clay/` |
| `commercial_state_file` | path | The pipeline snapshot: one row per opportunity, with current evidence, source and a dated next step. Read first at every run. | `routines/followup-engine.md` · `routines/weekly-review.md` |
| `contact_queue_file` | path | The operational queue with its sections: ready · prepared · sent · reactivations · special cases · rules. | `routines/followup-engine.md` · `policies/01-account-selection.md` · `routines/followup-engine.md (reactivation section)` |
| `account_dossier_path` | path | Where each account's research dossier lives (signals with source URLs, stakeholders, angle). One dossier per account, referenced by the queue. | `routines/followup-engine.md` · `routines/universe-sourcing.md` |
| `writing_rules_file` | path | **Hard gate.** Binding writing rules, read before every customer-facing text. | `languages/it.md` · `routines/followup-engine.md` (step 1) |
| `positioning_file` | path | ICP and offer. | `setup-and-intake.md` |
| `autonomy_boundary_file` | path | What requires approval. Read at session start. | `permissions.md` · `setup-and-intake.md` |
| `systems_of_record_file` | path | Declares where truth lives for each kind of fact. | `setup-and-intake.md` |
| `product_thesis_file` | path | The current product thesis. Read before writing copy. Where two theses are active, the conflict is declared, never silently merged. | `failure-modes.md` · `setup-and-intake.md` |

---

## Rules for changing this file

1. **Add a slot rather than hard-code a value.** If a translated policy needs a company
   value that has no slot here, the slot is missing; do not inline the value.
2. **Never rename a slot in place.** The *Consumed by* column is a dependency list. Rename
   means updating every consumer in the same change.
3. **Defaults are evidence, not recommendations.** Every default here came from one motion
   of 26 accounts. The `[INFERENCE]` markers say which were never even used. An installer
   who adopts all of them unchanged has configured nothing.
4. **The three hard gates block the install.** `icp_definition`, `approved_claims` and
   `writing_rules_file` have no defaults on purpose.
