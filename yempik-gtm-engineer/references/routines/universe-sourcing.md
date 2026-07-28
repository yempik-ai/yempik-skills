# Universe sourcing

**Status:** observed. Actually run on day 7, 152 accounts sourced.

**Objective:** build a qualified, scored account universe from zero for a vertical, within a
limited enrichment budget. This is the engine that generates the contacts that are later
written to.

**Trigger:** manual. When the contact queue drops below 10 ready accounts, or a new geography
opens.

**Frequency:** on_demand. Not scheduled: this is a project, not a daily routine.

## Channel rule

The channel depends on volume, not on which enrichment tool is in use.

| Volume | Channel | Why |
|---|---|---|
| 1-20 rows, ad-hoc research | the enrichment connector (`enrichment_platform`), from the conversation | fast, sufficient for work on single accounts |
| Above roughly 20 rows, recurring work | the enrichment platform (`enrichment_platform`), tables and a scan agent | the connector cannot handle the volume and is not repeatable |

Rule: above roughly 20 rows, propose the platform instead of forcing the connector. The
connector is comparatively unstable across sessions. The reference run worked at 200-300 rows
and used the platform throughout.

## Prerequisites

- ICP approved (`icp_definition`, ratified before install).
- Geography decided (`geography`).
- An actions budget declared and approved by the founder (`enrichment_spend_approval`,
  reference default: required).
- A suppression table available: previous universe, warm relationships (`warm_relationship_map`),
  competitors.

## Inputs

Vertical, geography, actions budget, ICP, exclusions (`exclusion_rules`).

## Steps

### 1. Sourcing

Cost: cheap.

Collect accounts from public sources, in this order:
1. Local maps and directories, with the sector's category queries.
2. Category directories and regional trade associations, where public.
3. Customer pages of the sector's software vendors, where they expose their customers.

Columns: name, domain, city, province, source, social profile if it exists.

Real output: 152 accounts across two regions.

### 2. Normalize and suppress

Cost: free. Formulas only, no paid action.

Deduplicate on domain, and on name plus city. Apply the suppression table: previous universe,
customers and warm relationships (zero rule), competitors and software vendors. Exclude
categories that are not customers: software houses, associations, single units.

Critical: yes.

### 2.5 Verify live domains

Cost: minimal. One HTTP call per row.

Before any enrichment, verify that the domain responds. Dead rows exit the conditional run.

Why: real spot check, 20% of the domains in a sample were dead or non-existent.

Saving: 100-200 actions saved.

Critical: yes.

### 3. Site scan

Cost: high. The bulk of the spend, 4-6 actions per live row.

One scan agent per row, a single pass, compact JSON output. The exact prompt and its rules are
in `assets/clay/site-scan-prompt.md`.

Rules:
- Test on 5-10 rows before scaling.
- Use a cheap model.
- Run conditionally, only on valid domains.
- Keep existing results, do not overwrite them.

Real output: 5 scan batches across roughly 110 live rows.

### 4. Score

Cost: free.

Calculate the score with a formula over the JSON fields the scan produced. Do not delegate
scoring to the model. Formula in `policies/02-scoring.md`.

Critical: yes.

Why: corrective rule from day 6. Leaving the score to the model undervalued an important
account. Since then the model extracts the facts and the formula assigns the points.

### 5. Selective further research (stakeholder phase)

Cost: medium, 10-15 actions per row. Only for accounts at or above `further_research_threshold`
(reference default: 7).

Only for accounts above threshold: a second pass to identify the buying group (owner,
operational owner, actual user) from the about-us pages and web research, verifying that the
person is still current.

Forbidden: enrichment "because it might be useful."

This step absorbs the routine originally run separately as stakeholder discovery. Its detail
follows.

**Trigger:** event. An account at or above `further_research_threshold` enters batch
preparation.

**Frequency:** per_batch.

**Binding lesson (day 7 run):** in micro-enterprise verticals, people search on professional
social networks is close to useless. 3 searches out of 4 returned zero contacts. People are on
websites, not on social media. Do not spend on people search below roughly 10 declared
employees.

**Prerequisites:** account scored, domain live.

**Inputs:** domain, about-us and contact pages, footer, category directory.

**Sub-steps:**

1. **Site.** Extract names, roles and plaintext emails from the about-us, contacts and footer
   pages. Cost: low.
2. **Registries.** Verify the owner and legal form on registries and category directories.
   Cost: low.
3. **Buying group.** Identify up to three roles: economic sponsor, operational owner, actual
   user or data contact. If they do not emerge, state that rather than guessing.
4. **Channel.** Choose the channel according to real availability: a public named contact, a
   department mailbox, a generic mailbox, certified mail, phone (`stakeholder_preference_order`
   sets the canonical order). If only a web form exists, the account is not contactable by
   email.
5. **Facts vs hypotheses.** Explicitly separate what has a URL source from what is inferred.
   Every email is marked: publicly verified, publicly obfuscated, likely unverified, or not
   found. Critical: yes.
6. **Multiplier signals.** Flag separately the accounts that are not only prospects but
   possible channels (association roles, partners of other accounts in the pipeline). These
   exit the automatic batch; the founder decides them.

**Tools:** web research (read); the enrichment connector (read), a few targeted searches, zero
paid enrichment if the site is enough.

**Outputs:** a people record per account, email with status, first-touch channel, facts
separated from hypotheses.

**Approval policy:** notify, required if it involves spend.

**State updates:** Stakeholder.*

**Failure policy:** an email not found is a legitimate outcome, flag it and consider a form or
phone. Never construct an address by analogy.

**Idempotency strategy:** one record per account per run, dated. Later runs update, they do not
duplicate.

**Success metrics:** share of accounts with at least one usable channel; share of emails with
a URL source.

**Real output (day 7 run):**

- Accounts worked: 10.
- Gaps closed: 2.
- Public emails found: 5.
- Emails not found: 5.
- Cost: 4 searches, zero paid enrichment.
- Multiplier signals found: 2.

### 6. Output

Export the scored CSV to the workspace, produce the summary with the top N, package the
batches with a per-account brief and drafts on the approved template. Update the CRM
(`crm_system`) only for accounts that actually enter a batch, not for the whole universe.

Gate: explicit founder approval on the top N (`list_approval_required`, reference default:
true) before any send.

## Enrichment discipline

Applies wherever a step above uses the enrichment connector or the enrichment platform.

**The four-step flow:**

1. **Search / Find.** Returns a task identifier and the base fields. Parameters: always
   domains, never bare company names. Few people per company (2-4). Up to 10 domains per call.
2. **Enrich.** Add data points on that identifier. Standard: email, professional history,
   public presence. Custom: any research question.
3. **Poll.** Enrichment is asynchronous. Never conclude without re-reading the task's context.
   No result is a definitive outcome, not an error: register it and plan the fallback.
4. **Never invent.** Never declare that a data point does not exist without having polled.
   Never invent values.

**Budget discipline (seven rules):**

1. Filter before you enrich. A row out of ICP must never reach a paid step.
2. Verify live domains before the scan. In the real sample, 20% were dead: the check saved
   100-200 actions.
3. Test small. New prompt: first 5-10 rows, check the output, then scale.
4. Deduplicate on domain or on profile, before the spend.
5. Enrich only the fields that will actually be used. If the channel is phone, email is not
   needed.
6. One run, one written objective. If you cannot write the objective, the run does not happen.
7. Further research only above `further_research_threshold` (reference default: 7). Enriching
   "because it might be useful" is forbidden.

**Budget planning:**

Declare and get founder approval for a budget before every run (`enrichment_spend_approval`).
Fill in a copy of the table below per run; keep the filled copies under `assets/clay/` as the
persistent planning record.

| Line item | Estimated actions |
|---|---|
| Sourcing and normalization | |
| Site scan | |
| Further research on the top 30 | |
| Reserve for pre-call research and responders | |

Compare the filled total against the enrichment credits actually available before starting the
run.

When enrichment credits for the period run out, there is no cascade verification of email or
phone numbers: the run continues on scan actions and public data only. Declare this constraint
before the run starts, not partway through.

Consequence to keep in mind: an address found publicly can be used as a public contact, but it
is not a verified address. Do not call it one.

## Tools

- `enrichment_platform` (read). Tables, not the connector, above roughly 20 rows.
- `enrichment_platform` (read). Only ad-hoc research, from 1 to 20 rows.
- `web_research` (read).
- `file_tools` (read, write).

## Outputs

- CSV of the scored universe with funnel counts.
- Top-N summary with evidence, email, angle and reservations.
- Batches ready for the queue.
- From the stakeholder phase: a people record per account, email with status, first-touch
  channel, facts separated from hypotheses.

## Approval policy

Required on the actions budget beforehand, and on the top N afterward. Notify for the
stakeholder phase, required if it involves spend.

## State updates

Account, Experiment.approved_by_founder, Stakeholder.*

## Failure policy

An unverifiable data point is written as n/a and flagged. Never infer numbers, offices or
unpublished software. No result is a definitive outcome: it is registered and a fallback is
planned. An email not found is also a legitimate outcome: flag it and consider a form or
phone. Never construct an address by analogy.

## Idempotency strategy

Deduplicate on domain. The suppression table prevents rework on accounts already touched.
Existing scan results are not overwritten. For the stakeholder phase: one record per account
per run, dated; later runs update, they do not duplicate.

## Success metrics

- Share of rows still live after the domain check.
- Share of accounts with a citable fact.
- Share of public emails found.
- Actions spent per account that actually entered a batch.
- Share of accounts with at least one usable channel.
- Share of emails with a URL source.

## Real funnel (day 7 run)

| Stage | Count |
|---|---|
| Sourced | 152 |
| Live | 139 |
| In ICP | 43 |
| Borderline | 46 |
| Out of ICP | 50 |
| Shortlisted | 30 |
| Entered a batch | 9 |
| Meetings generated | 4 |

## Design note

The most underrated step is 2.5, verifying live domains. It costs almost nothing and protects
the most expensive step. The second most underrated is step 2, the suppression table: without
it, the system re-contacts accounts already worked and burns warm relationships.
