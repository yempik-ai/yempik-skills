# Site-scan prompt

In the observed vertical, people search on social networks proved close to useless. The
engine that actually generates citable facts is an agent that visits sites and returns JSON.
Prompt actually used, adaptable to a new market.

## Prompt

```
Visit the site {{domain}}. Respond ONLY in JSON with these fields:

scale: number of managed units if declared, otherwise 'n/a'
offices: number of offices
team: number of visible people and names with role (maximum 5)
software: names of systems or portals cited
public_emails: plaintext addresses on the site
signals: at most 2 from [customer portal, app, described process, hiring, new office, acquisition]
proof: 1 URL of the most informative page

If the site does not respond or the domain is wrong, respond {"error": "reason"}.
Do not invent values.
```

## Field list: core versus market-specific

`team`, `public_emails`, `signals`, `proof` and the `error` fallback are universal: keep them
unchanged in every market.

`scale`, `offices` and `software` are market-specific and must be re-derived per market: see
`references/markets/_template.md` and the `scoring_proxies` slot in `references/configuration.md`.
In the reference market, a spot-check on `spot_check_sample_size` sites (reference default: 20)
found that 0 out of 20 sites declared a managed-unit count, so `scale` almost always resolves to
`n/a` there and `offices` carries the weight instead. A new market may need a different field in
this slot entirely (declared client count, declared square footage, whatever that market actually
publishes). Do not assume the reference three fields transfer as-is.

## Prompt rules (all learned in the field)

- Second person, imperative.
- An explicit fallback declared in the prompt, not left implicit.
- Constrained output format: compact JSON only.
- Short response, under 50 words per field: tokens cost money.
- One question per data point.
- `"Do not invent values"` is written in the prompt. It is not implied.

## Output contract

- JSON only. No prose before or after the object.
- `n/a` is a legitimate value for an undeclared field, not an error. It is not a value to
  invent around: if the site does not state it, write `n/a` and move on.
- `{"error": "reason"}` is the only response when the site does not respond or the domain is
  wrong. This is the explicit fallback: the scan agent never returns a half-filled object when
  it cannot read the page.
- The scan agent extracts facts only. It never scores, ranks or recommends. Scoring is a
  separate step: see `assets/clay/scoring-formula.md`.
