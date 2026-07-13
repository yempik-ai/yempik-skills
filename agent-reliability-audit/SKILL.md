---
name: agent-reliability-audit
description: >-
  Audit whether an internal AI agent or agentic workflow can safely act using knowledge
  that is current, approved, authoritative, non-conflicting, source-linked,
  permission-aware, and testable. Use when users ask for an agent reliability audit,
  agent-readiness assessment, stale or contradictory policy review, source-precedence
  check, internal-agent governance review, scenario evals, or evidence-based testing of
  whether an agent could take the wrong action. Also use for a company brain or
  workspace health audit when the goal is agent reliability. Inspect live files,
  connected sources, instructions, and traces read-only; create an evidence ledger;
  run the relevant checks from a 15-audit rubric; and return prioritized findings with
  citations, failure scenarios, limits, remediation, and evals.
---

# Agent Reliability Audit

Audit the knowledge an internal AI agent actually uses before it acts. Start with one
agent or workflow, inspect its live sources, and test concrete failure scenarios. Do
not substitute a questionnaire for source inspection. Return evidence behind every
material finding.

## Non-negotiable rules

1. Keep source systems read-only. Creating audit artifacts is allowed; changing the
   audited knowledge is not, unless the user separately asks for remediation.
2. Separate **observation**, **inference**, and **absence test**. Never present one as
   another.
3. Cite a file plus line range, page, URL, or connected-record ID for every finding.
   If the tool cannot expose stable locations, cite the smallest stable source unit.
4. Treat age as a signal, not proof of staleness. Confirm scope, owner, validity,
   supersession, or review cadence before calling content stale.
5. Treat contradictions as candidates until subject, scope, time, authority, and
   status have been compared.
6. Do not infer business permissions from filesystem access. Mark permission audits
   `NOT ASSESSED` unless identity/scope metadata is available.
7. Do not claim that tacit knowledge is absent. Report observable key-person risk and
   specify the interview or evidence needed to validate it.
8. Redact secrets, personal data, and sensitive values from excerpts. Record only the
   minimum evidence needed to reproduce the finding.
9. State coverage and blind spots. A partial audit is useful; an unlabeled partial
   audit is misleading.

## Choose the audit mode

Infer the narrowest useful mode from the request. Ask only when two plausible scopes
would materially change the result.

| Mode | Use it for | Default scope |
|---|---|---|
| **Agent** | "Audit this internal agent" | One agent, accessible knowledge, instructions, tools, traces, and 5-10 scenario evals |
| **Workflow** | "Can our support agent handle refunds safely?" | One business outcome, its agent, sources, rules, exceptions, and recent cases |
| **Workspace** | "Audit our company brain / Notion / folder" | All 15 audits, risk-based sampling when the corpus is large |

Prefer **Agent** or **Workflow** for a first audit: a large account with a small,
testable scope produces stronger evidence than an organization-wide score based on
shallow sampling.

## Core workflow

### 1. Establish scope and evidence access

Record:

- audit objective and mode;
- business workflow or agent, if any;
- sources available and unavailable;
- date/time boundary and current date;
- whether recent cases, traces, permissions, owners, and review history exist;
- output location.

Default output folder: `agent-reliability-audit/YYYY-MM-DD/`. If it exists, append
`-HHMM`. Never write audit output inside an audited source-of-truth folder.

### 2. Build an inventory before deep reading

Enumerate sources, types, owners, modification/review dates, status fields, declared
sources of truth, and likely operational importance. When shell access is available,
run:

```bash
python3 <skill-path>/scripts/inventory.py <workspace-root> \
  --output <audit-output>/inventory.json
```

The scanner is optional and standard-library only. For connected apps or environments
without shell access, build the same inventory with available search/fetch tools.

Exclude generated assets, dependencies, caches, backups, and obvious archives unless
they are relevant to a suspected conflict. Do not read every file blindly. Prioritize:

1. policies, procedures, decision logs, operating instructions, and agent prompts;
2. documents retrieved or cited by the selected agent or workflow;
3. current records plus older or duplicate versions of the same subject;
4. recent real cases, failures, escalations, or traces;
5. source/owner/review and permission metadata.

For more than 500 candidate documents, use risk-based sampling and disclose the
selection rule. Include every high-impact source, then sample across teams, ages,
formats, and duplicate clusters.

### 3. Run the relevant audits

Read [references/audit-rubric.md](references/audit-rubric.md) completely. Run all 15
audits for Workspace mode. For Workflow or Agent mode, run every applicable audit and
mark the rest `NOT ASSESSED`; never convert missing access into a failing score.

Use [references/evidence-and-scoring.md](references/evidence-and-scoring.md) for the
evidence ledger, maturity levels, confidence labels, and P0-P3 priority rules.

### 4. Test what an agent can do

For Workflow and Agent modes, read
[references/scenario-evals.md](references/scenario-evals.md) completely. Derive 5-10
cases from the actual sources and recent work:

- normal case;
- exception or boundary case;
- conflicting-source case;
- missing-information case;
- forbidden or approval-required action.

Run the target agent only when it is available and the user has authorized that test
surface. Otherwise produce an executable test pack and label it `NOT RUN`. Never grade
the same model output that invented the expected answer without anchoring the expected
answer to approved sources.

### 5. Prioritize without fake precision

Rank findings by consequence, evidence confidence, recurrence, and blast radius. Use:

- **P0** — confirmed exposure or high-impact action risk requiring containment;
- **P1** — confirmed/strong issue likely to cause wrong action in a core workflow;
- **P2** — material reliability gap, or a serious candidate requiring validation;
- **P3** — hygiene or leverage improvement with limited immediate consequence.

Do not predict revenue, compliance, or probability unless the input contains the
necessary data. State what additional evidence would change the rank.

### 6. Deliver reproducible artifacts

Create:

```text
agent-reliability-audit/YYYY-MM-DD[-HHMM]/
  REPORT.md          # executive verdict, scorecard, prioritized findings, roadmap
  evidence.jsonl     # one minimal, source-linked evidence record per line
  evals.md           # scenario test pack and results, when applicable
  inventory.json     # when the scanner or equivalent inventory was used
```

Use [templates/REPORT.md](templates/REPORT.md) as the report contract. Every detailed
finding must include:

- finding ID, audit dimension, priority, and confidence;
- observed condition and evidence IDs;
- concrete failure scenario;
- recommended control or remediation;
- effort (`S`, `M`, `L`) and suggested owner role;
- verification step and remaining uncertainty.

End with **What this audit did not establish**. Include unassessed sources, unrun evals,
unavailable permission data, and inferences requiring a human interview.

## Definition of done

Do not call the audit complete until:

- scope, date, mode, and source coverage are explicit;
- each material finding points to evidence;
- absence claims include the searched scope and method;
- all 15 audits are scored or marked `NOT ASSESSED`;
- overall maturity respects the gates in the scoring reference;
- scenario evals are run or clearly labeled `NOT RUN`;
- source systems remain unchanged;
- the report separates verified facts, candidates, limitations, and next actions.

## What this skill cannot establish

It cannot certify legal compliance or security, discover knowledge nobody expressed,
prove business ROI without operational data, validate the truth of a policy without an
authoritative source, or guarantee future agent behavior from document inspection alone.
It produces an evidence-based diagnostic and test surface, not a certification.
