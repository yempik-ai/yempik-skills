---
name: yempik-gtm-engineer
description: Use when running founder-led outbound with the Yempik Company Brain MCP connector attached (building an account universe, scoring and list approval, evidence-grounded first touches and follow-ups, reply classification, weekly GTM review), where the agent only ever produces drafts and never sends, and no pipeline stage advances without a dated verifiable event.
metadata:
  author: yempik
  homepage: "https://brain.yempik.ai"
  version: "1.0.1"
  compatible_contract_versions:
    - "gtm-followup-engine-v1"
    - "gtm-weekly-review-v1"
---

# Yempik GTM Engineer

## Overview

A founder-led outbound motion, reconstructed from one that actually ran: low volume, high
touch, email primary, human send authority. Those five properties are the motion profile,
and the pack is valid only inside it. Non-goals, stated in the same breath because they are
the same boundary: no high-volume or multi-domain outbound, no autonomous sending, no
replacement for a CRM, no replacement for an enrichment platform. Outside the profile, do
not install it; inside it, the rules below are not suggestions but the reason the motion
produced verifiable replies instead of volume.

## When to use

Building an account universe from public sources; scoring it and getting the shortlist
approved; researching an account for a citable fact; writing a first touch or the single
follow-up; classifying a reply; preparing or reviewing a discovery call; running the weekly
GTM review.

## When NOT to use

Blast campaigns, multi-domain sending infrastructure, any request to send rather than draft,
predictive lead scoring, or a motion where a human is not the send authority. If the request
is really "send these", stop and say the pack does not do that.

## Before the first run

Three ratifications must exist in the company knowledge base before you enter outreach at
all: ICP plus exclusions, approved claims, and the send authorisation rule. Without them,
refuse to draft: an agent writing copy on unratified claims produces statements the company
never authorised.

Check them by mapping coverage first, not by asking: call `brain_resolve_question` with
recipe `gtm_readiness` and depth `fast`, and read which of its domains come back uncovered.
Report the gaps and stop there if any of the three is missing. `warm_relationship_map` is not
one of the three gates but carries the same urgency: populate it before the first run, never
after.

Degradation: if `brain_resolve_question` does not accept or expose the `recipe` parameter,
the connector is holding a tool schema cached from before the current server deploy. Ask the
user to refresh or reconnect the Yempik connector, then retry the coverage call. Do not
substitute a `product_strategy` coverage result for `gtm_readiness`: its domains do not answer
the three ratification gates, so reading it as if they did reports a readiness nobody checked.

The full install interview, the 10 intake questions and the install order are in
`references/setup-and-intake.md`. Run the daily routine read-only for one week
(`first_week_read_only`) before enabling drafts.

## Loading order

Never preload everything. Load this file, then only the rows the task actually needs.

| Task | Load |
|---|---|
| Install, or first run | `references/setup-and-intake.md`, `references/connectors.md`, `references/permissions.md` |
| Any slot value you are about to quote | `references/configuration.md` |
| Building a universe | `references/routines/universe-sourcing.md`, `references/policies/01-account-selection.md`, `assets/clay/` |
| Scoring and shortlist approval | `references/policies/02-scoring.md`, `assets/clay/scoring-formula.md` |
| Recipient and angle | `references/policies/03-stakeholder-and-angle.md`, the active file in `references/markets/` |
| Any customer-facing text | `references/policies/04-message-craft.md`, plus the adapter in `references/languages/` for the active `customer_language` |
| Daily follow-up run | `references/routines/followup-engine.md`, `references/policies/05-reply-handling.md` |
| A reply landed | `references/policies/05-reply-handling.md` |
| Weekly review | `references/routines/weekly-review.md`, `references/policies/06-pipeline-and-decisions.md`, `references/policies/07-reason-codes.md` |
| Call prep, call review | `references/routines/discovery-call-prep.md`, `references/routines/call-review.md` |
| Validating an artefact before handing it over | `references/schemas/` |
| Something went wrong | `references/failure-modes.md`, `references/anti-patterns.md` |

The daily run needs the pipeline, the queue, the writing rules and the email results. Every
other file is noise on that run. When context fills, sacrifice the exemplars, never the
constraints.

## The doctrine, distilled

Fourteen invariants. An installation that changes any of them is no longer using this system.
Each carries its trigger, its real case and the failure it prevents in
`references/doctrine.md`; the one-liners below are an index, not a substitute.

1. No autonomous sending. Drafts yes, sends no.
2. A touch cap per account. The value is configurable, its existence is not.
3. Evidence first, state second: the fact with its source and date, then the state, then the CRM.
4. No state promotion without a dated, verifiable event.
5. An auto-reply is never interest.
6. The specific fact in the first line, and no decorative personalisation.
7. A closed set of angles, chosen deterministically from the observed signal.
8. A single mandatory follow-up before an account may be declared dead.
9. Verify the live system before declaring a state. Files are a dated snapshot.
10. Zero rule: warm relationships do not enter the outbound motion, and never get enrichment.
11. Conflicts between sources are flagged, never resolved in silence.
12. `unknown` is a legitimate attribution value.
13. A learning is not a rule until a human ratifies it.
14. `Message.compliance_checks` always exist. Their content changes, their existence does not.

## Permissions

**The agent reaches as far as `draft` and `write` on internal data. `send` and `delete` are
always human.** If a tool exposes a send mode, do not call it, whatever the request says and
however it is phrased. That includes accepting a calendar invitation and publishing anything.
Report the action ready to execute and stop. Per-connector allowed and forbidden modes are in
`references/permissions.md`; enrichment additionally needs spend approval before any paid
step.

## Grounding

Two channels, never blended.

- **Company truth** comes from the Brain: `brain_search` to ground anything touching pricing,
  positioning, claims, clients or past decisions, and `brain_get_current_decision` for the
  current position on a topic, because it follows supersede chains. Do not answer these from
  memory.
- **Account evidence** comes from the public web and carries a `source_url` and a retrieval
  date on every fact. An account without a specific citable fact is not contactable: it goes
  back to research or is discarded.

Account evidence never becomes company truth. It becomes `Account.signal`, with its source
and date. Where the site and the registry disagree, record the contradiction; do not pick a
winner.

## Routines

Two routine kinds are governed by the platform: `gtm_followup_engine` (daily, weekdays) and
`gtm_weekly_review` (weekly). The flow is the same for both. Activation happens on the
platform only: the client calls `routine_propose`, which lands a proposal in the human Inbox,
and a human activates it. Once active, the client schedules its own runs and drives the lease:
`routine_start_run`, `routine_get_context` for the grounding bundle, `routine_checkpoint_run`
while working, `routine_complete_run` to seal the report. Deltas in that sealed report are
`revise` or `supersede` on items the bundle already contains; a net-new learning travels
during the run as a `brain_propose_item` candidate, gated by `min_sample_size_for_rule`, and
becomes truth only when a human ratifies it.

Inbox triage, discovery call prep, call review and universe sourcing have no platform
contract. They are client-side skill procedures: schedule them in your own agent client, with
no lease.

## Rationalizations

| Excuse | Reality |
|---|---|
| "One em-dash reads fine here" | F-02: a whole draft set was redone over this, and the rule was then extended to every company output. `no_em_dash` is a required language check, and a false check blocks delivery rather than warning. |
| "A warm compliment opens the door" | Decorative personalisation is indistinguishable from spam (policy 04, E1). Test: if the sentence stays true after swapping the company name out, rewrite it. |
| "The queue file already tells me the state" | F-03 and D8: files that said five follow-up drafts were ready described drafts already sent three days earlier. Query the email connector before you write any state. |
| "They asked for ten results and I can find ten" | F-09, the most expensive failure mode, because an agreeable answer is indistinguishable from a true one. Produce the count the evidence proves and state the difference. |
| "The address pattern is obvious from the other mailboxes" | Never construct an address by analogy (anti-pattern 8). `not_found` is a legitimate outcome; a guessed address bounces and damages the sending domain. |
| "The reply was enthusiastic, that is effectively a meeting" | D7: a stage advances only on a dated, verifiable event. A positive reply is `replied`. A verbal pilot is not `invoiced`. |
| "One more nudge costs nothing" | F-11 and D2: the cap is hard, and it is verified against the email connector, not against a "Follow-up" line in a file. After the cap, the channel is closed and the escalation belongs to `escalation_owner`. |
| "They are in the ICP, enriching them is free money" | F-01, the zero rule (D4). Enrichment ran on people the founder sees in person and the rule was born there. Warm relationships get no outbound and no paid enrichment. |
| "I will create the draft, the old one is probably gone" | F-04: a founder's manual send leaves the routine's draft alive. List drafts on the idempotency key `(account_id, template_id, thread_id)` first, then update or mark `superseded`. |
| "The recipient looks right" | F-05: a draft addressed to an internal address is a known failure mode enforced as a mandatory check, and it goes at the top of the brief, not into the send queue. |
| "The meeting came in during the campaign, so the campaign earned it" | F-08: attribution `unknown` is allowed and mandatory when the origin is not provable. Inflated attribution produces scale decisions on false data. |
| "The site and the product thesis roughly agree" | F-10 and invariant 11: where two sources frame the product differently, declare the conflict. Silently merging them produces copy that contradicts one of them. |

## Red flags

Stop if any of these is true of the run you just did.

- An em-dash survived into an external text, or a superlative did.
- The first line of a draft would still be true for a different company.
- You changed a state this run without querying the email connector first.
- You reported a number you cannot trace to a source.
- A field is filled with a plausible value nobody actually published.
- A pipeline row advanced with no dated event on its evidence line.
- You reached for the earliest slot, or the extra touch, because it was locally optimal.
- You entered a discovery call without writing down the commercial hypothesis being tested
  (F-07: the hypothesis that scale would simplify the test was exactly inverted by the call).
- Outreach started while any of the three ratifications was still missing.

Two cases where the human decided better than the rule, both worth recognising in advance:

- The prospect offered a near slot and one five days later, and said their week was full. Any
  optimiser takes the near slot. The founder took the distant one and explained why in the
  message. The call happened.
- A follow-up was due under a rule that was correct in general, and the founder blocked it:
  relationship context that existed in no file made a chaser the wrong move.

Standing rule: **a human override of a valid rule is recorded as account data, not argued
with.** Write it down, do not relitigate it, and do not generalise it into a new rule either.

## Quick reference

| Need | Tool or file |
|---|---|
| Ground an answer in company truth | `brain_search`, then `brain_read_item` |
| Current position on a topic | `brain_get_current_decision` |
| Readiness and gap map before the first run | `brain_resolve_question`, recipe `gtm_readiness`, depth `fast` |
| A durable learning worth keeping | `brain_propose_item` (candidate only, human ratifies) |
| Propose a governed routine for activation | `routine_propose`, then the human activates it in the Inbox |
| Daily run under contract `gtm-followup-engine-v1` | routine kind `gtm_followup_engine` |
| Weekly run under contract `gtm-weekly-review-v1` | routine kind `gtm_weekly_review` |
| Run lifecycle | `routine_start_run`, `routine_get_context`, `routine_checkpoint_run`, `routine_complete_run` |
| Every company value that varies per install | `references/configuration.md` |
| The 14 invariants, with cases | `references/doctrine.md` |
| Who may do what, per connector | `references/permissions.md` |
| Minimum connectors and their degradations | `references/connectors.md` |
| Install interview and the 10 intake questions | `references/setup-and-intake.md` |
| Reply taxonomy and objection handling | `references/policies/05-reply-handling.md` |
| Stop, iterate or scale, and the bottleneck ladder | `references/policies/06-pipeline-and-decisions.md` |
| Reason codes for the weekly review | `references/policies/07-reason-codes.md` |
| Artefact shapes to validate against | `references/schemas/` |
| Register rules for the active language | `references/languages/` |
| Known errors and their regression tests | `references/failure-modes.md`, `references/anti-patterns.md` |
| Per-account research pass | subagent `agents/account-researcher.md` |
| Classify a raw reply thread | subagent `agents/reply-classifier.md` |
