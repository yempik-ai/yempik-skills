# Stage 5 · Output contract

Three to five theses. Not twenty, not "here are the ones that survived plus some honourable
mentions". The cap is the deliverable's whole point, because handing back a long list returns
the filtering work the user wanted done. If stage 4 left more than five survivors, rank by how
much the grounding actually says and drop the rest; if it left fewer than three, ship what
survived and say so rather than reviving deaths to hit a number.

## Thesis fields

Exactly these six, every thesis, in this order. No extra fields, no missing ones.

| Field | Content |
|---|---|
| `claim` | One sentence, contrarian, stated as a position and not as a question |
| `consensus` | What consensus believes instead, taken from the stage-2 map |
| `grounding` | The Brain item, entity or decision ids from stage 4, each with one line on its relevance, or the `UNGROUNDED` label below |
| `cheapest_test` | One action, runnable in a week or less, with the observable signal that decides it |
| `risk_if_wrong` | One sentence on what this costs if the claim is false |
| `type` | `market-contrarian` or `internal-contrarian` |

```
claim: <one contrarian sentence>
consensus: <the median belief this contradicts, from the consensus map>
grounding:
  - <id>: <one line on why this item supports the claim>
  - <id>: <one line>
cheapest_test: <one action, ≤ 1 week> → signal: <what you would observe>
risk_if_wrong: <one sentence>
type: market-contrarian | internal-contrarian
```

Field notes that decide whether the artefact is usable:

- **`claim`** is a bet someone could disagree with. A claim nobody would argue against is a
  restatement of consensus that escaped stage 3.
- **`consensus`** comes from `references/consensus-map.md` unedited except for grammar. Writing
  a weaker consensus than the one on the map makes the thesis look braver than it is.
- **`grounding`** carries ids returned by tool calls in this session, nothing else. Citation
  integrity is a red line, defined in `references/grounding.md`.
- **`cheapest_test`** names the observable signal, not the intention to observe. "Talk to three
  clients" is not a test; "ask three clients in this segment to name their current workaround,
  and see whether two or more describe the same one" is.
- **`risk_if_wrong`** is what breaks, concretely. Not "we lose time".
- **`type`** is `internal-contrarian` exactly when the thesis was promoted from a
  contradicted active decision, and that decision's id belongs in `grounding`.

## The `UNGROUNDED` label

The label belongs to a thesis, not to a run. A thesis carries it when stage 4 left one or more
of its load-bearing sub-claims without a relevant citation, whether because
`references/readiness.md` classified the domain `blind` or `thin` or because the checks came
back empty on a covered domain. Then the `grounding` field carries this literal text in place of
citations:

```
UNGROUNDED: Brain coverage on this domain is <blind|thin>
```

Verbatim, with the actual level substituted. Never both a label and citations, never a softer
wording, never buried in a closing caveat. State once, in the reply around the theses, why the
difference matters: a labeled thesis survived no check, so its failure rate is unknown, while a
grounded one has already been tested against what the company decided and recorded.

A thesis whose every load-bearing sub-claim earned a relevant, session-returned citation in
stage 4 meets the `supported` bar and ships grounded, with its ids, even when the stage-1 probe
called the domain `blind` or `thin`: the probe is an estimate of coverage and stage 4 is the
measurement, so for the thesis it measured the measurement decides. Every other thesis in the
same run carries the label. "Never both a label and citations" is a rule about one thesis, so it
is never grounds for stripping earned citations because a neighbouring thesis has none, and
never grounds for rounding a whole run up. The readiness report to the user still states the
run-level class, exactly as stage 1 computed it.

## The outlet

A surviving thesis can become a candidate in the Brain for human review. **Default off, one
approval per thesis, and the approval must be given after the thesis exists.** Ask plainly,
naming the thesis; a blanket yes collected in advance authorises nothing, and silence
authorises nothing.

On an explicit yes:

```
brain_open_changeset      → get changeset_id
brain_propose_item        → pass changeset_id, fresh UUID request_id per write
brain_submit_changeset    → submit for human review
brain_get_proposal_status → confirm the outcome
```

Every write takes its own freshly generated UUID `request_id`, which makes retries idempotent
rather than duplicative. Proposing is low-risk by construction: it creates a candidate in the
review Inbox, never active truth, with no external effect. That is exactly why it still needs
the user's yes: the cost of a bad proposal is not the write, it is the reviewer's attention
and a Brain filling with unratified theses.

Never propose a thesis the user did not approve, never propose the death log, and never treat
approval of one thesis as approval of the batch.
