# GTM Engineering Anti-Patterns

Use this for critique, QA, and risk checks.

## Strategic Anti-Patterns

- Treating outbound as a campaign instead of a system.
- Starting with tools before ICP, pain, proof, and signal.
- Targeting "all B2B companies" or another broad segment.
- No exclusion criteria.
- No clear reason the prospect should care now.
- Confusing lead generation with qualified pipeline.

## Audience Anti-Patterns

- Filling a database without knowing why each account/person belongs there.
- Using job title only as ICP.
- Starting company-first when the buyer role is the real constraint.
- Starting people-first when account fit is the real constraint.
- No manual validation sample before scale.
- No confidence field for AI-enriched attributes.

## Signal Anti-Patterns

- Decorative personalization.
- Signals that do not connect to pain or urgency.
- AI-inferred facts used as if they were verified.
- Too many weak signals in one message.
- No negative signals or exclusions.

## Copy Anti-Patterns

- Generic compliments.
- Long intros about the sender.
- Feature dump.
- Multiple CTAs.
- Pushy follow-ups.
- Fake familiarity.
- Overpromising results without proof.
- Copy that would work unchanged for any company.

## Delivery Anti-Patterns

- Using the main corporate domain for risky cold outbound.
- Increasing volume to compensate for bad targeting.
- More than a conservative number of mailboxes per domain.
- Mixing warmup, outbound, and recovery settings casually.
- Ignoring bounce, SMTP, spam, and reputation signs.
- Treating deliverability as a setup task rather than a weekly operating concern.

## Measurement Anti-Patterns

- Celebrating open rate only.
- No reply categorization.
- No distinction between reply and positive reply.
- No meeting quality tracking.
- No decision log.
- Repeating the same campaign without learning what changed.

## Audit Prompt

When auditing, score each layer 1-5:

| Layer | Score | Evidence | Fix |
| --- | --- | --- | --- |
| Strategy | | | |
| Audience | | | |
| Signals | | | |
| Messaging | | | |
| Delivery | | | |
| Measurement | | | |

Then name the one bottleneck to fix first.
