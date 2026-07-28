# Scoring formula

The enrichment platform's scan agent (`assets/clay/site-scan-prompt.md`) extracts facts. It
never assigns points. This file is the formula that turns those facts into a score.

## The three-way separation

```
model    -> extracts facts from the site, in JSON, without inventing
formula  -> assigns points to the JSON fields (this file)
human    -> approves the list before every send
```

Corrective rule: when scoring was left to the model, an important account was undervalued.
Since then, assigning points is never delegated to the model. See `policies/02-scoring.md`
for the narrative.

## Inputs

The formula reads exactly the fields the site-scan prompt produces, plus the buying-group
output from the selective further-research step (`routines/universe-sourcing.md`, step 5). It
never reads a field the scan did not produce, and it never infers a field from its absence: an
absent field scores at the lowest band for that dimension, it is not treated as evidence of
anything.

## Dimensions and weights (implementable spec)

Configuration: `scoring_weights` (`references/configuration.md`). Six dimensions, non-uniform
weights, total 0-12.

| Dimension (`score_breakdown` key) | Range | Scored from | Rule |
|---|---:|---|---|
| `scale_and_complexity` | 0-2 | `scan_json.scale`, `scan_json.offices`, `scan_json.team` | 0: no evidence of scale. 1: one signal present (for example more than one office). 2: two or more signals present (portfolio, units, team size, network). |
| `centralisation` | 0-2 | `scan_json.team`, `scan_json.signals` | 0: no distinct roles visible. 1: a specialised team or a department mailbox is visible. 2: distinct roles are named and a central process is described. |
| `evidence_of_system` | 0-2 | `scan_json.software` | 0: no system named. 1: a fragmented or generic stack is named. 2: a specific named incumbent system is named. |
| `pilotability` | 0-3 | `scan_json.offices`, `scan_json.team`, the step-5 buying-group output | 0: no isolable unit visible. 1: an isolable unit exists but no sponsor or user identified. 2: a sponsor or a user is identified. 3: an isolable unit, a sponsor, a user and available data are all identified. Heaviest dimension: never round it down to match the others. |
| `decision_access` | 0-2 | the step-5 buying-group output | 0: no buying-group role identified. 1: one role identified. 2: the buying group (sponsor, operational owner, actual user) is identified and reachable. |
| `change_signal` | 0-1 | `scan_json.signals` | 0: none of [hiring, new office, acquisition] present. 1: at least one present. |

Total: sum of the six dimensions, integer, 0-12.

## Priority bands

Configuration: `priority_bands`.

```
9-12  -> A, worked first
7-8   -> B, worked after A
5-6   -> C, only with a strong dynamic signal (change_signal = 1)
<5    -> not_now, or competitive intelligence only
```

## Further-research gate

Configuration: `further_research_threshold` (reference default: 7). Below this score, do not
spend on identifying the buying group: skip step 5 of `routines/universe-sourcing.md` for that
account.

## Output

Populate `Account.score` and `Account.score_breakdown` per `schemas/account.schema.json`.
`priority_band` is computed from the total against the bands above; it is never asserted
independently of the total.

## Gate before use

`list_approval_required` (`references/configuration.md`): the score orders the queue and makes
the order defensible. It does not predict a reply. A human approves the list before any send,
regardless of score. See `policies/02-scoring.md` for the counter-evidence: two accounts scored
10/12 and never replied, one account scored 9/12 and replied positively in 38 minutes, and the
account with the best conversion of the whole campaign was never scored at all.

## Market-specific proxies

The six dimensions above are universal. The observable proxies that feed
`scale_and_complexity`, `centralisation` and `evidence_of_system` are market-specific and must
be re-derived per market: see `references/markets/_template.md` and the `scoring_proxies` slot.
Run a spot-check on `spot_check_sample_size` sites (reference default: 20) before scoring the
whole universe. In the reference market, 0 out of 20 sites declared a managed-unit count, which
is why `scale_and_complexity` above reads offices and team rather than a declared unit count.
