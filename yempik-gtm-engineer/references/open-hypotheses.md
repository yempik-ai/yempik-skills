# Open hypotheses

Four hypotheses read like rules but were never demonstrated. Each is kept with its
counter-evidence: a hypothesis separated from its counter-evidence becomes a rule by
accident. A learning candidate built on any of these still needs `min_sample_size_for_rule`
(reference default: 30) before it can move from candidate to ratified.

## H1 [H] The 0-12 score predicts conversion

**Not validated.** It orders the queue, but accounts at 10/12 did not reply, and an
account at 9/12 converted in 38 minutes. Test proposed in the eval suite.

## H2 [H] A named mailbox converts better than a department mailbox

**Not validated, and partly contradicted:** ACCOUNT-C, a department mailbox, converted
in 38 minutes; ACCOUNT-M, a named mailbox, never replied. A plausible hypothesis, not
demonstrated.

## H3 [H] The tracked link click as a warm signal

The hypothesis is that a click without a reply indicates interest. **Never verified:**
the web analytics connector was never consulted in the observed period.

## H4 [H] The "published method" signal is the strongest

Based on a single case (ACCOUNT-A, the only reply on the first touch). To be tested on
at least 10 accounts.

---

## Not yet generalizable

Distinct from the four hypotheses above: these are choices that worked once, in one
motion, and have not been tested against alternatives or at scale. Do not port any of
them unchanged into a new market or a new company; re-derive each one.

| Element | Why it is not yet generalizable |
|---|---|
| The four specific angles | Valid for a market with vertical incumbent systems and multi-office accounts. |
| The `followup_window_days` threshold (4-5 days) | Observed across 26 accounts over the campaign window; seasonality and sector are not controlled for. |
| The `cta_wording` (a 25-minute call) | Never tested against alternatives. |
| The weight of the "published method" signal | A single case (see H4 above). |
| The `stop_rule_conversations` threshold (10 qualified conversations) | A founder decision for this product, not a law. |
| The conversion rates | Sample too small to be a benchmark. |
| The warmer register used in recovery messages (`recovery_register`) | The founder's personal preference, not a demonstrated rule. |
