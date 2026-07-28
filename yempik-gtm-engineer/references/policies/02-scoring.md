# Policy 02: Scoring

> **Corrected on day 18.** The previous version of this file contained a derived formula (six
> criteria x 0-2). It was wrong. This is the actual formula, taken from the scoring-rule file
> (day 6) and the day 7 runbook.

## Actual formula

Six dimensions, **non-uniform** weights, total 0-12.

| Dimension | Range | Evidence required |
|---|---:|---|
| Scale and complexity | 0-2 | portfolio, units, team, offices or network |
| Centralisation | 0-2 | central processes and services, specialised teams, distinct roles |
| Evidence of an existing system | 0-2 | a **named** software product or a fragmented stack, never assumptions |
| **Pilotability** | **0-3** | an isolable unit, a sponsor, a user and available data |
| Decision access | 0-2 | an identified and reachable buying group |
| Change signal | 0-1 | acquisition, new office, hiring, recent reorganisation |

Configuration: `scoring_weights` (reference default: the six weights above).

**Pilotability outweighs everything else** (0-3): it is the only dimension that says whether a
test is materially possible. A large, centralised account that cannot be piloted is worth less
than a small one where the test can happen tomorrow. This is the single most transferable piece
of the formula: in any validation motion, the heaviest weight goes to "can you actually test
here."

## Reference market example

*The section below is market-specific: the priority bands and the scoring proxies must be
re-derived for each new market. It ships here only as a worked reference example and is flagged
for extraction into `references/markets/_template.md`; do not treat it as universal policy.*

### Priority bands

```
9-12  -> priority A, worked first
7-8   -> priority B, worked after A
5-6   -> priority C, only with a strong dynamic signal
<5    -> not now, or competitive intelligence only
```

Configuration: `priority_bands` (reference default: the four bands above).

### Correction applied after the first spot-check (day 7)

Check on 20 sites in the sample: **0 out of 20 declared their managed-unit count**. The
"declared scale" dimension was therefore unusable as designed.

Replacement proxies adopted, all observable from the site:

- corporate form (structured company versus sole practitioner);
- a team with distinct roles, or department mailboxes;
- number of offices;
- declared years in business;
- presence of a portal or a reserved area;
- affiliation with a trade association;
- site quality (professionally built versus a free site-builder).

**Strong negative signal:** a footer signed "di [First name] [Last name]" (this market's
personal-signature pattern) almost always indicates a sole practitioner, i.e. out of ICP.

Configuration: `scoring_proxies` (reference default: the seven proxies above).

## Transferable rule

**Scoring criteria must be calibrated on what that market actually publishes, not on what would
be useful to know.** Run a spot-check on `spot_check_sample_size` sites (reference default: 20)
before scoring the whole universe.

Configuration: `further_research_threshold` (reference default: 7). Below this score, no spend
on identifying the buying group.

## Who computes what

```
model    -> extracts facts from the site, in JSON, without inventing
formula  -> assigns points to the JSON fields
human    -> approves the list before every send
```

Corrective rule from day 6: when scoring was left to the model, an important account was
undervalued. Since then, assigning points is never delegated.

## What it is not for

The score orders the queue and makes the order defensible. **It does not predict the reply.**
Counter-evidence from real data:

| Account | Score | Outcome |
|---|---|---|
| ACCOUNT-K | 10/12 | no reply |
| ACCOUNT-L | 10/12 | no reply |
| ACCOUNT-C | 9/12 | positive reply in 38 minutes |
| ACCOUNT-A | not scored | pilot agreed verbally |

If the founder asks "who will reply," the correct answer is that the score does not know. And
the ACCOUNT-A case says something further: **the account with the best conversion was not in
the scored universe.** Static fit is not enough; a dynamic signal is required.
