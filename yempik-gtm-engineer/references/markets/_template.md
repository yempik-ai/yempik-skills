# Market configuration: worksheet

Copy this file to `references/markets/<market>.md` and fill it in before the first sourcing
run. Everything here is **market configuration**: it is rewritten per sector, not per company.
Company configuration lives in `references/configuration.md`; language configuration lives in
`references/languages/`.

Nothing in this file is universal. The universal parts of the same subjects are already
stated elsewhere and are only cross-referenced here:

| Universal | Where it lives |
|---|---|
| A closed angle set exists and the choice from it is deterministic | `doctrine.md` E2 |
| The specific fact in the first line | `doctrine.md` E1 |
| Six scoring dimensions with non-uniform weights, total 0-12, pilotability heaviest at 0-3 | `policies/02-scoring.md` |
| Spot-check the market before scoring the universe | `policies/02-scoring.md` |

**The most expensive thing to regenerate is not the copy: it is the scoring proxies.** They
require looking at 100 or more sites in the sector to understand what it publishes and what
it hides. Budget for that before budgeting for messages.

The worked examples throughout are the reference market, anonymized: small and mid-size
operators managing residential property portfolios on behalf of owners, in two regions,
sourced from public websites. They are one motion of 26 accounts. They are here to show the
shape of a filled-in answer, not to be reused.

---

## 1. Segments (`segment_definitions`)

**What to decide.** An ordered list of segments. The order is the work sequence, not a
taxonomy: the first segment is worked first.

**How to derive it.** Group by how the buying decision is structured, not by size alone. Two
accounts of the same size with different decision structures belong in different segments.

**Worked example.** Four ordered segments: centralised enterprise operators; networks and
franchises; structured regional operators; adjacent ecosystem.

**Market vocabulary.** Not a configuration slot, but decide it here and hand it to the active
language adapter: the market's own word for an account, and its own word for the unit a pilot
runs on. In the reference market these were the practice and a single building. Copy that
uses the market's noun reads as written by someone inside it.

Consumed by: `schemas/account.schema.json` (`segment_id`) · `state-machine.yaml`
(`segmentation`).

---

## 2. Sources

**What to decide.** Where the raw universe comes from, and which of those sources is
authoritative for which fact.

**How to derive it.** List the public sources the sector actually maintains. For each, state
what it is reliable for.

**Worked example.** Account websites and company registries. Registry figures were treated as
unreliable on their own: two accounts showed declared revenue incompatible with the declared
portfolio and with the declared headcount. Both were recorded as contradictions and neither
was resolved.

**Binding rule, universal:** conflicts between sources are flagged, never resolved in
silence (`schemas/account.schema.json`, `contradictions`).

Consumed by: `routines/universe-sourcing.md`.

---

## 3. Scoring proxies (`scoring_proxies`)

**What to decide.** The observable facts that stand in for each of the six scoring dimensions
in this market.

**How to derive it.**

1. Take the six dimensions from `policies/02-scoring.md`. Do not change them and do not
   change their weights: they are universal.
2. Run a spot-check on `spot_check_sample_size` sites (reference default: 20) **before**
   scoring the universe.
3. For each dimension, write down what the sample actually publishes. A dimension whose
   evidence is not published is unusable no matter how useful it would be.
4. Replace every unusable dimension with proxies drawn from what is published.
5. Record the negative signals too: the observable facts that reliably put an account out of
   ICP.

**Worked example.** The spot-check found that **0 out of 20** sites declared their
managed-unit count, so the "declared scale" dimension was unusable as designed. The
replacement proxies, all observable from the site:

- corporate form (structured company versus sole practitioner);
- a team with distinct roles, or department mailboxes;
- number of offices;
- declared years in business;
- presence of a portal or a reserved area;
- affiliation with a <TRADE-ASSOCIATION>;
- site quality (professionally built versus a free site-builder).

Negative signal: a footer signed with a single personal name almost always indicated a sole
practitioner, i.e. out of ICP.

> Note on the count: the portability table calls these "the six scoring proxies" (scale,
> structure, offices, incumbent system, contactability, ICP fit), while the list the reference
> market actually re-derived has seven entries. The discrepancy is in the source and is left
> as found. What matters for a new market is the derivation, not the count.

**Priority bands (`priority_bands`).** Re-derive the cut-offs against the new market's score
distribution; the reference bands are `9-12 -> A`, `7-8 -> B`, `5-6 -> C` (only with a strong
dynamic signal), `<5 -> not now`. Spend on identifying the buying group starts at
`further_research_threshold` (reference default: 7).

**Carry the counter-evidence forward.** The score orders the queue and makes the order
defensible. It does not predict the reply: two 10/12 accounts never replied, a 9/12 account
converted in 38 minutes, and the account that converted best was never in the scored universe
at all. A new market's proxies will be no better at prediction.

Consumed by: `policies/02-scoring.md` · `assets/clay/scoring-formula.md`.

---

## 4. Qualifying signals (`signal_types`)

**What to decide.** The closed set of signal classes that justify contacting an account in
this market.

**How to derive it.** A signal is a fact that is (a) observable from a public source, (b)
citable in a first line with a `source_url`, and (c) operationally consequential. A fact that
fails any of the three is not a signal. Without a signal there is no outreach: doctrine E1.

**Worked example.** Seven: published method · multiple offices · named incumbent system ·
declared volume · customer portal · existing engagement · verbalised pain.

Consumed by: `policies/03-stakeholder-and-angle.md` · `schemas/account.schema.json`
(`signal.type`).

---

## 5. Angle set (`angle_set`)

**What to decide.** The closed set of message framings.

**How to derive it.** Angles come from the sector's operational pain, not from the product's
feature list. Keep the set small: four angles over 26 accounts still allow learning which one
works, 26 angles allow none, because every email becomes a single-case experiment.

Angle identifiers are vendor-neutral. If an angle exists because a named incumbent product is
common in the market, the identifier still names the move, not the vendor.

**Worked example.** Four, closed:

| Angle id | Framing |
|---|---|
| `continuity_across_offices` | Continuity of work across multiple offices |
| `replace_ecosystem` | Replace the incumbent system rather than adding tools around it |
| `workflow_ownership` | Take ownership of the workflow end to end |
| `published_method` | Engage with the operational method the account publishes |

Consumed by: `policies/03-stakeholder-and-angle.md` · `schemas/account.schema.json`
(`angle_id`).

---

## 6. Signal-to-angle mapping (`signal_to_angle_map`)

**What to decide.** A deterministic mapping from signal class to angle, plus a tie-break
order for accounts carrying more than one signal.

**How to derive it.** One angle per signal class. Every signal class in §4 maps to exactly one
angle in §5, or the class does not belong in §4. Where signals coexist, the one most specific
to the account wins. An account with no mapped signal returns to `research`; it is not
contacted with a generic message.

**Worked example.**

```
if signal.type == published_method            -> angle = published_method
elif signal.type == named_incumbent_system    -> angle = replace_ecosystem
elif signal.type == multiple_offices          -> angle = continuity_across_offices
elif signal.type in (declared_volume,
                     customer_portal)         -> angle = workflow_ownership
else                                          -> no angle, return to research
```

Tie-break order, most specific first: a published method beats a named incumbent system,
which beats the number of offices, which beats volume.

In the reference market, `named_incumbent_system` was triggered by INCUMBENT-SOFTWARE-1 or
INCUMBENT-SOFTWARE-2 appearing on the account's site. The vendor names are the observation;
they never enter the angle identifier.

Result: 4 angles across 26 accounts, none invented ad hoc.

Consumed by: `doctrine.md` E2 · `policies/03-stakeholder-and-angle.md`.

---

## 7. Mandatory discovery questions (`mandatory_discovery_questions`)

**What to decide.** The questions that must be asked on every discovery call in this market.

**How to derive it.** Write them against the operational process being sold into, not against
the product. Each question exists to establish one qualification criterion
(`qualification_criteria`), and a question that establishes nothing is dropped.

**Worked example.** The four themes the reference market required: the workflow, where the
source of truth lives, which system is currently in use, which unit can be isolated for the
test. The reference motion's full question set is in `routines/discovery-call-prep.md`
step 3.

Consumed by: `routines/discovery-call-prep.md`.

---

## 8. Objection taxonomy

**What to decide.** The recurring objections in this market, each with the honest answer.

**How to derive it.** Do not write it in advance. Populate it after the first 5 calls, from
what was actually said. Until then the field is empty, and an empty field is a correct state.

Every objection is then tested against doctrine E8: does it block the first test on a single
unit, or only adoption at full scale? The two resolve on different timescales, and confusing
them disqualified the largest account in the reference pipeline.

**Worked example (three observed).** Integration with a closed incumbent system; privacy and
data protection; an AI capability already present in the current system. Three objections from
two calls held: too few to be a taxonomy, recorded because they were the ones that occurred.

Consumed by: `policies/05-reply-handling.md`.

---

## 9. Completion check

The market configuration is complete when:

- [ ] Segments are listed **in work order**.
- [ ] Every source is paired with what it is authoritative for.
- [ ] The spot-check has been run and its findings are written down, including the
      dimensions that turned out to be unusable.
- [ ] Every scoring dimension has at least one observable proxy, or is explicitly recorded as
      unscoreable in this market.
- [ ] Negative signals are listed.
- [ ] Every signal class maps to exactly one angle, and the tie-break order is written.
- [ ] Every discovery question is traceable to a qualification criterion.
- [ ] The objection taxonomy is empty and dated, waiting for the first 5 calls.

An installer who fills sections 5 and 7 but skips section 3 has configured the copy and left
the expensive part undone.
