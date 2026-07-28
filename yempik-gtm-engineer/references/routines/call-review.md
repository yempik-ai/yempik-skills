# Call Review

Turns a call into evidence, a decision and learning candidates.

## Platform governance

This routine has no platform contract. It is a client-side procedure, run from workspace
files and the CRM connector, not through the platform's MCP routine tools
(`routine_start_run` / `routine_checkpoint_run` / `routine_complete_run`).

## Metadata

| Field | Value |
|---|---|
| Status | `proposed`: in the observed period the debrief ended up in the deltas of the commercial state file, not in a dedicated artefact. Do not upgrade this status. |
| Objective | Turn a call into evidence, a decision and learning candidates. |
| Trigger | Event: a call held. |
| Frequency | `per_meeting` |

## Prerequisites

Notes or a transcript of the call.

## Inputs

- Notes.
- Pre-call dossier.
- Commercial hypothesis stated beforehand.

## Configuration slots referenced

- Step 2 evaluates the qualification criteria (`qualification_criteria`): an available real
  unit, a named operational owner, an observable workflow, exportable data, a named
  approver, budget or process, a baseline metric.
- Step 7 updates the CRM connector (`crm_system`), if one is configured.

## Steps

1. **Facts.** Extract only the facts stated by the customer, separating them from
   interpretations.

2. **Qualification.** Evaluate the qualification criteria (`qualification_criteria`): an
   available real unit, a named operational owner, an observable workflow, exportable data,
   a named approver, budget or process, a baseline metric.

3. **Hypothesis.** Compare the pre-call commercial hypothesis against what emerged and
   explicitly declare whether it is confirmed or refuted. This is the highest-value step in
   the routine: skipping it turns a call into an anecdote instead of evidence.

4. **Objections.** Record every objection and classify it (product, price, risk, timing,
   competition).

5. **Outcome.** Assign `pilot_qualified` / `nurture` / `disqualified`, with a written
   rationale.

6. **Product.** Separate feature requests from recurring roadmap signals.

7. **State.** Update the evidence, the pipeline row and the CRM connector (`crm_system`), in
   that order.

8. **Learning.** For anything that contradicts a previous assumption, write a learning delta
   using `schemas/learning-delta-template.md`. This routine does not propose to the company
   knowledge base directly: the delta is carried forward and proposed from
   `routines/weekly-review.md`, which is where Brain proposals are made. A learning delta
   produced here is a draft candidate, not yet a proposal.

## Tools

| Tool | Modes |
|---|---|
| Workspace files | read, write |
| CRM connector | propose, write |

## Outputs

`call_record`, qualification outcome, objections, learning candidates (as learning-delta
drafts, see step 8).

## Approval and state updates

Approval policy: notify. Required if price, scope or opportunity state changes.

State updates: `Account.state`, `Outcome`. There is no `LearningCandidate` state object:
that schema was converted to the `schemas/learning-delta-template.md` markdown template,
and the store is the platform's review Inbox, not a field on this routine.

## Failure handling

Without notes from the call, do not invent content. Record only that the call took place.

## Idempotency

One record per `meeting_id`.

## Success metrics

- Share of calls with an outcome declared within 24 hours.
- Number of refuted hypotheses recorded.

## Real example

ACCOUNT-B, day 18: hypothesis "scale makes the test easier" refuted. Dominant objection:
integration. Outcome: nurture. Product signal (migration off the incumbent system) emerged
for the second time, after ACCOUNT-A.
