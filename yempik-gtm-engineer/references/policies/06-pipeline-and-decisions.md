# Policy 06: Pipeline Updates, Stop/Iterate/Scale, Bottleneck

## Pipeline updates

Mandatory order: evidence -> state -> CRM. Never the reverse.

Every row must contain: current evidence with date and time, source, next step with a date.
Written rule: "Every open opportunity must have a concrete date and next action."

### Advancement conditions (deterministic)

| From | To | Required event |
|---|---|---|
| `contacted` | `replied` | inbound human message (not an auto-reply) |
| `replied` | `meeting_set` | date **and** time explicitly agreed by both sides |
| `meeting_set` | `meeting_held` | the call took place |
| `meeting_held` | `pilot_verbal` | agreement on scope and price stated verbally |
| `pilot_verbal` | `pilot_signed` | signed document |
| `pilot_signed` | `invoiced` | invoice issued |

**No skipping is allowed.** ACCOUNT-A stays at `pilot_verbal` despite the enthusiastic
reaction, because there is no signature. This is the rule that protects the forecast.

### Prohibitions

- Do not convert "interested" into partner.
- Do not convert a call into a pilot.
- Do not convert a free setup into paying traction.
- Do not attribute an event of unknown origin to the campaign (the ACCOUNT-F case).

## Stop, iterate or scale

Weekly decision, explicit formula over a rolling window of `decision_window_accounts`
(reference default: 20) contacted accounts:

```
reply_rate      = human_replies / accounts_contacted
positive_rate   = positive_replies / accounts_contacted
meeting_rate    = meetings_set / accounts_contacted

if meeting_rate >= meeting_rate_scale (reference default: 0.10) [INFERENCE]
   and the calls produce useful qualification                          -> SCALE
if positive_rate >= positive_rate_floor (reference default: 0.10) [INFERENCE]
   and meeting_rate < meeting_rate_floor (0.05 [INFERENCE])
                                                                          -> ITERATE on CTA and reply handling
if reply_rate < reply_rate_floor (reference default: 0.05) [INFERENCE]  -> ITERATE on the list and the first line
if reply_rate >= icp_review_reply_rate (reference default: 0.15) [INFERENCE]
   and the calls do not qualify                                         -> ITERATE on ICP, not on copy
if stop_rule_conversations (reference default: 10) qualified conversations
   without convergence on a payable workflow                            -> STOP and revisit the wedge
```

The last one is the **stop rule written by the founder** in the approved shortlist file, not
an invention.

In this system, `SCALE` means increasing daily first touches from `max_first_touches_per_day`
(reference default: 3) to `scale_first_touches_per_day` (reference default: 5) **and nothing
else**: it does not mean widening the ICP or adding domains.

## Choosing the weekly bottleneck

Look at the first stage in the funnel, from the top, that is losing more than its expected
rate:

```
1. list          -> too many accounts without a citable signal
2. deliverability -> bounces or dead mailboxes > 10%
3. first line    -> reply_rate < 5%
4. CTA           -> positive replies that do not turn into a date
5. discovery     -> calls that do not produce qualification
6. offer         -> qualified accounts that do not buy
```

Work `bottleneck_focus_per_week` (reference default: 1) bottleneck at a time. In the observed
period, the real bottleneck was not generating replies (27%, high), but the conversion from
discovery to a paid pilot: 2 calls held, 0 paid pilots.

`[INFERENCE]` The numeric thresholds above are a reasonable formalisation; they were **not**
explicitly used during the period: the decisions were made by judgement. They must be
calibrated to the company installing the package. `stop_rule_conversations` is the one
exception: it was written by the founder before the campaign, not formalised after the fact.
