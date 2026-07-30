# Stage 4 · Brain grounding

The filter, and the half of the pack a copier cannot run. Every raw idea from stage 3 is
broken into the claims it depends on, and each of those claims is checked against the
tenant's governed truth. Ideas do not survive because they are interesting; they survive
because the Brain says something about them.

## Procedure, per idea

**1. Decompose into load-bearing sub-claims.** Two to four per idea. A sub-claim is
load-bearing when the idea collapses if it is false: not a detail, a dependency. Write them
as verifiable statements about the company, its clients, its constraints or its past
decisions, because those are the things the Brain can answer. "Clients would like this" is
not checkable; "clients in this segment have recorded the underlying need" is.

If an idea decomposes into one sub-claim, it is a slogan and needs to be restated concretely
before it can be checked. If it needs six, it is several ideas and should be split.

**2. Check each sub-claim.**

```
brain_search: "<the sub-claim's operative terms, in the company's vocabulary>"
brain_get_current_decision: when the sub-claim asserts or assumes a company position.
                            It follows supersede chains, so it answers "our position now"
                            rather than "what we once decided"
brain_get_entity:  when a specific client, person or process is named
brain_neighbors:   when the sub-claim depends on a relationship: this client's needs,
                   this process's dependants
```

Phrase the `brain_get_current_decision` query the way a decision title reads, a concrete
position on a concrete subject, rather than as an abstract concept: abstract phrasings are the
ones that misrank or error.

Record, per sub-claim, the ids returned and one line on why each is relevant. That line is
what stage 5 ships; reconstructing it later from memory is how fake grounding starts.

**3. Assign the idea a verdict.** One of exactly three:

| Verdict | Condition | Outcome |
|---|---|---|
| `supported` | Every sub-claim has at least one citation | Survives to stage 5 |
| `unsupported` | Any sub-claim finds nothing | Dies |
| `contradicts-active-decision` | Any sub-claim conflicts with a `brain_get_current_decision` result | **Promoted** |

`unsupported` is a death, not a demotion, and one empty sub-claim is enough: an idea standing
on three verified claims and one unverifiable one is an idea whose weight rests on the
unverifiable one. Log it: the idea, and the sub-claim that found nothing. The log is not
decoration; a domain where most ideas die on the same sub-claim is telling you the Brain has a
coverage hole worth recording, and the user should hear it.

**4. Handle contradiction by promotion, never by deletion.** An idea that conflicts with an
active decision is the most valuable output this pipeline produces, and killing it would make
the pack an enforcer of the company's existing orthodoxy, the opposite of its purpose. Convert
it into an internal contrarian thesis:

- cite the contradicted decision by id, with what it currently says;
- state precisely where the idea and the decision disagree, in one sentence;
- argue the revisit on the evidence: what has changed, or what the decision's recorded
  reasoning did not account for;
- carry `type: internal-contrarian` into the output contract.

Check the supersede chain before arguing. `brain_get_current_decision` returns the live
position, and a contradiction against a decision that was already superseded is not a
contrarian thesis, it is a stale reading.

## Citation integrity

**Only ids actually returned by tool calls in this session may be cited.** No id from memory,
no id inferred from the user's phrasing, no plausible-looking id, no id carried over from an
earlier conversation. This is a red line in `SKILL.md`, and the reason is that a fabricated
citation is indistinguishable from a real one to the reader while destroying the only thing
that separates this pack from a prompt anyone can copy. If a citation cannot be traced to a
call in this session's history, the thesis has no grounding and takes the `UNGROUNDED` label
from `references/output-contract.md`.

**Read a returned decision before citing it.** `brain_get_current_decision` declines below a
relevance bar: an off-topic query answers with null and says no active decision matched
closely enough, and a non-null result carries a note that it cleared the bar. Take the note
as the server's claim, not as your check. Read the returned title and body and confirm they
are about the sub-claim's subject; if they are not, the sub-claim found nothing. The reason
this rule survives a server that now filters: an id that genuinely was returned by a tool
call in this session passes the returned-by-a-tool check while supporting a claim it says
nothing about, which makes it more dangerous than a fabricated id rather than less. A
declined lookup is a normal answer, not a fault, and never evidence that the company has no
position: `brain_search` may still surface weaker material, because it never claims what it
returns is current truth.

**A tool error is not a verdict.** On an error, an internal error included, retry the call once
with the phrasing tightened toward a decision title. If it errors again the sub-claim is
unverifiable, which is neither support nor a death: the Brain did not answer, so it did not say
no. Tell the user the check could not run, name the sub-claim, and grade the idea on the
sub-claims that did resolve. If the unverifiable one was load-bearing on its own, the thesis
takes the `UNGROUNDED` label instead of a death-log entry, because logging a death would record
a coverage hole the run never established.

When coverage was classified `blind` or `thin` in `references/readiness.md`, this stage still
runs. It just finds little. Ideas that find nothing under thin coverage are not dead on the
merits, so keep the strongest of them and ship them labeled rather than reporting an empty
result. Say which is which. That classification does not overrule what this stage measures in
the other direction either: an idea whose every load-bearing sub-claim earned a relevant
citation here is `supported` and ships with those ids even in a run the probe called blind,
because stage 1 estimated the coverage and stage 4 measured it. Every other thesis in the run
carries the label.

## Handing over

Pass to stage 5: the surviving `supported` ideas with their citations and relevance lines, the
promoted `contradicts-active-decision` ideas with the decision ids and the revisit argument,
and the death log. Then load `references/output-contract.md`.
