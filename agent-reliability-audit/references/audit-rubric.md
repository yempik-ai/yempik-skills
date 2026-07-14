# The 15-audit rubric

Run the rubric against the declared scope. Score each audit `0-4` or mark it
`NOT ASSESSED`. Cite evidence for both strengths and risks.

## A. Coverage

### 1. Source coverage and silos

Determine which sources the workflow or agent depends on and whether material sources
are absent, disconnected, duplicated, or inaccessible. Evidence may include a source
map, tool configuration, citations in operating documents, and actual retrieval paths.

Do not equate "connected" with "used correctly".

### 2. Tacit knowledge and key-person risk

Look for observable dependencies on individuals: single-owner processes, undocumented
escalations, "ask X" instructions, repeated manual intervention, or rules found only in
interviews/calls. Report risk candidates, not claims about unknowable missing knowledge.

### 3. Decision and process coverage

Check whether core outcomes have an explicit process, decision criteria, exceptions,
stop conditions, escalation paths, and a definition of done. A checklist without
decision logic is incomplete for an agent.

## B. Integrity

### 4. Freshness and decay

Check review dates, validity windows, owners, supersession links, change frequency, and
recent operational changes. Age alone is insufficient. A current-looking document with
no owner or review rule may be higher risk than an old stable glossary.

### 5. Contradictions and unresolved conflicts

Compare statements only when they concern the same subject and scope. Resolve or flag:

- simultaneous active rules with incompatible actions;
- mismatched thresholds, prices, SLAs, roles, or approval paths;
- decisions contradicted by later docs without explicit supersession;
- shared-system records that disagree with the declared source of truth.

Label unresolved comparisons `candidate contradiction`.

### 6. Current truth and version control

Determine whether a user or agent can identify the active version. Look for status,
effective date, supersedes/superseded-by links, version history, one declared source of
truth, and archive boundaries. File versioning alone does not identify current policy.

## C. Evidence

### 7. Source lineage and citations

Check whether consequential rules, claims, and decisions point to an authoritative
source, date, and smallest useful source location. A bibliography at the end of a large
document is weaker than claim-level lineage.

### 8. Approval and human accountability

Check draft/active/deprecated states, approver identity or role, approval date, and the
path for corrections. Agent-generated content without an explicit review state must not
be treated as approved operational truth.

### 9. Confidence and inference control

Check whether facts, assumptions, hypotheses, recommendations, and model inferences are
distinguished. Look for confidence labels, unresolved questions, and rules preventing
unverified inferences from reaching production behavior.

## D. Agent readiness

### 10. Retrieval reliability

Test whether the relevant information can be found from realistic task wording and
returned with the correct source. Measure wrong-source retrieval, no-answer behavior,
and whether newer/authoritative sources outrank plausible but obsolete ones.

### 11. Executable rules and exceptions

Check whether knowledge is actionable: trigger, required inputs, action, exception,
approval threshold, prohibited action, and escalation. Narrative guidance can be useful
to humans while remaining unsafe for autonomous execution.

### 12. Scenario evals and failure handling

Check whether representative cases exist and whether the agent respects expected
decisions, citations, exceptions, abstention, and escalation. Use the scenario protocol;
do not award a score based only on a polished demo.

## E. Governance

### 13. Permission boundaries and sensitive data

Inspect business permission metadata, identity scopes, source-level access, and whether
retrieval preserves those constraints. File readability is not proof of authorization.
If permission metadata or identity-specific tests are unavailable, mark `NOT ASSESSED`.

### 14. Ownership and portability

Check whether the company can export knowledge in usable form, preserve sources and
history, change model/provider, and recover without a vendor-specific memory silo.
Portability is not merely a PDF export; agents and humans must still be able to use it.

### 15. Maintenance and review burden

Determine how knowledge enters, changes, gets reviewed, and decays. Look for duplicated
manual work, review queues, ownership gaps, feedback loops, and time spent maintaining
truth. A system that is accurate only after heroic upkeep is not operationally mature.

## Scoring anchors

Apply these anchors per audit:

| Score | Meaning | Required evidence |
|---|---|---|
| `0` | Absent or uncontrolled in the assessed scope | Direct evidence or a documented absence test |
| `1` | Ad hoc; depends on individual behavior | Repeated examples, not a single anecdote |
| `2` | Documented and repeatable | Current artifacts covering the scope |
| `3` | Governed | Owner, state, source, review/control path evidenced |
| `4` | Verified and continuously maintained | Governed artifacts plus recent eval/monitoring evidence |

Use `NOT ASSESSED` when access or evidence is insufficient. Do not score missing access
as zero.
