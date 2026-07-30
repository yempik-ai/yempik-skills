# Stage 2 · Consensus map

Write the median answers down before generating anything else. Not thought about: written,
as full sentences, in the output of this stage. An unwritten consensus cannot be banned in
stage 3 and cannot be quoted in stage 5, and a model asked for "something non-obvious"
without an explicit list of the obvious reliably returns the obvious with more adjectives.

## Procedure

**1. Produce roughly five entries.** Five is the working number: four leaves the median
under-described, seven starts inventing consensus nobody holds. Each entry is one declarative
sentence stating what the market, the industry press, a competent consultant and the model's
own first instinct would all answer for this domain.

**2. Write them as claims, not topics.** "AI adoption" is a topic and bans nothing. "The way
to use AI here is to bolt an assistant onto the existing workflow and measure time saved" is
a claim, and stage 3 can be held to avoiding it.

**3. Include the model's own first answers.** Before the denial pass has any teeth, generate
your own immediate three or four ideas for the prompt and put them on this list. They are by
definition the typicality-weighted output, and leaving them off means banning everyone else's
median while keeping your own.

**4. Do not evaluate them.** Some consensus is correct. This stage is not judging the
entries, it is naming them so that agreement with them is a deliberate choice rather than a
default. A thesis is allowed to end up agreeing with consensus; it is not allowed to do so
by accident.

## The two uses

**As the denylist for stage 3.** `references/divergence.md` forbids every entry here in its
denial pass. The ban covers restatements: if a later idea says the same thing with different
vocabulary, a narrower scope, or one extra qualifier, it counts as banned and is dropped.
Test it by stripping the phrasing: reduce the candidate to its operative claim and compare
that against the entries, not the wording. (Fixation is measurable, not hypothetical: ideas
generated after an anchor stay anchored to it, which is why the anchor must be named and
excluded explicitly rather than merely avoided: Deng, Brucks and Toubia 2026.)

**As the `consensus` field of every thesis.** The output contract in
`references/output-contract.md` requires each thesis to state what consensus believes
instead. That field is filled from this map, unedited except for grammar. A thesis whose
`consensus` field does not correspond to any entry here means either the map was incomplete
or the field was written to flatter the thesis. Both are stage-2 defects, and both are fixed
here rather than in the output.

## Output shape

```
Consensus map · <domain> · <n> entries
1. <declarative sentence>
2. <declarative sentence>
...
```

Keep it in context for the rest of the run. Every subsequent stage reads it, and regenerating
it later produces a different map, which quietly invalidates the bans stage 3 already applied.
