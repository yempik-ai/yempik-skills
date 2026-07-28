# Policy 07: Reason codes (the real taxonomy)

> **Added on day 18.** This taxonomy already exists in the source company's system and is
> used by the Friday GTM review. The pack's first draft invented a thinner taxonomy; this
> replaces it.

## Why reason codes matter more than rates

A reply rate tells you **how much** is not working. A reason code tells you **what** to
change. The weekly review chooses a single variable to change, and it chooses it by reading
the distribution of reason codes, not the percentage.

## Taxonomy (11 codes)

| Code | Meaning | What to change |
|---|---|---|
| `pain_not_priority` | The problem is recognised but not urgent. | Segment or timing, not copy. |
| `replacement_too_risky` | Replacing the incumbent system feels dangerous. | Change the offer: shrink the test scope. |
| `pilot_scope_too_large` | The proposed test looks too demanding. | Shrink `first_purchase_scope` (reference default: one real unit, one workflow, running in parallel with the existing system). |
| `no_data_access` | They cannot or will not grant data access. | Verify pilotability earlier. |
| `no_operational_owner` | Nobody would run the test day to day. | Wrong person. |
| `no_budget_owner` | Nobody can authorise spend. | Escalate decision access. |
| `current_software_sufficient` | The current system is good enough. | Possibly the wrong ICP segment. |
| `integration_blocker` | Technical block: integration or migration. | Product, not message. |
| `interested_no_timeline` | Real interest, no timing. | Nurture with a date. |
| `pilot_candidate` | A genuine test candidate. | Accelerate, do not optimise. |
| `partner_only_after_proof` | Willing as a channel, only after proof. | Not a customer. |

## How a code is assigned

- One code per account per cycle: the **dominant** one.
- Always paired with a **literal quotation** from the reply or the call. Without a
  quotation the code is an opinion.
- Silence is not a reason code: record it as `no reply`, which is a fact about the channel,
  not the market.

## Real examples from the observed period

| Account | Code | Quotation |
|---|---|---|
| ACCOUNT-B | ~~`integration_blocker`~~ -> `no_operational_owner` | "the real breakthrough would be direct integration between the incumbent systems" |
| ACCOUNT-I | `interested_no_timeline` | "let's pick this up again in a couple of months" |
| ACCOUNT-J | `current_software_sufficient` | "thank you, but we are not interested" |
| ACCOUNT-A | `pilot_candidate` | "it would sell itself in two seconds" |

## Watch out for the code that looks obvious

The classification of ACCOUNT-B as `integration_blocker` was **wrong**, and the founder
corrected it on day 19. Integration blocks full-scale adoption, not the first test on a
single building: that work is done by hand and was already under way on another account.
The real obstacle was that no **operational owner** had been identified, i.e.
`no_operational_owner`.

Derived rule: when a reason code points to a product limitation, check whether it blocks
the **first test** or **full adoption**. If it only blocks the second, the right code is
almost always a different one, and concerns the people or the access, not the technology.
A wrong technical code is dangerous because it looks objective and closes the account
without appeal.

## The signal that emerges from the distribution

With only 4 codes assigned the distribution is not statistically readable, but
`integration_blocker` appeared **twice** in different forms (ACCOUNT-B explicitly,
ACCOUNT-A as a worry about the initial data import). Two occurrences out of four qualified
conversations indicate a product theme, not a messaging one.

**Derived rule:** when the same reason code appears in two qualified conversations out of
four, it stops being an objection and becomes a roadmap input. This applies to full-scale
adoption. It must **not** stop pilots in the meantime: the one-off manual work is the
bridge that keeps accounts open while the feature is built.
