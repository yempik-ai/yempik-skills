# Discovery Call Prep

Prepares a discovery call before it happens: what needs to be learned, who will be in the
room, and what would make the call useful even if it ends in disqualification.

## Platform governance

This routine has no platform contract. It is a client-side procedure, run by hand or by the
agent from workspace files, not through the platform's MCP routine tools
(`routine_start_run` / `routine_checkpoint_run` / `routine_complete_run`).

## Metadata

| Field | Value |
|---|---|
| Status | `proposed`: performed by hand in the observed period, never formalised. Do not upgrade this status. |
| Objective | Arrive at the call knowing what needs to be learned and who will be across the table. |
| Trigger | Schedule: the day before every meeting set. |
| Frequency | `per_meeting` |

## Prerequisites

- A meeting set with a confirmed date and time.
- An account dossier.
- Approved discovery questions (`mandatory_discovery_questions`).

## Inputs

- Full thread.
- Dossier.
- Evidence from the site.
- Known contradictions.

## Configuration slots referenced

- The mandatory qualification questions (`mandatory_discovery_questions`) are
  market-specific: re-derive them per market from the operational process being sold into.
  See `markets/_template.md`.

## Steps

1. **Dossier.** Summarise in one page: the evidence, the signal used, the angle, and any
   open contradictions.

2. **Stakeholder.** State who is attending, their presumed role, and what is NOT known
   about their authority. Do not assume decision access from a title.

3. **Questions.** Prepare the mandatory qualification questions (`mandatory_discovery_questions`):
   a workflow with more than one step, where the source of truth lives, who updates the end
   customer, which system is currently in use, which unit can be isolated for the test, who
   is the sponsor and who approves, what outcome would make it rational to extend.

4. **Risks.** List the objections expected for this profile and the honest answer to each.

5. **Minimum useful outcome.** Define, before the call, what makes it useful even if it ends
   in disqualification.

6. **Agenda.** Check for calendar conflicts and flag them.

## Tools

| Tool | Modes |
|---|---|
| Workspace files | read, write |
| Calendar connector | read |
| Email connector | read |

## Outputs

One-page pre-call brief.

## Approval and state updates

Approval policy: none.

State updates: none.

## Failure handling

If the dossier is missing, produce the mandatory questions anyway and flag the gap. Do not
skip discovery preparation for lack of a dossier.

## Idempotency

One brief per `meeting_id`, regenerated only if the thread changes.

## Success metrics

- Share of calls in which authority and baseline are identified.

## Gap note

Both calls held (ACCOUNT-A, ACCOUNT-B) were prepared without this artefact. On ACCOUNT-B the
commercial hypothesis was refuted in the call. A pre-call brief that had already anticipated
the integration objection could have surfaced the qualification problem earlier.
