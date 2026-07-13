# Agent Reliability Audit: synthetic refund agent

> Reproducible sample. All companies, people, records, and amounts are fictional.

## Executive verdict

The refund workflow is **L1 Searchable**. Its core rules are easy to find, but two
active sources give incompatible approval thresholds. A recent synthetic case follows
the older SOP and would allow a EUR 750 refund without the Finance Operations approval
required by the current policy and approved decision.

This is a **P1 agent reliability risk**. The immediate control is to make the current
policy authoritative, deprecate the old SOP, and add source precedence plus abstention
rules to the agent instructions.

## Scope and coverage

| Field | Value |
|---|---|
| Audit date | 2026-07-13 |
| Mode | Agent |
| Agent | Synthetic customer-support refund agent |
| Workflow | Customer refund approval |
| Sources assessed | 5 of 5 files in the sample workspace |
| Scenario evals | 5 generated, not run |
| Permissions | Not assessed because identity and access metadata are absent |

## Scorecard

| # | Audit | Score |
|---:|---|---|
| 1 | Source coverage and silos | 3 |
| 2 | Tacit knowledge and key-person risk | NOT ASSESSED |
| 3 | Decision and process coverage | 2 |
| 4 | Freshness and decay | 2 |
| 5 | Contradictions | 0 |
| 6 | Current truth and version control | 1 |
| 7 | Source lineage and citations | 2 |
| 8 | Approval and accountability | 2 |
| 9 | Confidence and inference control | 1 |
| 10 | Retrieval reliability | 1 |
| 11 | Executable rules and exceptions | 1 |
| 12 | Scenario evals and failure handling | 1 |
| 13 | Permission boundaries and sensitive data | NOT ASSESSED |
| 14 | Ownership and portability | 3 |
| 15 | Maintenance and review burden | 1 |

Raw median of assessed dimensions: **1**. Gated maturity: **L1 Searchable**.

## Prioritized findings

### F-001: two active sources give different approval thresholds

**Audit:** Contradictions  
**Priority:** P1  
**Confidence:** CONFIRMED  
**Evidence:** E-001, E-002, E-003

The current policy and approved decision require Finance Operations approval above
EUR 500. The still-active SOP allows a Support Lead to approve up to EUR 1,000.

**Failure scenario:** a EUR 750 refund is approved without the required Finance
Operations review.

**Remediation:** mark the SOP version as deprecated, update its threshold, and link it
to the approved decision and current policy.

**Effort:** S  
**Suggested owner:** Customer Support Operations  
**Verification:** search all active refund sources for approval thresholds and confirm
that only EUR 500 remains authoritative.

### F-002: the agent has sources but no precedence rule

**Audit:** Retrieval reliability  
**Priority:** P1  
**Confidence:** CONFIRMED  
**Evidence:** E-004, E-005

The agent instructions list the policy, SOP, and decision but do not say which source
wins when they conflict. The sample case cites only the older SOP and recommends the
wrong approval path.

**Failure scenario:** retrieval returns a plausible active document, so the agent acts
confidently even though a more authoritative source says the opposite.

**Remediation:** define source precedence, require claim-level citations, and force
abstention plus escalation whenever active sources conflict.

**Effort:** S  
**Suggested owner:** Agent owner  
**Verification:** run the EUR 750 conflict eval and require the agent to cite the
policy and approved decision before escalating to Finance Operations.

### F-003: an approved update was not propagated to every operating artifact

**Audit:** Maintenance and review burden  
**Priority:** P2  
**Confidence:** CONFIRMED  
**Evidence:** E-003, E-006

The approved decision explicitly required updates to the policy, SOP, and agent
instructions. The policy changed, but the SOP remained active with the old rule.

**Remediation:** attach a completion checklist to consequential decisions and block
closure until every affected artifact has an owner, update, and verification result.

**Effort:** M  
**Suggested owner:** Decision owner  
**Verification:** replay the decision checklist and confirm every referenced artifact
was updated or formally exempted.

## 30-day remediation order

1. Contain: make the policy authoritative and deprecate the old SOP.
2. Prevent recurrence: add source precedence and conflict abstention to the agent.
3. Verify: run the five scenario evals in `evals.md`.
4. Maintain: add decision-to-artifact completion checks to the review workflow.

## What this audit did not establish

This sample did not run a live agent, inspect identity-specific permissions, interview
process owners, certify compliance, or estimate financial impact. It demonstrates the
audit method and evidence contract on a synthetic workspace.
