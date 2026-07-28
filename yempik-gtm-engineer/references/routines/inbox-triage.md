# Inbox Triage

Do not miss a relevant commercial email without reading the whole mailbox. Short and generic:
a light-touch scan of everything, twice a day.

## Scheduling

This routine has no platform routine contract. It is client-side only: there is no
`gtm_inbox_triage` contract and no `routine_start_run` / `routine_checkpoint_run` /
`routine_complete_run` lease as with `routines/followup-engine.md` and
`routines/weekly-review.md`. Schedule it directly in your own agent client, twice daily; no
lease is required.

## Metadata

| Field | Value |
|---|---|
| Status | `observed`: runs as an active scheduled task, twice a day. |
| Objective | Do not miss a relevant commercial email without reading the whole mailbox. |
| Trigger | Schedule: twice daily, morning and evening. |
| Frequency | `twice_daily` |

## Prerequisites

Read access to the email connector.

## Inputs

Subject lines of recent messages.

## Steps

1. **Scan subjects.** Read only the subject lines, not the bodies.
   Why: contains the cost and the reading surface.
2. **Filter.** Open only the relevant emails (clients, leads, partnerships, meetings).
3. **Recap.** Produce a summary of what requires a decision or a reply.

## Tools

| Tool | Modes |
|---|---|
| Email connector | read |

## Outputs

Triage recap.

## Approval and state updates

Approval policy: notify.

State updates: none.

## Failure handling

If the connector does not respond, declare it and do not infer the state of the mailbox.

## Idempotency

Time window since the last run, no full re-read.

## Success metrics

Zero relevant commercial emails unseen within 12 hours.

## Relationship to the follow-up engine

Triage looks at the whole mailbox with a light filter. The follow-up engine
(`routines/followup-engine.md`) looks only at accounts in the pipeline and in the queue, but in
depth. They are complementary: the first finds what you do not expect, the second makes sure
that what you do expect does not go cold.
