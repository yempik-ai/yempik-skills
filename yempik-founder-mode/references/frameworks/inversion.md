# Framework · Inversion

## What it finds

Failure paths that are not hypothetical. Asking how to succeed produces the median plan;
asking how the goal provably fails produces a short list of concrete mechanisms, and the
Brain then says which of them are already in motion. A failure path with recorded evidence
behind it is the strongest thesis this pack produces, because the contrarian claim is not a
prediction. It is a diagnosis the company's own records already support.

## Mandatory Brain inputs

| Input | Tool call | When it comes back empty |
|---|---|---|
| Rules governing the domain | `brain_search` for rules, policies and "we always / we never" statements on the domain | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |
| Constraint-type facts on the domain | `brain_search` for recorded limits, capacities, dependencies and known frictions | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |

The framework's whole value is the cross-check in step 3. Without rules and constraint facts
there is nothing to cross-check against, and every failure path stays equally speculative,
which is a list of worries, not theses. Skip it or label it per
`references/output-contract.md`.

## Procedure

**1. State the goal in one sentence, in the company's terms.** Not an aspiration: something
that can be observed to have failed. "Grow the segment" cannot fail observably; "reach a
second repeat order from the same buyer within a quarter" can.

**2. Enumerate the concrete ways it provably fails.** Six to ten, each a mechanism rather than
a risk word.

```
Goal: <the one-sentence goal>
List 6-10 mechanisms by which this goal fails. Each must name what happens, in what order, and
what makes it irreversible. Ban the words "risk", "challenge" and "if we do not execute well".
```

A mechanism is testable; "poor execution" is not, and its presence on the list means the
enumeration stopped early.

**3. Cross-check each path against the record.** Per failure path:

```
brain_search: "<the mechanism's operative terms>"
brain_search: "<the constraint the mechanism exploits>"
```

Sort into: *live* (recorded facts or rules show the mechanism is already operating, at least
partially); *dormant* (plausible, nothing recorded); *blocked* (a rule or recorded constraint
already prevents it). Only *live* paths continue. Dormant paths are not theses, they are
speculation, and mixing them in dilutes the ones with evidence. Blocked paths are worth one
line to the user: a rule doing real work is worth knowing about.

**4. Invert the live paths.** The thesis is the action that removes or defuses the mechanism,
stated as a position rather than a mitigation plan. The `consensus` field is what the market
does instead, almost always adding effort at the goal rather than removing the mechanism
working against it. The `grounding` field carries the ids showing the mechanism is live.

**5. Keep the diagnosis inside the claim.** A claim that reads as generic prudence has lost the
framework's contribution. It must name the mechanism, because that is what makes it arguable
and what makes `cheapest_test` obvious: the test is usually "measure whether the mechanism is
operating at the rate the records imply".

## Worked shape

*Fictional throughout: "Verdana Kilns" does not exist, and neither do the ids below.*

```
Goal: Verdana Kilns wants half of new studio customers to reorder consumables within 90 days.
Failure mechanism 4: the first firing goes wrong, the customer blames the kiln rather than the
  clay body, and reorders stop before the second attempt.
brain_search "first firing support" → KB-3310 (fact): 40% of first-90-day support tickets are
  first-firing failures; KB-3318 (rule): support does not advise on materials, only on hardware.
Status: live. The mechanism is recorded, and the rule guarantees the misattribution goes
  uncorrected.

claim: Verdana should own the first firing end to end, materials included, because the reorder
  is lost at the moment a hardware-only support rule hands the customer a wrong explanation.
consensus: Reorder rate is a marketing and pricing problem, addressed with reminders and bundles.
grounding:
  - KB-3310: 40% of early support tickets are first-firing failures
  - KB-3318: support is scoped to hardware, so the failure is never attributed correctly
cheapest_test: take the next ten first firings through a guided session covering the clay body
  → signal: whether the failure rate in that cohort drops below the recorded 40%
risk_if_wrong: support time doubles on a cohort that would have reordered anyway
type: market-contrarian
```
