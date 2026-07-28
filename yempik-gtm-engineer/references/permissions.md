# Permissions

Levels, from least to most dangerous: `read` (reads) · `propose` (suggests in the brief) ·
`draft` (creates a non-active artifact) · `write` (modifies internal state) · `send`
(irreversible external effect) · `delete`.

**General rule of the pack: the agent reaches as far as `draft` and `write` on internal
data. `send` and `delete` are always human.** This is the `send_authority` slot (reference
default: `human_only`) in `configuration.md`; see `doctrine.md` (D1).

Error handling and deduplication keys are per-connector and are documented in
`connectors.md`, not repeated here.

## Email connector

| Field | Content |
|---|---|
| Allowed modes | `read`, `draft` |
| Forbidden modes | `send`, `delete`, modifying labels on customer threads |
| When to use it | every run: check replies, bounces, existing drafts; create follow-up and first-touch drafts |
| When NOT to use it | to infer state without reading the full thread; to send anything |
| Data read | thread, messages, sender, date, body, draft list |
| Data written | drafts only |
| Risk | high: contains conversations with real customers |
| Approval | `read` no · `draft` no · `send` **always** |

## Workspace files

| Field | Content |
|---|---|
| Allowed modes | `read`, `write` |
| Forbidden modes | `delete` of evidence or historical files; rewriting history to make it look cleaner |
| When to use it | read state at every run; update the queue and the pipeline when the evidence is unambiguous |
| When NOT to use it | to record a state change without a citable fact |
| Data written | state rows, queue sections, dated delta notes |
| Risk | medium: reversible, but it is the company's memory |
| Approval | no for state updates with evidence; **yes** for changes to rules, policy or decisions |

## CRM connector

| Field | Content |
|---|---|
| Allowed modes | `read`, `propose`, `write` with confirmation |
| Forbidden modes | `delete`, silent writes |
| When to use it | when a verifiable event changes the state of an opportunity |
| When NOT to use it | to create opportunities from unattributed events (the ACCOUNT-F case) |
| Risk | medium-high: it is the operational system of record, misalignment contaminates decisions |
| Approval | **yes** to create or advance opportunities |

This connector maps to the `crm_system` slot (reference default: `none`, i.e. optional) in
`configuration.md`.

## Calendar connector

| Field | Content |
|---|---|
| Allowed modes | `read`, `draft` (slot proposal) |
| Forbidden modes | `send` of invitations, accepting invitations, `delete` of events |
| When to use it | check conflicts before proposing a slot |
| Risk | high: an invitation is visible to the customer |
| Approval | **yes** for any invitation |

This connector maps to the `calendar_system` slot (reference default: `none`, i.e.
optional) in `configuration.md`.

## Enrichment connector

| Field | Content |
|---|---|
| Allowed modes | `read` with prior approval |
| Forbidden modes | any use on warm relationships; enrichment on rows outside the ICP |
| When to use it | only on the missing data point that changes the recipient, the message or the next action |
| When NOT to use it | when the public website is enough. In the observed period it was **never used** |
| Risk | medium: it costs money and can violate the zero rule |
| Approval | **yes**, because it involves spend |

This connector maps to the `enrichment_platform` slot (reference default: `none`, i.e.
optional) and to `enrichment_spend_approval` (reference default: `required`) in
`configuration.md`. The zero rule is `doctrine.md` (D4).

## Web research

| Field | Content |
|---|---|
| Allowed modes | `read` |
| When to use it | find the citable fact and the public email address |
| When NOT to use it | to confirm facts internal to the company, which live in the workspace |
| Risk | low, but it is the source of facts used in copy: every cited fact must have a `source_url` |

## Sandbox and file generation

| Field | Content |
|---|---|
| Allowed modes | `read`, `write` in the workspace area |
| Risk | low |
| Approval | no |
