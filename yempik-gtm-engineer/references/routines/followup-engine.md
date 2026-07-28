# Follow-up Engine

The daily routine that keeps the first-touch queue, the reply queue and the reactivation
queue moving. It produces briefs and drafts. It never sends.

This file merges three source routines: the daily follow-up run itself, the queue-exit step
from reply handling (step 4 below), and the daily reactivation check (its own section at the
end). Reply classification and objection handling in general are specified in
`policies/05-reply-handling.md`; this file covers only the step that removes an
account from the outbound queue once a reply exists.

## Platform governance

This routine runs under the `gtm_followup_engine` contract via the platform's MCP routine
tools (`routine_start_run` / `routine_checkpoint_run` / `routine_complete_run`). Idempotency
key: (`routine_id`, `date`). This platform-level key deduplicates runs of the routine itself;
it is separate from the draft-level idempotency key described below, which deduplicates
individual drafts within a run.

## Metadata

| Field | Value |
|---|---|
| Status | `observed`: runs in production as a scheduled task. |
| Objective | No follow-up lost, no reply left to cool off, first-touch queue keeps advancing. Produces briefs and drafts. Never sends. |
| Trigger | Schedule: every weekday morning, before working hours. |
| Frequency | `daily_weekday` |

## Binding read order

The order below is binding: read the most authoritative source first.

1. The commercial state file (`commercial_state_file`).
2. The contact queue file (`contact_queue_file`).
3. The per-account research dossier at the `account_dossier_path` slot.
4. The writing-rules file (`writing_rules_file`).
5. Email: replies from the last 48 hours plus the weekend, threads with the product in the
   subject line, bounces.

Live systems required: the email connector (`evidence_of_record`).

## Prerequisites

- Read access to the email connector.
- An existing contact queue (`contact_queue_file`) with Ready / Prepared / Sent /
  Reactivations / Special cases sections.
- Writing rules approved and readable (`writing_rules_file`).
- A commercial pipeline (`commercial_state_file`) with a dated "next step" column.

## Configuration slots referenced

- Prepare at most `max_first_touches_per_day` first-touch drafts per run (reference default: 3).
- Treat a next step as due once `followup_window_days` has elapsed since the previous touch
  (reference default: 4-5 days, `[INFERENCE]`: a median of observed intervals, never a
  written rule).
- An account never receives more than `touch_cap_per_account` touches before it exits the
  queue (reference default: 2).
- Aim to act on a reply expressing interest within `reply_response_target` (reference
  default: 1 working hour).

## Steps

1. **Load state.** Load the pipeline, the queue and the writing rules.

2. **Verify the live system.** Critical step. Query the email connector for new replies,
   bounces and drafts that already exist. Compare against the files: every divergence is a
   discrepancy, reported at the top of the brief.

   Real failure prevented: on day 18, the files indicated 5 follow-up drafts ready; the
   email connector showed they had already been sent on day 15. Without this step, 5
   duplicate drafts would have been created.

3. **Bounces.** Search sent emails for delivery failures; a bounce goes to the top of the
   brief with the alternative address.

4. **Classify replies.** Apply `policies/05-reply-handling.md`, one class per reply.

   4b. **Queue exit** (merged from reply handling, step 4). If the account was in the
   outbound queue, remove it and move it into the reply-handling flow.

5. **Follow-ups due.** For every account whose next step is overdue or due today, with no
   reply, prepare a short draft (2-4 sentences) as a reply in the original thread, one CTA
   only. Guard: check existing drafts before creating a new one.

6. **First touches.** Prepare drafts from the queue in order (Ready first, then the next
   approved batch), using the first-touch template, the angle from the queue, and the
   tracked-link rule. Guard: if the contact's email is marked "to find," search the site for
   it; if it is not there, flag it rather than guess.

7. **Update files.** Move worked rows into Prepared with the date; update pipeline rows
   where the evidence is unambiguous.

8. **Brief.** Produce the four-section brief.

## Tools

| Tool | Modes |
|---|---|
| Email connector | read, draft |
| Workspace files | read, write |

## Outputs

Brief sections:

- New replies (who, what they said, recommended action)
- Follow-ups due today or overdue
- First touches prepared
- Nothing to do (if everything else is empty)

Artifacts: email drafts, updated status rows.

## Approval and state updates

Approval policy: required. Every send belongs to the founder.

State updates: `Account.state`, `Account.next_action`, `Message.status`, `Outcome`.

## Failure handling

If the email connector is unreachable, produce the brief from the files anyway and
explicitly declare the degradation. Do not infer reply status from the files alone.

## Idempotency

Key = (`account_id`, `template_id`, `thread_id`). Before creating a draft, list existing
drafts and search for the thread. A draft that already exists is updated or marked
superseded, never duplicated. Rows moved into Prepared are not re-selected the next day.

## Success metrics

- Zero replies without action within 24 hours.
- Zero duplicate drafts.
- Zero emails sent by the agent.
- Queue progress: 2-3 new accounts prepared per day.

---

# Reactivation

Checked at every daily run, alongside the steps above. Resumes accounts that asked to be
recontacted, on the right date.

## Metadata

| Field | Value |
|---|---|
| Status | `observed`: the mechanism exists in the contact queue file but has not yet triggered. |
| Objective | Resume accounts that asked to be recontacted, on the right date. |
| Trigger | Checked at every daily run. |
| Frequency | `daily_weekday` |

## Prerequisites and inputs

Prerequisites: a reactivations table with dates in ISO format.

Inputs: `reactivation_date`, original context, angle for resuming contact.

## Steps

1. **Check.** For each account in the Reactivations section: if `reactivation_date` <=
   today, it re-enters the queue.

2. **Angle.** Resume from the deferral, not from the first touch. Cite the prior agreement
   (for example, "as we agreed earlier"), do not repeat the initial pitch.

3. **Draft.** Prepare the draft in the original thread.

4. **Record.** Move the row from Reactivations to Prepared.

## Tools

| Tool | Modes |
|---|---|
| Workspace files | read, write |
| Email connector | read, draft |

## Outputs

Resumption draft, updated queue.

## Approval and state updates

Approval policy: required.

State updates: `Account.state`, `Account.reactivation_date`.

## Failure handling

If the date is more than `reactivation_stale_after_days` days in the past (reference
default: 30), flag it instead of reactivating automatically.

## Idempotency

One reactivation per account per cycle; clear `reactivation_date` after use.

## Success metrics

- Zero missed reactivations.
- Zero touches before the date.

## Reference example

ACCOUNT-I, day 54: "we'll be in touch again then," as agreed. No touch before that date.
