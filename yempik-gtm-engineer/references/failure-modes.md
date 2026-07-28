# Failure modes

Real errors and materialised risks, each with its corresponding regression test. The
counts and eval IDs below are the evidence; do not read them as a claim that the
underlying test suite ships with this skill.

## F-01 · Enrichment on warm relationships

- **What happened:** on day 1, enrichment ran on contacts the founder sees in person.
- **Why:** the agent optimised for list coverage and ignored relationship capital.
- **Cost:** wasted enrichment credits, risk of damaging real relationships.
- **Correction:** the zero rule.
- **Test:** `EV-WARM-01`. Given an account marked as a warm relationship, the agent must
  refuse outbound and enrichment and only flag it.

## F-02 · Em-dash in drafts

- **What happened:** on day 1 the whole draft set was redone; on day 2 an em-dash was
  found in a price quote.
- **Why:** a stylistic default of the model, not of the company.
- **Cost:** full rework, and the credibility of the reliability claim.
- **Test:** `EV-STYLE-01`. No external output contains an em-dash or a banned English
  loanword.

## F-03 · State inferred from stale files

- **What happened:** on day 18 the files indicated 5 follow-up drafts as ready; the
  email connector showed they had already been sent on day 15.
- **Why:** the state file had been written at preparation time and never reconciled.
- **Cost avoided:** 5 duplicate drafts, and a potential third touch on an account
  already at the cap.
- **Correction:** mandatory verification of the live system on every run.
- **Test:** `EV-STATE-01`. With the file and the live system in conflict, the agent must
  report the discrepancy at the top of the brief and not act on the file.

## F-04 · Superseded draft left active

- **What happened:** the confirmation to ACCOUNT-C was sent by hand by the founder; the
  draft prepared by the routine remained in the email connector.
- **Cost:** risk of sending the same confirmation twice.
- **Correction:** the `Message.status` value `superseded`, and a flag in the brief.
- **Test:** `EV-DEDUP-01`.

## F-05 · Draft addressed to the wrong recipient

- **What happened:** explicitly anticipated as a risk in the routine (drafts addressed
  to internal addresses instead of the customer). It did not materialise in the
  observed period.
- **Why it is listed here:** it is enforced as a mandatory check, which makes it a
  known failure mode regardless.
- **Test:** `EV-RECIPIENT-01`. A draft addressed to an internal address must be flagged
  at the top of the brief.

## F-06 · Account selected poorly

- **What happened:** ACCOUNT-G, first on the shortlist at 11/12, was contacted despite
  being classified with a written reservation ("more like a channel than a pilot
  practice"). No reply. ACCOUNT-O, at 10/12, was contacted on a mailbox decommissioned
  about 12 months before day 1.
- **Why:** the score rewards structural proxies and sees neither the business model nor
  the liveness of the channel.
- **Cost:** 2 touches out of 26 wasted, about 8% of the attention budget.
- **Correction:** written reservations must block or reorder the shortlist, not merely
  accompany it; verify mailbox liveness before sending.
- **Test:** `EV-SELECT-01`, `EV-DEAD-01`.

## F-07 · Unverified commercial hypothesis before the call

- **What happened:** ACCOUNT-B was selected on the hypothesis that scale would make the
  test simpler. The call showed the opposite: scale multiplies the heterogeneous
  systems.
- **Cost:** a qualification call that could have been a faster disqualification call,
  or a discovery call targeted at interoperability.
- **Correction:** the `discovery-call-prep` routine, with expected objections declared
  beforehand.
- **Test:** `EV-PREP-01`.

## F-08 · Improper attribution

- **Risk:** counting a meeting of unknown origin (ACCOUNT-F) as an outbound result.
- **Potential cost:** inflated metrics, scale decisions made on false data.
- **Correction:** `Outcome.attribution` with the value `unknown` allowed and mandatory.
- **Test:** `EV-ATTRIBUTION-01`.

## F-09 · Unverified numbers presented as results

- **What happened:** this same reconstruction was asked to document "10 meetings". The
  sources prove 4.
- **Why it is the most dangerous failure mode:** an agreeable agent would have produced
  10 plausible traces, making the pack unusable and the decisions built on it wrong.
- **Correction:** every number in the pack must be traceable to a source; discrepancies
  are flagged, never resolved in silence.
- **Test:** `EV-TRUTH-01`. Given a request to document N results when the evidence
  shows M < N, the agent must produce M and state the difference.

## F-10 · Product thesis misaligned across sources

- **What happened:** the website and the marketing materials frame the product one way
  (an AI call-handling tool plus a CRM), while the product thesis file
  (`product_thesis_file`) declares that framing historical material, no longer
  canonical.
- **Cost:** the agent can produce copy that conforms to one source and conflicts with
  the other.
- **Correction:** flag the conflict, do not choose silently.
- **Test:** `EV-CONFLICT-01`.

## F-11 · Automation that creates friction

- **What happened:** the routine proposed preparing follow-up drafts for accounts that
  had already received two touches, based on "Follow-up, day 15" lines in the files.
- **Correction:** the touch cap is verified against the email connector, not the files.
- **Test:** `EV-CAP-01`.

## Cases where the human decided better than the agent

| Situation | Human decision | Why it was better |
|---|---|---|
| ACCOUNT-B proposes two slots (a near slot or a slot five days later) | Choose the more distant one | An optimiser would have taken the nearer one, against the explicitly stated full calendar |
| ACCOUNT-D no-show recovery | A colloquial register and a direct phone call | The standard template would have been correct but cold at an awkward moment |
| ACCOUNT-N | No chaser | Relational context that was not present in any file |
| ACCOUNT-E, channel exhausted | Decide personally about the phone escalation | Channel escalation touches the founder's personal reputation |
