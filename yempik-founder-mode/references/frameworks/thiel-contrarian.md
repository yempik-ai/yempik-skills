# Framework · Thiel's contrarian question

## What it finds

The gap between what the company says it believes and what it has actually decided. A stated
minority position with no active decision behind it is not a position, it is marketing, and
the gap itself is the thesis, because either the belief is fake or the company is failing to
act on something it already thinks is true. Runs in stage 3 as a generator against stated
positioning, and in stage 4 as a validator that rejects ideas which are consensus with an edge
rather than genuine minority positions.

## Mandatory Brain inputs

| Input | Tool call | When it comes back empty |
|---|---|---|
| The company's active position on the domain | `brain_get_current_decision` on the domain, and on each consensus belief the company appears to reject | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |
| Rules and facts stating the company's thesis or positioning | `brain_search` for positioning, thesis, differentiation and "why we do it this way" in the company's own vocabulary | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |

Both inputs are required, not one of two. Without the decisions there is nothing to check the
stated belief against, and without the stated positioning there is no belief to check. Skipping
is the honest option; labeling per `references/output-contract.md` is the other. Producing a
say-do gap from an empty lookup invents a hypocrisy the company never expressed.

## Procedure

**1. List the market's five consensus beliefs for the domain.** Reuse the stage-2 map from
`references/consensus-map.md` where it overlaps; add beliefs specific to how the market
operates rather than to the prompt.

**2. Ask the question per belief.** For each one:

```
Consensus believes: <belief>
Does the company hold the minority position here, and if so, which active decision is the bet?
brain_get_current_decision: "<the belief's subject, as the company would name it>"
```

**3. Sort each belief into one of three buckets.**

- *Aligned*: the company agrees with consensus, no active decision bets against it. Nothing
  here; it is not a contrarian position and pretending otherwise wastes the run.
- *Bet placed*: a stated minority position with an active decision behind it. Not a thesis
  candidate either, but note the decision id: it is the strongest evidence available for
  grounding neighbouring theses.
- *Say-do gap*: the company states or implies it rejects the belief, and no active decision or
  recorded behaviour bets against it. **This is the thesis candidate.**

**4. Turn each say-do gap into a thesis.** The `claim` is the bet the company is not placing,
stated as a position. The `consensus` field is the belief from step 1. The `grounding` field
carries the positioning item that states the belief plus, where relevant, the absence itself
described precisely, "no active decision on <subject>; `brain_get_current_decision` returned
none", which is a checkable observation, not a citation, and must be worded as such.

**5. Reject consensus-with-an-edge.** As a stage-4 validator, kill any candidate whose claim
would be endorsed by a competent operator on first hearing. The test: would naming this
position publicly cost the company anything with peers or customers? If not, it is the median
in confident phrasing, and it belongs in the death log rather than the output.

## Worked shape

*Fictional throughout: "Northwind Crate Co." does not exist, and neither do the ids below.*

```
Domain: how Northwind Crate Co. sells industrial packaging
Consensus belief 3: buyers in this category choose on unit price, so the lever is cost.
Company's stated positioning (item KB-2201): "we win on failure rate in transit, not price."
brain_get_current_decision "pricing approach" → DEC-0417: match the market on unit price,
  differentiate in the sales conversation.
Bucket: say-do gap. The stated belief rejects price competition; the active decision competes
  on price and pushes the differentiation into conversation, where it is unmeasured.

claim: Northwind should price above the market and sell the failure-rate difference as the
  product, because a differentiator defended only in conversation is one the buyer never pays for.
consensus: Buyers in this category choose on unit price, so the lever is cost.
grounding:
  - KB-2201: states failure rate, not price, as the basis of the company's positioning
  - DEC-0417: the active pricing decision competes on price, contradicting KB-2201
cheapest_test: quote the next five inbound at a premium with the failure-rate claim stated in
  the quote → signal: how many ask for the failure-rate evidence rather than a discount
risk_if_wrong: the premium quotes stall and five weeks of pipeline is lost at the top
type: internal-contrarian
```

The `internal-contrarian` type follows from the contradiction against `DEC-0417`, per the
promotion rule in `references/grounding.md`.
