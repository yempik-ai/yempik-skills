---
name: yempik-founder-mode
description: Use when the user wants contrarian, non-obvious, founder-grade ideas on a business domain and the Yempik Company Brain MCP connector is attached (consensus mapping, forced divergence, grounding of every idea against the tenant's governed decisions, rules, facts and clients), where surviving theses arrive already validated with Brain citations, anything ungrounded is labeled as such, and nothing is written to the Brain without per-thesis human confirmation.
metadata:
  author: yempik
  homepage: "https://brain.yempik.ai"
  version: "1.0.1"
---

# Yempik Founder Mode

## Overview

Two halves, and only one of them is defensible. Divergence (forcing a model off the median
answer it was trained to prefer) is prompt text: verbalized sampling, ordinary-persona
rotation, denial prompting. All published, all copiable, and all shipped openly here in
stage 3. Grounding is the other half: every raw idea is decomposed into its load-bearing
sub-claims and each sub-claim is checked against the tenant's governed truth in the Company
Brain: active decisions, rules, facts, client entities. That half runs on data the copier
does not have, which is why this file without the connector is a manual for an engine
nobody owns.

The consequence is a different deliverable. A list of twenty provocations hands the
filtering back to the user, which is exactly the work they wanted done; there is no
human-as-idea-filter in this pipeline. What comes out is three to five theses that already
survived the grounding pass, each carrying the Brain citations that kept it alive, what
consensus believes instead, the cheapest test that would kill it, and the risk if it is
wrong. Ideas whose sub-claims find no support die inside stage 4 and never reach the user.
Ideas that contradict an active decision are promoted rather than killed: a company's own
orthodoxy is the highest-value thing to be contrarian about, and supersede chains make the
argument checkable instead of rhetorical.

## When to use

A domain-level strategy question where the obvious answers are already known and worthless:
what to do that the market is not doing, which of our own active decisions deserves
revisiting, what we rejected for the wrong reason, what our clients will still want when the
current tooling is gone. Use it when the user asks for ideas and would be insulted by the
median five.

## When NOT to use

Execution work: plans, roadmaps, specs, implementations. Generic brainstorming with no
connector attached and a request to present the result as grounded: run it if asked, but
only under the ungrounded label of the degradation rule below, never as founder mode on data
you do not have. Any request to write the theses into the Brain autonomously, in bulk, or on
a blanket approval given before the theses existed.

## The pipeline

Five stages, fixed order, no exceptions. Nothing is skipped and nothing is merged into a
neighbour: stage 2 exists to produce the denylist stage 3 consumes, stage 3 is unfiltered by
construction, and stage 4 is therefore the only filter in the system. Merging generation and
evaluation re-collapses the distribution, which defeats the one thing stage 3 is for. Each
stage's full procedure lives in its reference file, loaded when that stage runs.

**1. Readiness gate**: `references/readiness.md`. Establish the tenant and the granted
scopes with `whoami`, then probe what the Brain actually holds on the domain with
`brain_search` and `brain_list_items`. The probe classifies coverage as blind, thin or
covered, and that classification is binding on stage 5's output contract. Coverage is
measured before ideating, never asserted afterwards.

**2. Consensus map**: `references/consensus-map.md`. Write out, as full sentences, the
roughly five answers anyone would give to this prompt, the median the model reaches for
first. They serve twice: as the explicit ban list for stage 3 and as the `consensus` field
of every thesis that ships. Writing them down is what makes denial prompting a procedure
rather than an intention.

**3. Divergence**: `references/divergence.md`. Three techniques in sequence: verbalized
sampling with probabilities and tail selection, rotation through mundane personas, and a
denial pass against the consensus map plus everything generated so far. Target 15 to 20 raw
ideas. No evaluation, no feasibility talk, no quiet dropping of the weird ones: judgment
belongs to stage 4 and arrives there in full.

**4. Brain grounding**: `references/grounding.md`. Decompose each raw idea into two to four
load-bearing sub-claims and verify each against the Brain with `brain_search`,
`brain_get_current_decision`, `brain_get_entity` and `brain_neighbors`. An idea whose
sub-claims find nothing dies and is logged with the sub-claim that failed. An idea that
conflicts with an active decision is promoted to an internal contrarian thesis, citing the
decision id it contradicts.

**5. Thesis output**: `references/output-contract.md`. Three to five surviving theses in the
fixed field format, with the coverage label from stage 1 applied where grounding is absent.
Then, and only then, the outlet: per thesis, default off, the user may approve turning it
into a Brain candidate through `brain_open_changeset`, `brain_propose_item` and
`brain_submit_changeset`. Silence is not approval.

## Loading order

Never preload everything. Load this file, then only the rows the task actually needs.

| Task | Load |
|---|---|
| Stage 1, readiness on a domain | `references/readiness.md` |
| Stage 2, writing the consensus map | `references/consensus-map.md` |
| Stage 3, generating raw ideas | `references/divergence.md`, plus any framework row below |
| Stage 4, grounding the raw ideas | `references/grounding.md` |
| Stage 5, writing theses and offering the outlet | `references/output-contract.md` |
| Where the company's stated thesis has no decision behind it | `references/frameworks/thiel-contrarian.md` |
| Which known failure paths are already in motion | `references/frameworks/inversion.md` |
| What was rejected for being tedious rather than worthless | `references/frameworks/schlep-blindness.md` |
| Offerings re-derived from what clients will still want | `references/frameworks/what-wont-change.md` |
| The ideas read diverse but say the median, or a citation looks invented | `references/failure-modes.md` |

Frameworks are optional idea generators inside stage 3 and validators inside stage 4; the
five stage files are not optional. When context fills, drop framework files, never the stage
procedures or the output contract.

## Degradation

No connector, or coverage classified blind or thin: the pipeline still runs, and the output
is labeled. Every thesis that did not meet stage 4's `supported` bar carries
`UNGROUNDED: Brain coverage on this domain is <blind|thin>` in place of citations, and the
reply states the difference in plain terms: these are provocations that survived nothing, so
their failure rate is unknown, whereas a grounded thesis has already been checked against what
the company decided, recorded and observed.
Say which one the user is holding. The label is not a disclaimer to bury at the end; it is
the honest name of the artefact.

## Red lines

- Never fake grounding. A thesis presented with citations must have earned them in stage 4,
  and a thin-coverage run wearing a grounded output contract is the same lie with better
  formatting.
- Never cite a Brain item, entity or decision id that a tool call in this session did not
  return. Ids reconstructed from memory, from the user's phrasing, or by pattern are
  fabrications regardless of whether they happen to resolve.
- Never write to the Brain without the user's explicit yes on that specific thesis. One
  approval covers one thesis; approval of the batch is not a thing this pack offers.
- Never present stage 3's raw list as the deliverable. Ungrounded ideas are working material,
  and shipping them as theses moves the filtering job back onto the user.
