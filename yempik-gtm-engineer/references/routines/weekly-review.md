# Weekly Review

The weekly routine that turns a week of outbound into decisions, not a summary. It reads the
commercial state, the contact queue and the week's email, assigns reason codes, picks exactly
one variable to change, and checks the stop rule. Related: `policies/06-pipeline-and-decisions.md`
(the stop/iterate/scale formula and the bottleneck ladder) and `policies/07-reason-codes.md`
(the taxonomy used in step 2).

## Platform governance

This routine runs under the `gtm_weekly_review` contract via the platform's MCP routine tools
(`routine_start_run` / `routine_checkpoint_run` / `routine_complete_run`). Idempotency key:
(`routine_id`, `week`): one dated review file per week, with sections appended in date order
within that week; the file is never cumulative across weeks.

Where the review surfaces a repeatable pattern (a recurring reply pattern, a reason-code
cluster, a corrected assumption), it may be proposed to the company knowledge base as a
learning candidate via `brain_propose_item`, following the shape in
`schemas/learning-delta-template.md`. The proposal is gated by `min_sample_size_for_rule`
(reference default: 30): below that sample size the candidate may only be filed as a
`hypothesis`, never as a `rule`, whatever the evidence looks like. Proposing creates a
candidate only, with no external effect; a human ratifies it before it becomes active truth.

## Metadata

| Field | Value |
|---|---|
| Status | `observed`: corrected on day 18 to record that this is an active scheduled task, not a proposal. |
| Objective | Turn the week of outbound into decisions, not a summary. |
| Trigger | Schedule: Friday afternoon. |
| Frequency | `weekly` |

## Prerequisites

- Current commercial state readable (`commercial_state_file`).
- Contact queue updated (`contact_queue_file`).
- Read access to the last 7 days of email.
- Outbound doctrine loaded before starting (`doctrine.md`).

## Inputs

- Canonical commercial state.
- Pipeline detail.
- Contact queue.
- Emails sent and replies from the last 7 days.
- The decision log embedded in the commercial state file (`commercial_state_file`), read only
  for the context of this week's dated entries.

## Steps

1. **Numbers.** First touches sent, follow-ups sent, total replies, positive replies, calls set
   and calls held. Compare against the previous week if the file exists.
2. **Reason code.** Classify negative or absent replies with the taxonomy
   (`policies/07-reason-codes.md`).
3. **Voice of the market.** Objections and recurring language in actual replies, with short
   quotations. Facts kept separate from interpretations.
4. **One variable.** Critical step. Exactly `variables_changed_per_week` (reference default: 1)
   variable to change the following week: subject line, angle, segment or pace. Never more than
   one, justified against the numbers.
5. **Stop rule.** State where the count stands against `stop_rule_conversations` (reference
   default: 10) qualified conversations. If they do not converge on a payable workflow, say so
   explicitly.
6. **Actions.** Actions proposed for Monday, in order of impact.
7. **State correction.** If verified facts emerge that close a gap declared in the commercial
   state, apply a minimal factual correction with a link to the review. Guard: do not touch
   sections that require a founder decision.

## Tools

| Tool | Modes |
|---|---|
| Workspace files | read, write |
| Email connector | read |

## Outputs

Dated review file, one file per week, not cumulative.

## Approval and state updates

Approval policy: notify.

State updates: `Experiment.decision`, factual correction to the commercial state file.

## Failure handling

Do not invent numbers. If a figure is not measurable, write that it is missing and how to make
it measurable. No sending, no changes to the queue.

## Idempotency

One file per week, dated sections appended.

## Success metrics

- Exactly one variable changed per week.
- Reason codes assigned with a quotation.
- Stop rule verified.

## Design note

The "one variable" rule is the core of this routine. Changing the subject line, the angle and
the segment in the same week makes it impossible to know what worked: at low volumes there is
no statistical power for parallel tests.
