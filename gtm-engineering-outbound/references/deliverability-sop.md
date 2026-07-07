# Deliverability SOP

Use this for email infrastructure, warmup, scaling, and recovery guidance.
This is not legal advice and does not guarantee inbox placement.

## Non-Negotiables

- Protect domain reputation before chasing volume.
- Use separate outbound domains when risk is material.
- Keep a conservative mailbox-per-domain structure.
- Scale by adding healthy domains and mailboxes, not by pressuring one domain.
- Warmup, outbound, and recovery are different modes. Do not mix them casually.
- Pause or reduce when bounce, spam, SMTP errors, or reputation problems appear.

## Default Domain Structure

Conservative default:

- Max 3 mailboxes per outbound domain.
- New domains start with warmup only.
- Use custom tracking domains only if configured safely.
- Do not use the main corporate domain for aggressive cold outbound.

## Decision Flow

Before changing any setting:

```text
Is the domain new?
-> Warmup mode.

Was there a server/provider change, spam issue, SMTP error, or reputation drop?
-> Recovery mode.

Has the campaign been stable for 30-45 days?
-> Stable outbound mode.

Are replies good but capacity is capped?
-> Scale by adding domains/mailboxes, not pressure.
```

## Warmup Mode

Use for new domains/mailboxes.

Default guardrails:

- Warmup on.
- Outbound off for the initial warmup period.
- Gradual ramp only.
- Monitor reputation, SMTP errors, spam placement, and warmup reply behavior.
- Do not judge campaign performance during warmup.

## Transition Mode

Use after initial warmup when outbound starts for the first time.

Default guardrails:

- Keep warmup on.
- Start with low daily outbound per mailbox.
- Use short sequences.
- Use highly qualified ICP only.
- Avoid broad scale-up.

## Stable Outbound Mode

Use only after the system is stable.

Default guardrails:

- Increase volume gradually.
- Keep sequences short unless reply quality justifies more steps.
- Track by mailbox and domain, not only aggregate campaign results.
- Separate audience/copy problems from delivery problems.

## Recovery Mode

Use after reputation, spam, SMTP, or bounce problems.

Default guardrails:

- Stop scaling.
- Reduce or pause outbound.
- Keep/restart warmup depending on tool and situation.
- Isolate whether the issue is list quality, domain reputation, content, provider, or volume.
- Resume only after reputation and error signals stabilize.

## Red Flags

- High bounce rate.
- Sudden open-rate collapse across several mailboxes.
- SMTP errors.
- Spam complaints.
- Reputation drop.
- Positive replies fall while negative replies rise.
- One domain carries too much of the sending load.
- The campaign uses weak or scraped data with no validation sample.

## Metrics To Track

- Sent volume by mailbox/domain.
- Bounce rate.
- Open/reachability trend where available.
- Reply rate.
- Positive reply rate.
- Spam/error signals.
- Meetings booked.
- Objection categories.
- Domain/mailbox health.

## Stop Conditions

Recommend pausing or reducing if:

- deliverability errors are increasing;
- bounce quality is not under control;
- the list source changed and quality is unknown;
- the team is increasing volume to compensate for weak messaging;
- the same domain is being pushed harder instead of adding infrastructure.
