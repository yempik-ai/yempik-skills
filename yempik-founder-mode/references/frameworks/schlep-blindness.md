# Framework · Schlep blindness

## What it finds

Work the company already judged valuable and then declined because it was tedious, manual or
unscalable. Those rejections are the densest source of non-obvious ideas available, because the
evaluation was already done and only the distaste killed them, and distaste is not a market
signal. The framework's job is to separate the two reasons a decision was reversed, since only
one of them is a reason to leave the idea dead.

## Mandatory Brain inputs

| Input | Tool call | When it comes back empty |
|---|---|---|
| The domain's active decisions, as entry points to their history | `brain_list_items` (type decision, state active), relevance judged from the returned titles and excerpts; no list call exposes non-active states directly | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |
| Each subject's superseded decisions, the recorded reason each was reversed, and what replaced it | `brain_get_current_decision` per subject: it follows the supersede chain, which is the only route to the non-active history | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |

Without recorded reasons the sort in step 2 is guesswork, and guessing why a company rejected
something reads exactly like knowing. Skip the framework or label it per
`references/output-contract.md`. A domain whose decisions were never superseded has no history
to mine and is a legitimate empty result: say so rather than reaching further afield.

## Procedure

**1. Mine the reversals.** Non-active decisions cannot be listed directly (`brain_list_items`
only exposes active and candidate states), so enter through the live side: list the active
decisions, keep the ones relevant to the domain by reading their titles and excerpts, then walk
each subject's supersede chain to reach what was reversed and why.

```
brain_list_items: type = decision, state = active, relevance judged from the results
brain_get_current_decision: "<each relevant subject>", reading the chain it returns,
                            not just the live position
```

A subject whose chain has a single link was never reversed and holds nothing for this
framework; a run where every relevant chain is single-link is the legitimate empty result
described above.

Read the reason as recorded, in the decision's own words. Do not paraphrase it into a cleaner
motive. The paraphrase is where the sort in step 2 goes wrong.

**2. Sort the pile in two.**

- *Rejected because not valuable*: the outcome was judged not worth having, the market was
  absent, the customer did not want it. Leave it dead. Reviving it is contrarianism about an
  answered question.
- *Rejected because tedious, manual, unscalable, unglamorous, or "does not scale"*: the outcome
  was judged worth having and the path to it was judged unpleasant. **This is the candidate
  list.** Phrases to look for in the recorded reason: too manual, too much hand-holding, not
  repeatable, one-off, would need a person on it, no leverage.

When the recorded reason contains both, treat it as tedium: a genuinely worthless outcome rarely
needs the effort argument attached.

**3. Pair each candidate with its smallest non-scalable version.** The thesis is not "revisit
this". It is the unscalable version runnable this week, by hand, at a size where the tedium is
affordable. Name who does it, on how many cases, and for how long. The point of the pairing is
that the original objection was about scale, and a five-case manual run does not have to answer
it.

**4. Write the thesis.** The `claim` states the work, done manually, as the position. The
`consensus` field is the objection that killed it, which is almost always the market's default
belief too: that anything unscalable is not worth doing. The `grounding` field carries the
retired decision id, its recorded reason, and the id of what superseded it. The `cheapest_test`
field is nearly written already: it is the small manual version from step 3, and its signal is
whether the outcome shows up at all at that size.

**5. Do not launder the tedium.** A claim that quietly proposes automating the unpleasant part
has re-run the original rejection and reached the same place. The bet is that doing it by hand
teaches something the automated version cannot, and the claim should say that out loud.

## Worked shape

*Fictional throughout: "Halcyon Translations" does not exist, and neither do the ids below.*

```
Domain: how Halcyon Translations onboards new corporate accounts
brain_list_items (decision, active) → DEC-0501 relevant to the domain: send a glossary
  template for the client to fill in.
brain_get_current_decision "account onboarding" → live: DEC-0501; chain: supersedes DEC-0288,
  build a glossary by hand with each new account before the first delivery. Recorded reason
  for reversal: "two days of linguist time per account, does not scale past ten accounts a
  quarter."
Sort: rejected for tedium. The outcome (an agreed glossary before first delivery) was never
  judged worthless; the two days were.

claim: Halcyon should hand-build the glossary with the client for the highest-value five accounts
  a quarter and stop pretending the template is the same artefact, because the two days buy an
  agreement the client cannot produce alone.
consensus: Anything that costs two days of specialist time per account is not worth doing and
  should be templated.
grounding:
  - DEC-0288: the hand-built glossary, reversed on effort per account, not on value
  - DEC-0501: the live template approach that replaced it
cheapest_test: hand-build with the next five accounts above the value threshold → signal: first
  delivery revision count against the template cohort's recorded average
risk_if_wrong: ten linguist-days spent for a revision count that matches the template cohort
type: internal-contrarian
```

The `internal-contrarian` type follows from contradicting the live `DEC-0501`, per
`references/grounding.md`.
