# Evidence, confidence, priority, and maturity

## Evidence ledger

Write one JSON object per line in `evidence.jsonl`:

```json
{"id":"E-001","type":"direct","source":"policies/refunds.md#L18-L31","observed_at":"2026-07-13","claim":"Refunds over EUR 500 require finance approval.","excerpt":"[redacted/minimal excerpt]","sensitivity":"internal","supports":["F-001"]}
```

Required fields:

- `id`: stable `E-###` identifier;
- `type`: `direct`, `inference`, `absence_test`, `user_stated`, or
  `external_baseline`;
- `source`: reproducible path/line, page, URL, or connected-record identifier;
- `observed_at`: audit date;
- `claim`: the atomic observation or bounded inference;
- `excerpt`: optional and minimal; redact secrets and personal/sensitive data;
- `sensitivity`: `public`, `internal`, `restricted`, or `unknown`;
- `supports`: finding IDs using this evidence.

For `absence_test`, also include:

```json
{"scope":"42 policy files under policies/","method":"searched headings and frontmatter for owner, reviewed, review_after, valid_until","result":"No review field found in 39/42 files"}
```

Never write "there is no policy" when the evidence is only "the searched locations did
not contain one".

## Confidence labels

| Label | Use only when |
|---|---|
| `CONFIRMED` | Direct evidence or a reproducible absence test establishes the condition |
| `STRONG` | Multiple independent signals support the same bounded inference |
| `CANDIDATE` | A plausible risk needs an owner, authority, permission, or context check |
| `UNVERIFIED` | User-stated or externally assumed; no source in the audited scope confirms it |

An external best practice can explain importance, but cannot prove an internal finding.

## Priority rules

Prioritize consequence first, then confidence, recurrence, and blast radius.

| Priority | Rule |
|---|---|
| `P0` | Confirmed sensitive-data exposure, unauthorized action path, or high-impact operational rule that is actively wrong; contain before expansion |
| `P1` | Confirmed/strong defect likely to cause repeated wrong action, missed approval, or wrong-source use in a core workflow |
| `P2` | Material reliability weakness, or serious candidate requiring a named validation step |
| `P3` | Hygiene, portability, efficiency, or leverage improvement with limited immediate consequence |

Do not rank a `CANDIDATE` above a confirmed issue solely because its imagined consequence
is dramatic. State the evidence that would promote or demote it.

Effort estimates:

- `S`: same-day change, no architectural dependency;
- `M`: several days or cross-owner coordination;
- `L`: multi-week system/process change.

## Overall maturity L0-L4

Calculate the median of **assessed** audit scores, round down, then apply all gates. Show
both the raw median and the gated level.

| Level | Meaning |
|---|---|
| `L0 Fragmented` | No dependable map or operating knowledge surface |
| `L1 Searchable` | Knowledge exists and can be found, but authority and maintenance are ad hoc |
| `L2 Structured` | Core knowledge is organized, owned, and repeatable |
| `L3 Governed and agent-ready` | Sources, state, approvals, freshness, permissions, and executable rules are controlled |
| `L4 Continuous and verified` | Capture, review, evals, monitoring, and correction loops are operating continuously |

Apply these caps:

1. No source-of-truth map or source lineage for consequential rules: maximum `L1`.
2. No approval state or freshness/review control: maximum `L2`.
3. Permission audit `NOT ASSESSED` for an acting agent: do not claim agent-ready; maximum
   `L2` for that agent scope.
4. No executed scenario evals: maximum `L3`.
5. `L4` requires evidence of a recent continuous capture/review/monitoring loop; a design
   document describing the loop is insufficient.

Do not compute an overall level when fewer than 8 audits are assessed in Workspace mode.
For Workflow/Agent mode, report a **scope maturity** and list the unassessed dimensions.
