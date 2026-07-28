# Data model

Five objects: `Account`, `Stakeholder`, `Message`, `Outcome`, `Experiment`, plus one authoring
template, `learning-delta-template.md`.

## What these are, and what they are not

These are **client-side working formats**. The agent validates its own artefacts against them
before it hands anything over: a scored account, a stakeholder record, a draft, a recorded
outcome, a batch. They are a discipline on the agent's output, nothing more.

They **never travel to the Yempik platform**. No property here is a wire format, a column or an API
payload. The platform has its own contracts and the agent uses those verbatim when it talks to
the platform. If a field in this folder ever looks like it needs to be sent somewhere, that is
a sign the boundary has been crossed and the field is wrong.

The schemas are JSON Schema draft 2020-12 and validate with any standard validator.

## The two extension keys

Every property carries two non-standard keys that are part of the contract, not annotations:

- `x-source`: where the value comes from. One of `website`, `email`, `crm`, `founder`,
  `agent_inference`, `workspace_file`, `calendar`, `computed`.
- `x-update`: how it changes. One of `once`, `on_event`, `per_run`, `manual_only`, `derived`.

They exist so that the agent cannot quietly overwrite a founder-owned value with an inference,
or recompute per run something that was fixed once. Strip them and the schemas still validate,
but they stop being a discipline and become documentation.

## No field was invented

Every property corresponds to a column or a piece of information that really existed in the
reference motion's pipeline file, contact queue, approved shortlist, validation notes or email
threads. Fields that would have been useful but were never used are not here.

Where a value differs between one company and the next, the schema does not hard-code it: it
carries an open string and a `$comment` naming the configuration slot or the market file that
validates it. This applies to `Account.segment_id`, `Account.signal.type`, `Account.angle_id`
and `Message.template_id`. The reference motion's own values live in `references/markets/`,
not in the schemas.

## Five fields with no real-world backing

The state machine needs these, but the reference motion never populated them. An installer
starts them from zero and should not read the schema as evidence that they work:

- `Account.contradictions`: used exactly once.
- `Outcome.time_to_reply_minutes`: computable at the time, never computed.
- `Experiment.statistical_caveat`: introduced to prevent a known failure mode, never present
  before it.
- The whole learning delta: the real learning happened in dated notes and direct human
  corrections, not in a structured object.
- Structured run logging: the routine executions were never logged in a structured way.

They are marked necessary, not observed.

## Two schemas that are gone

The private pack had a `Run` and a `Routine` schema. Both are superseded by platform contracts
and are deliberately not shipped here:

| Dropped | Replaced by | The idea that survived |
|---|---|---|
| `run.schema.json` | The platform's own run records, created and closed through the routine run lifecycle. | A run that read only files may not declare a state. This is now a stated obligation in the objective of each file in `references/routines/`. |
| `routine.schema.json` | The platform's `RoutineContract`, which owns the routine's identity, schedule, inputs and checkpoints. | The binding read order, most authoritative source first. This is now the opening ordered list of each file in `references/routines/`. |

Recreating either object client-side would give the agent a second, private notion of what a
run is, and the two would drift. There is one run record and the platform owns it.

## The one hard rule in this folder

`Message.compliance_checks`: **every required check true is a necessary condition to deliver a
draft.** Not a warning, not a score, not something to note in the brief and hand over anyway.
A false value means the draft does not leave the agent.

The required set is universal: `single_cta`, `tracked_link_present`, `claims_approved`,
`no_duplicate_draft`. Register checks that depend on the customer language live in the nested
`language_checks` object and are supplied by the active adapter in `references/languages/`.

Necessary is not sufficient. All checks green means the draft is deliverable, not that it is
good. A message can pass every check and still cite a fact nobody would care about.
