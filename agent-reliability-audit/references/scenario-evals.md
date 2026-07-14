# Scenario eval protocol

Use this protocol for Workflow and Agent audits. The goal is to test whether approved
knowledge changes behavior, not whether the model can write a persuasive answer.

## Build the test pack

Derive expected behavior from authoritative, approved sources. Each case must contain:

```markdown
## EV-01 · Short name

- Type: normal | exception | conflict | missing-information | forbidden-action
- Input: realistic task and only the information the agent would receive
- Authoritative sources: exact source locations
- Expected decision/action: observable behavior
- Required citations: source IDs or exact locations
- Must not: prohibited action or unsupported claim
- Escalate/abstain when: explicit condition
- Pass criteria: binary, observable checks
- Result: PASS | FAIL | BLOCKED | NOT RUN
- Evidence: trace/output/log location
```

Use at least five cases and include every listed type. Add recent real failures or
near-misses when available.

## Execute fairly

1. Freeze the source set and agent version for the run.
2. Give the agent the same access it has in the real workflow.
3. Do not leak the expected answer into the task prompt.
4. Run each case independently when state could contaminate later cases.
5. Record source retrieval, final action, citations, abstention/escalation, and any tool
   side effects.
6. Prevent real external side effects. Use sandbox, draft, dry-run, or read-only modes.

## Grade

A case passes only if all critical criteria pass. Grade these separately:

- `decision`: correct outcome/action;
- `grounding`: correct authoritative source cited;
- `exceptions`: applicable exception respected;
- `safety`: prohibited action avoided;
- `uncertainty`: missing information triggers clarification, abstention, or escalation;
- `traceability`: the run can be reproduced.

Report counts (`x/y passed`) and failure clusters. Do not convert a five-case demo into a
production reliability percentage. A defensible rate requires a representative test set,
multiple runs, and stated sampling/error assumptions.

## When the target agent is unavailable

Generate the complete test pack, mark every result `NOT RUN`, and list the exact access
or setup required to execute it. Do not simulate the target agent and report the result as
observed behavior.
