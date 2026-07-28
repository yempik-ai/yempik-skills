# Learning delta: authoring template

A learning delta is one proposed change to the company's durable knowledge, written by the
agent and reviewed by a human. It is prose in a fixed shape, not a record in a database.

The private pack modelled this as a `LearningCandidate` JSON object with a `status` field.
That object is gone. It was never populated with real data, and a schema implies a store that
does not exist here: the platform's Inbox is the store. **Candidate status is implicit.**
Every proposal lands in the review Inbox as a candidate and nothing else; there is no state to
set, no `candidate` value to write, and no way for the agent to promote its own proposal. A
candidate is not a decision until a human ratifies it.

Use this template as the body of a Brain proposal. Fill every section. A section you cannot
fill is the finding: say so in one line rather than deleting the heading.

---

## The template

```markdown
## Statement

One actionable sentence. Present tense, specific, falsifiable.
Not "follow-ups seem to help" but "three of the four conversions arrived on the second touch".

## Kind

One of: rule | heuristic | preference | hypothesis | correction

- `rule`: deterministic, no judgement at execution time.
- `heuristic`: a judgement call that held up more often than not.
- `preference`: a company choice, defensible but not derived from evidence.
- `hypothesis`: stated, not yet validated.
- `correction`: comes from a human editing or reversing the agent's output.
  A correction outranks everything else in this list and is never filed as a hypothesis.

## Origin

One of: founder_correction | reply_pattern | call_objection | failed_assumption |
conflict_between_sources

## Evidence

Quote the evidence inline. Every quotation carries its source reference and its date.
A paraphrase is not evidence: paraphrase is how an observation becomes a claim.

> "quoted text, exactly as written"
> Source: thread or file reference. Date: <date>.

List one block per piece of evidence. At least one block is required.

## Sample size

The number of distinct cases behind the statement, as an integer, plus what one case means
here (one account, one reply, one call).

If the sample is below the `min_sample_size_for_rule` slot (reference default: 30), state it
in this section. Below that threshold the delta may not be proposed as a `rule`, whatever the
evidence looks like. A single case never becomes a rule.

## Contradicts

Existing rules, decisions or defaults this delta would call into question. Name them.
An empty list is a real answer; "none found" is not the same as "did not look".

## Proposed change

What should change and where: which policy, which configuration slot, which default value.
Write the replacement text, not a description of it. A reviewer should be able to accept or
reject without rewriting the delta.
```

---

## Confidence

The proposal carries a numeric confidence. Do not invent a value: map the qualitative level
to the number below and keep the level word in the statement so the mapping stays auditable.

| Level | Confidence | When it applies |
|---|---|---|
| `single_case` | `0.2` | One case. Enough to record, never enough to generalise. |
| `weak` | `0.4` | A repeated pattern with an obvious alternative explanation. |
| `moderate` | `0.65` | Consistent across cases, no contradicting case found, sample still small. |
| `strong` | `0.85` | Consistent, corroborated by a second source, and it survived an attempt to break it. |

Confidence never reaches 1.0. The reference motion produced 4 meetings from 26 accounts over
two weeks: at those volumes nothing is proved, and a delta that claims certainty is a defect,
not a strong finding.

## What happens next

1. The agent proposes. The proposal is a candidate in the Inbox, with no external effect.
2. A human reviews, edits or rejects it. Only a human moves a candidate to ratified.
3. Once ratified, the delta is active truth and the agent may cite it.

The agent never skips step 2, never treats its own proposal as ratified, and never re-proposes
the same statement to force a decision. If a proposal has been pending for a while, that is a
fact to report in the brief, not a reason to propose again.
