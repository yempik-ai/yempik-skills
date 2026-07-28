# Setup and intake

This file is the install interview. No run starts before it is complete. It has four parts:
the knowledge split that decides what gets ratified versus what stays operational data, the
list of company knowledge base ratifications that gate the install, the intake questions that
produce those ratifications, and the install order that sequences all of it.

## 1. Knowledge, by nature

Knowledge the agent needs splits into four kinds. The decisive column is whether it must be
approved in the company knowledge base: if yes, it is not operational data, it is company
truth and requires human ratification.

### 1.1 Universal GTM knowledge (ships with the pack, never reconfigured)

| Knowledge | Lives in | Approval |
|---|---|---|
| An auto-reply is not interest | `doctrine.md` | no, it is kernel |
| A positive reply is not a meeting | `doctrine.md` (D7) | no |
| The single follow-up is the main multiplier | `doctrine.md` (E3) | no |
| Decorative personalisation is spam | `policies/04-message-craft.md` | no |
| An angle is chosen from a closed set | `policies/03-stakeholder-and-angle.md` | no |
| Evidence first, state second | `doctrine.md` (D6) | no |
| Files are snapshots; live systems are the truth | `doctrine.md` (D8) | no |
| Filter before you enrich | `routines/universe-sourcing.md` | no |
| A quick no is worth more than a long maybe | `doctrine.md` (E6) | no |

### 1.2 Company-specific knowledge (configured at every install)

| Knowledge | Source | Approval in the company knowledge base |
|---|---|---|
| ICP, exclusions, ordered segments | the founder | yes, mandatory |
| Offer and minimum first purchase | the founder | yes |
| Approved claims and forbidden claims | the founder | yes |
| Writing rules and register | the writing-rules file (`writing_rules_file`) | yes |
| The competitor to name, and how to name it | the positioning file (`positioning_file`) | yes |
| Prices that can be shared and prices that stay private | the founder | yes |
| Send authority and operating caps | the autonomy-boundary file (`autonomy_boundary_file`, slot `send_authority`) | yes |
| Warm relationships and special cases | the founder | yes, and it must be kept current |
| The first-touch template that already worked | evidence plus ratification | yes |
| Available angles | derived from market signals | yes, as a closed set |

Without the first three ratified, the pack must not be installed. An agent that writes copy
without ratified claims produces statements the company never authorised.

### 1.3 Operational state (live data, never ratified as durable truth)

| Knowledge | Source | Update | Approval |
|---|---|---|---|
| Who has been contacted, and when | the email connector | per run | no |
| Who has replied, and how | the email connector | on event | no |
| Stage of each opportunity | the CRM connector plus workspace files | on event | yes, only for advances into opportunity |
| Queue and position in the batch | the contact queue file (`contact_queue_file`) | per run | no |
| Open drafts | the email connector | per run | no |
| Reactivation dates | the email connector | on event | no |
| Overdue next actions | derived | per run | no |

Rule: operational state does not enter the company knowledge base as durable knowledge. Only
what remains true after the specific account is closed enters it.

### 1.4 External evidence

| Knowledge | Source | Requirement |
|---|---|---|
| Citable facts about the account | the public site | `source_url` mandatory |
| System or software in use | the public site | citable verbatim |
| Structure, offices, volumes | the public site | never inferred |
| Corporate registry data for the sanity check | public registries | contradictions are recorded, not resolved |
| Competitive context | research | never used to attack a competitor by name |

No external evidence becomes company truth. It becomes `Account.signal`, with a source and a
date.

## 2. The company knowledge base ratifications that gate the install

Three checks gate the transition out of `setup` and must be true before the first run:
`icp_approved`, `claims_approved`, `send_rule_confirmed` (`state-machine.yaml`, the `setup`
state's exit conditions). A fourth, `touch_cap_defined`, is operational rather than a
ratification: it is covered by the intake questions below.

Separately, three configuration slots have no default value on purpose and block the install
outright: `icp_definition`, `approved_claims` and `writing_rules_file`.

`warm_relationship_map` is not one of the three hard gates, but carries the same urgency: it
must be populated before the first run, not after.

## 3. Intake questions (ICP workshop script)

Mandatory before the first run. Each question produces one ratification or one configuration
slot.

1. What is the ICP, and more importantly, who is **excluded**? -> `icp_definition`,
   `exclusion_rules`.
2. Is there already a message that got a real reply? This is the single most valuable asset a
   company can bring to the first run: in the reference motion, the product itself
   (`product_name`) grew out of exactly one email that worked. -> the first-touch template,
   `first_touch_reference` in `schemas/message.schema.json`.
3. Who has the authority to send? Can the agent send, or only prepare? -> `send_authority`.
4. How many first touches per day are acceptable? -> `max_first_touches_per_day`.
5. How many email touches per account before stopping? -> `touch_cap_per_account`.
6. Which claims are approved, and which are forbidden? -> `approved_claims`.
7. What are the warm relationships and the special cases that must never be touched? ->
   `warm_relationship_map`, `special_cases`.
8. What is the system of record: where does the truth about commercial state live? ->
   `systems_of_record_file`, `commercial_state_file`, `crm_system`.
9. What does "qualified" mean at this company? Which criteria turn interest into evidence? ->
   `qualification_criteria`.
10. What is the stop rule? After how many conversations without convergence does work stop? ->
    `stop_rule_conversations`.

`[GAP]` In the reference motion, these answers already existed in the workspace, in documents
written earlier. A company without a company knowledge base will have to produce them: the
pack without these answers is an engine with no fuel, not an autonomous system.

## 4. Documents to point at before the first run

Setup cannot complete without the agent knowing where four kinds of document live. None of
these travels as a fixed file name: each installation names its own documents and points the
matching slot at them. Read in this order at session start:

1. The writing-rules file (`writing_rules_file`). Hard gate: binding writing rules, read
   before any customer-facing text.
2. The positioning file (`positioning_file`). ICP and offer.
3. The autonomy-boundary file (`autonomy_boundary_file`). What requires approval.
4. The systems-of-record file (`systems_of_record_file`). Declares where truth lives for each
   kind of fact.

Two further documents are read on their own trigger, not at every session start: the
product-thesis file (`product_thesis_file`), read before writing copy, and the commercial-state
file (`commercial_state_file`) plus the contact-queue file (`contact_queue_file`), read at
every run of the daily routine. Where two product theses are active at once, the conflict is
declared, never silently merged.

## 5. Install order

1. Answer the 10 intake questions (section 3 above).
2. Have the ICP, exclusions, claims and writing rules ratified in the company knowledge base.
3. Find the message that already worked at that company and turn it into the template. If
   none exists, the first experiment exists to produce one, not to scale.
4. Re-derive the six scoring proxies by looking at the market's own sites (`scoring_proxies`).
5. Define the angles by observing declared pains, not product features (`angle_set`).
6. Configure the caps and the send authority (`max_first_touches_per_day`,
   `touch_cap_per_account`, `send_authority`).
7. Populate warm relationships and special cases before the first run
   (`warm_relationship_map`, `special_cases`).
8. Run the adapted golden eval set.
9. Start the daily routine read-only for one week (`first_week_read_only`), then enable
   drafts.
