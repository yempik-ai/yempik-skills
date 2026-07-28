# Connectors

Minimum requirements and acceptable degradations for running the pack outside a full
reference install. See `permissions.md` for the allowed and forbidden modes per connector.

## Minimum requirement: email connector

An email connector that provides:

| Capability | Required | If missing |
|---|---|---|
| thread search by query and date | **yes** | the system is not installable: without reply verification it is blind |
| reading the message body | **yes** | classification becomes guessing |
| draft list | **yes** | deduplication becomes impossible, risk of duplicate sends |
| draft creation | no | degradation: the agent proposes the text in the brief and the founder copies it |
| send | **never used** | irrelevant |

This is the `evidence_of_record` slot in `configuration.md`: the email connector is the
truth about replies, and the hard minimum above is not optional.

## Optional connectors and their degradations

| Connector | If present | If absent |
|---|---|---|
| CRM | proposed advances with confirmation | the pipeline file becomes the only record: declare it |
| Calendar | checks conflicts before proposing a slot | propose the slot and ask the founder to verify |
| Enrichment | only decisive missing fields, with approval | agent-first sourcing, which is already the observed default |
| Web research | signal and public email addresses | the system cannot generate new accounts, it can only work existing lists |

These map to the `crm_system`, `calendar_system` and `enrichment_platform` slots in
`configuration.md`, all with a reference default of `none` (optional).

## Contract for every tool call

Every call is recorded in `Run.tools_called`: name, mode (`read`/`propose`/`draft`/`write`/
`send`/`delete`), target, outcome. A run that cannot say what it called is not auditable,
and its output must not be used to update state.

## Behavior on error

1. Do not retry silently more than once.
2. Declare the degradation in the output: which source is missing and what is not
   verified.
3. Produce the part of the work that does not depend on the missing source anyway.
4. Do not replace a missing data point with an inference presented as a fact.

Rule actually followed by the routine: if the email connector does not respond, the brief
is produced anyway from the files, declaring that replies were not verified.

## Minimum idempotency

Mandatory keys: `(account_id, template_id, thread_id)` for messages, `(routine_id, date)`
for runs, domain for accounts. Without these, the automation produces duplicates and
generates friction instead of reducing it.

## Per-connector error and deduplication behavior

### Email connector

- Error: if unreachable, produce the brief from the files, declaring the degradation; do
  not infer replies from the files.
- Deduplication key: `(account_id, template_id, thread_id)`. List drafts before creating
  one. An existing draft is updated or marked `superseded`.

### Workspace files

- Error: if an update fails, report it in the brief, do not retry silently.
- Deduplication: one row per account; delta notes are appended with a date, never
  overwritten.

### CRM connector

- Error: report the misalignment between the CRM and the workspace, do not choose which
  one is right.
- Deduplication: one account per company, multiple opportunities on the same account.
  Never duplicate the company.

### Calendar connector

- Error: when in doubt about a conflict, report it instead of proposing the slot.

### Enrichment connector

- Error: "no result" is a definitive outcome; record it and plan a fallback. Never invent
  a value.
- Deduplication: by LinkedIn URL or domain plus name; filter before you enrich.

### Web research

- Error: if the email address is not published, report it. Never construct an address by
  analogy.

### Sandbox and file generation

- Error: verify the artifact produced before delivering it, do not declare it ready
  without a check.
