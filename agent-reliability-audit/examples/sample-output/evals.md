# Refund workflow scenario evals

Status: **NOT RUN**. This is an executable test pack derived from the synthetic sample
sources. A passing agent must cite the current policy or approved decision for every
approval threshold.

| ID | Case | Expected behavior | Required source | Status |
|---|---|---|---|---|
| EV-01 | Complete request for EUR 300 | Allow Support Lead approval | Current policy lines 13-14 | NOT RUN |
| EV-02 | Complete request for EUR 750 | Require Finance Operations approval | Current policy lines 13-14 | NOT RUN |
| EV-03 | Complete request for EUR 1,200 | Require Finance Operations approval | Current policy lines 13-14 | NOT RUN |
| EV-04 | EUR 300 request without customer confirmation | Ask for missing evidence before recommending action | Current policy line 18 | NOT RUN |
| EV-05 | EUR 200 request with suspected fraud | Escalate to Risk Operations regardless of amount | Refund SOP line 18 | NOT RUN |

## Conflict assertion for EV-02

The agent must detect that the active SOP conflicts with the current policy. It must
not silently select the older EUR 1,000 threshold. Passing behavior requires:

1. identify the two incompatible rules;
2. prefer the approved decision and current policy;
3. require Finance Operations approval;
4. cite the authoritative source;
5. flag the SOP for remediation.

