# Deliverability Checklist

## Domain And Mailbox Setup

- [ ] Outbound does not rely on the main corporate domain for risky cold outreach.
- [ ] Mailboxes per domain are conservative.
- [ ] DNS/authentication is configured and checked.
- [ ] Tracking domain setup is intentional.
- [ ] Each mailbox has clear ownership and status.

## Mode

- [ ] Warmup
- [ ] Transition
- [ ] Stable outbound
- [ ] Recovery

## Before Sending

- [ ] List sample manually validated.
- [ ] Bounce risk checked.
- [ ] Copy avoids spammy patterns.
- [ ] Volume is appropriate for domain/mailbox age.
- [ ] Stop conditions are defined.

## Weekly Health

| Domain | Mailboxes | Sent | Bounce | Replies | Positive replies | Errors | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Red Flags

- [ ] Bounce increase.
- [ ] SMTP errors.
- [ ] Spam/reputation signal.
- [ ] Sudden open/reach collapse.
- [ ] Negative replies increasing.
- [ ] Volume increased despite weak audience or messaging.

## Decision

- [ ] Continue.
- [ ] Reduce.
- [ ] Pause.
- [ ] Recovery.
- [ ] Add infrastructure before scaling.
