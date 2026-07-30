# Framework · What won't change

## What it finds

The wants clients will still have when the current tooling, channel and vocabulary are gone,
and the offerings that follow from them. Most roadmaps are built on transient enablers, which is
why they read as consensus: everyone is watching the same enablers change. Permanent wants are
boring, stated plainly in client records, and systematically under-served, and that combination
is where this framework's theses come from.

## Mandatory Brain inputs

| Input | Tool call | When it comes back empty |
|---|---|---|
| The client entities themselves | `brain_list_entities` filtered to clients, then `brain_get_entity` per client of interest | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |
| Each client's recorded needs and facts | `brain_neighbors` from the client entity, to reach the facts, processes and items connected to it | This framework refuses to run grounded: either skip it or run it labeled `UNGROUNDED`, never silently degrade |

The entities alone are not enough: a client list with no connected needs supports nothing about
what those clients want, and the split in step 2 would be invented. Skip the framework or label
it per `references/output-contract.md`. This is the framework most tempting to run on general
knowledge of the industry, and general knowledge of the industry is precisely the median this
pack exists to escape.

## Procedure

**1. Cluster the clients, then read their recorded needs.** Cluster on what their day is
measured in, not on size or sector. Two clients with the same headcount and different success
metrics belong in different clusters.

```
brain_list_entities: type = client
brain_get_entity:    per client in the cluster
brain_neighbors:     from each client entity, to reach connected needs, constraints and processes
```

Three or four clusters is usually enough. A cluster of one is a client, and theses derived from
it are account plans rather than strategy.

**2. Split every recorded need into permanent want or transient enabler.** The test is one
question, applied per need: *if the tool, channel or format currently used to satisfy this
disappeared tomorrow, would the client still want the thing?*

- **Permanent want**: survives the test. Reliability, speed, someone answering, not being
  surprised by a cost, not having to re-explain context, being able to prove what happened.
- **Transient enabler**: dies with the tool. A dashboard, an integration, a file format, a
  channel, a report cadence, a named product.

Enablers are not worthless; they are just not what to build a thesis on, because a thesis
anchored to one expires with it. When a recorded need is phrased as an enabler (most are, since
clients describe needs in the vocabulary of what they currently have), restate it as the want
underneath, and note that the restatement is yours.

**3. Score each permanent want against what the roadmap actually serves.** Per want, ask what
the company currently ships against it and how directly. Under-served wants are the ones the
roadmap addresses only as a side effect of something else: that indirection is the gap.

**4. Re-derive the offering from the want.** The thesis is an offering designed from the
permanent want as if the current product did not exist, then reconciled with what does. The
`consensus` field is the enabler-shaped answer everyone else is building. The `grounding` field
carries the client entity ids and the connected need ids, one relevance line each, per
`references/output-contract.md`.

**5. Reject theses that only re-skin an enabler.** If the claim reduces to a better dashboard,
a new integration or a faster report, the split in step 2 was not applied to the claim itself.
Run the disappearing-tool test on the thesis, not just on the need.

## Worked shape

*Fictional throughout: "Cobalt Bikeshare Services" and its clients do not exist, and neither do
the ids below.*

```
Domain: what Cobalt Bikeshare Services should offer its municipal clients next
brain_list_entities (client) → three clusters; cluster B = mid-size municipalities measured on
  complaints per thousand rides.
brain_neighbors from ENT-114, ENT-119, ENT-127 → KB-4402 (need): "monthly usage reporting in
  the council's own format"; KB-4407 (fact): every cluster-B contract renewal was preceded by a
  council meeting where a councillor asked about a specific complaint.
Split: KB-4402 is an enabler. The format dies with the reporting tool. The want underneath, per
  KB-4407, is being able to answer for a single incident in public without preparation.
Roadmap check: served indirectly. The monthly report aggregates, and an aggregate is the wrong
  shape for one councillor's question.

claim: Cobalt should sell per-incident answerability (any single ride reconstructable on
  demand) and treat the monthly report as a by-product, because the contract is defended in a
  council meeting about one complaint, not in a review of a monthly total.
consensus: Municipal clients want better reporting, so the roadmap is dashboards and formats.
grounding:
  - ENT-114, ENT-119, ENT-127: cluster-B clients measured on complaints per thousand rides
  - KB-4402: the recorded need, stated in the vocabulary of the current reporting tool
  - KB-4407: every cluster-B renewal was preceded by a public question about one incident
cheapest_test: reconstruct three real complaints end to end by hand and hand the file to one
  client contact before their next council meeting → signal: whether they use it in the meeting
risk_if_wrong: a week of reconstruction work on a want only the loudest client actually has
type: market-contrarian
```
