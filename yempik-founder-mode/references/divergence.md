# Stage 3 · Divergence

Three techniques, run in sequence, each one taking the previous one's output as material to
push against. Target 15 to 20 raw ideas by the end. This is the copiable half of the pack and
it is shipped openly: the techniques are published, the value is that they are run in order
and run completely rather than gestured at.

**Hard rule for the whole stage: no evaluation, no filtering, no feasibility talk.** Not "that
one is unrealistic", not "this would never pass legal", not a quiet omission of the two ideas
that felt embarrassing to write. Filtering while generating re-collapses the distribution to
the median it was just pushed off, which is the one thing this stage exists to prevent.
Judgment is stage 4's job and it needs the full set to do it. An idea that dies in
`references/grounding.md` for a reason you can cite costs one lookup; an idea suppressed here
costs the run its tail.

## Technique 1 · Verbalized sampling

Ask for a distribution instead of an answer. A single "give me ideas" request samples the mode
of the trained distribution; asking for candidates *with* their probabilities exposes the
distribution itself, and the interesting mass is in the tail (the verbalized-sampling result,
Zhang et al.).

Prompt scaffold, run as written:

```
For <domain>, generate 10 or more distinct approaches. For each one, state the probability
that a competent operator asked this question would name it, as an explicit number.
Format: <approach, one sentence> | p=<0.00 to 1.00>
Span the full range. Include low-probability approaches deliberately; a set where every
p is above 0.20 has not been sampled, it has been listed.
```

Then take the median of the stated probabilities and **keep only the entries below it**.
Discard the high-probability half without reading it for quality: those are the median
answers, and stage 2 already wrote them down. Expect 5 to 8 survivors here.

## Technique 2 · Ordinary-persona rotation

Regenerate from at least four mundane vantage points. Each persona is a person with concrete
daily friction and no strategic vocabulary, and each produces ideas the boardroom framing
cannot reach.

```
You are <persona>. You have never used the words "strategy", "leverage" or "positioning".
Describe what you would actually do about <domain>, in the terms your own day is measured in.
```

Examples of the register: a night-shift warehouse operator, a small-town accountant, a
municipal permit clerk, a repair technician who drives between sites. Rotate the set to suit
the domain. The requirement is four or more, mundane, and genuinely different in what their
day rewards.

**Banned: celebrity and genius personas.** No "think like a famous founder", no "as a genius
strategist", no named public figures. They collapse to the stereotype of the person rather
than to any reasoning, and measurably underperform generic personas on diversity
(Deng, Brucks and Toubia 2026). If a persona's output could have been generated from their
public reputation alone, the persona did no work.

Expect 4 to 8 further ideas, and keep duplicates across personas as one entry. Noting which
personas converged is useful input for `references/failure-modes.md`.

## Technique 3 · Denial pass

Regenerate a final time with everything already produced explicitly forbidden: the full
consensus map from `references/consensus-map.md` **and** every idea from techniques 1 and 2.

```
Forbidden (do not restate, narrow, rephrase or qualify any of these):
<the ~5 consensus entries, verbatim>
<every idea generated so far, one line each>
Now produce approaches to <domain> that none of the above covers. If an idea is a variant of
a forbidden entry, discard it and continue. Uncomfortable, small, unglamorous and
operationally awkward ideas are in scope.
```

The ban covers meaning, not wording, and the check is mechanical: reduce each new candidate to
its operative claim and compare that claim against the forbidden list. This pass typically
produces the strangest 3 to 5 ideas of the run, and it is the one most often cut short. Run
it until it genuinely stops producing non-variants, not until the count looks sufficient.

## Handing over

Output the raw set as a flat numbered list, 15 to 20 entries, one sentence each, with no
ranking, no grouping by theme and no commentary on which ones you like. Note beside each which
technique produced it: stage 4 verdict patterns per technique are the cheapest available
signal that a technique is being run badly. Then load `references/grounding.md`.
