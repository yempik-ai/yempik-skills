# Stage 1 · Readiness gate

Coverage is measured, never assumed. This stage decides whether the run produces grounded
theses or labeled provocations, and it decides it before a single idea exists, because a
coverage claim made after the ideas are written is a rationalisation of work already done.

## Procedure

**1. Identity and scopes.** Call `whoami` once. It returns the tenant the connector is bound
to and the scopes the user granted. Read both: the tenant tells you whose governed truth you
are about to reason over, and the scopes tell you which reads will succeed.

If any later call returns `insufficient_scope`, stop the pipeline and tell the user the grant
is too narrow for this run, that they can widen it in Connections on the Yempik workspace,
and which capability is missing. Do not work around it by inferring the missing data, and do
not silently continue into the ungrounded path as if the user had chosen it. A scope
refusal is a fixable configuration state, not a coverage verdict.

**2. Coverage probe.** Run at least two `brain_search` queries that reformulate the domain in
different vocabulary, plus one `brain_list_items` sweep of active items. Two reformulations
is a floor, not a target: a single phrasing measures the phrasing, not the coverage.

```
brain_search: "<domain in the user's words>"
brain_search: "<same domain in the company's own vocabulary, the terms decisions and
               rules would actually use>"
brain_list_items: state "active", narrowed by type when the domain implies one
                  (decision, process, rule, fact, glossary, person, client)
```

`brain_list_items` has no domain filter and no text filter: its parameters are type, state,
`created_since`, cursor and limit. It hands back a page of the tenant's active items, and you
judge from the returned titles and excerpts which of them touch the domain, paging or narrowing
by type when the page is long. The relevance judgment was always yours, not the tool's.

Count only **relevant active items**. A candidate awaiting review is not governed truth and
does not count. An active item that merely mentions the domain in passing does not count
either: the test is whether it would carry weight in a sub-claim check during stage 4.

On a question that spans several domains at once (positioning plus pricing plus delivery),
`brain_resolve_question` may complement the probe by reporting which domains come back
covered. No dedicated ideation recipe exists in v1, so treat its output as an additional
signal on the same count, not as a replacement for the probe above.

**3. Classify.** Explicit thresholds, applied to the relevant-active count:

| Relevant active items | Coverage | Effect on the output contract |
|---|---|---|
| 0 | `blind` | Every thesis stage 4 did not ground carries `UNGROUNDED: Brain coverage on this domain is blind` |
| 1-4 | `thin` | Every thesis stage 4 did not ground carries `UNGROUNDED: Brain coverage on this domain is thin` |
| ≥ 5 | `covered` | Grounded contract: theses cite the ids stage 4 returned |

The label is defined in `references/output-contract.md` and is written verbatim, in the
`grounding` field, in place of citations. Mixed outcomes are possible and normal: if the
probe covers positioning but nothing on clients, the run is covered for theses whose
sub-claims live in positioning and blind for the rest. Classify per thesis in that case,
never by rounding the whole run up to the better level. The same per-thesis rule runs the other
way too: a thesis whose load-bearing sub-claims all earn relevant citations in stage 4 ships
grounded even under a `blind` or `thin` classification, because this probe estimates coverage
and stage 4 measures it. Step 4 still reports the run-level class as computed here.

**4. Report before proceeding.** State the tenant, the coverage level, the count, and the
contract that follows from it, in one or two sentences. Then continue to stage 2. A run that
never told the user which contract it was operating under cannot be audited afterwards, and
its citations become unverifiable claims about a check nobody watched happen.

## What this stage never does

It never generates ideas: the temptation to "just check while brainstorming" is what
produces coverage claims shaped to fit the output. It never treats an absent domain as a
reason to skip the run: blind coverage still produces useful provocations, honestly labeled.
And it never re-runs itself later to upgrade a label after grounding disappointed.
