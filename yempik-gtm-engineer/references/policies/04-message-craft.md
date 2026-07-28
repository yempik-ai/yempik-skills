# Policy 04 · Message Craft

## Personalisation: the first-line rule

**Mandatory first-touch format:**

```
I am writing because [ACCOUNT] [SPECIFIC VERIFIABLE FACT]: this is a context in which
[OPERATIONAL CONSEQUENCE OF THE FACT].
```

The exact opening register (for example, an Italian formal address) is a
language-specific rule; see `languages/it.md`.

The FACT must have a `source_url`. The CONSEQUENCE is the only place where the agent
interprets, and it must stay at the operational level, not the emotional one.

**Reference example (this market).** "ACCOUNT-C manages approximately 90 managed units
across three offices in <CITY-1>: this is a context in which continuity of work across
offices matters more than in a single-office practice."

**Forbidden:** any compliment about the website, mission, history, or professionalism.
This is decorative personalisation, and it is indistinguishable from spam.

## Full first-touch structure (5 blocks, fixed order)

1. Specific reason with the account's own data point.
2. Product thesis, with the tracked product link (`tracked_link_policy`) at the first
   mention of the product name (`product_name`).
3. Strategic direction ("replace the incumbent system, do not add tools").
4. Offer of a controlled test, run in parallel, with no risk to data or operations.
5. Single CTA.

## CTA

CTA wording is `cta_wording` (reference default: "a 25-minute call"). Cap:
`cta_count_per_message = 1` (hard constraint, universal, not market-specific).

Observed pattern (reference motion): a direct question stating the CTA, followed by one
sentence on what the call covers and why it might be relevant to the account. The exact
wording belongs to `languages/it.md`.

When the prospect proposes a date and time, accept or confirm within the hour, with no
counter-proposals (doctrine E4). ACCOUNT-D and ACCOUNT-C: both confirmed within 20
minutes.

## Follow-up

```
if days_since_first_touch >= followup_window_days and no_reply and touch_count_email < touch_cap_per_account:
    prepare a single follow-up (followup_count), standard text, same CTA
if touch_count_email == touch_cap_per_account:
    email channel exhausted -> propose phone or close, do NOT send
```

`followup_window_days` (reference default: 4-5 days, `[INFERENCE]`),
`touch_cap_per_account` (reference default: 2), `followup_count` (reference default: 1).
All three from `references/configuration.md` §1.

Observed window: 4-5 days. Standard text, no additional personalisation: a short
reference back to the previous message plus a restatement of the test-cohort framing.
Exact wording belongs to `languages/it.md`.

This is the system's multiplier. 3 out of 4 conversions arrive on the second touch.

## Channel escalation

The agent does not decide the move to phone. It proposes the move and stops; the
decision belongs to `escalation_owner` (reference default: the founder).

Explicit founder rule on ACCOUNT-E: "Phone: the founder decides."
