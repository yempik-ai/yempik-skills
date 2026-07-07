# Weekly GTM Review

Use this when the user has campaign metrics, wants optimization, or asks "what should we change?"

## Review Logic

Do not optimize one metric in isolation. Diagnose the layer:

- Delivery: did the message reach the inbox?
- Audience: were the right people/accounts contacted?
- Signal: was the relevance real?
- Messaging: did the angle create curiosity or rejection?
- Offer: did the prospect believe the outcome mattered?
- Reply handling: were replies converted into meetings/learnings?

## Weekly Scorecard

| Layer | Metric | What it tells you | Decision |
| --- | --- | --- | --- |
| Delivery | bounce, spam, SMTP, domain health | Can we safely send? | pause, recover, or continue |
| Reachability | open/reach trend where available | Are messages likely seen? | inspect delivery and subject |
| Audience | role/company fit sample | Are we contacting the right people? | refine filters/exclusions |
| Signal | signal accuracy sample | Is personalization based on truth? | fix enrichment/classification |
| Messaging | reply and positive reply | Is the angle working? | keep, rewrite, segment |
| Sales | meetings, opps, next steps | Are replies converting? | improve CTA/reply handling |
| Learning | objections and reasons | What should change? | update ICP, offer, or sequence |

## Diagnosis Patterns

### High Open / Low Reply

Likely issue:

- weak pain;
- generic copy;
- wrong buyer;
- CTA too heavy;
- signal not connected to business value.

Action:

- rewrite angle from signal to pain;
- segment audience more tightly;
- test a shorter CTA.

### Low Open / Low Reply

Likely issue:

- deliverability;
- bad subject/preview;
- wrong mailbox/domain setup;
- list quality.

Action:

- inspect domain/mailbox health;
- validate list sample;
- reduce volume until cause is clear.

### Replies But Low Positive Reply

Likely issue:

- pain not urgent;
- offer mismatch;
- wrong seniority;
- value prop unclear;
- proof not believable.

Action:

- categorize objections;
- split ICP;
- add proof or change wedge.

### Meetings But No Opportunities

Likely issue:

- qualification weak;
- CTA attracts curiosity but not intent;
- buyer lacks budget/authority;
- offer is too broad.

Action:

- tighten qualification;
- improve discovery and routing;
- adjust ICP or promise.

## Weekly Output

Use this structure:

```markdown
# Weekly GTM Review

## Verdict
[keep / adjust / pause / recover / scale]

## What happened
- Sent:
- Audience:
- Replies:
- Positive replies:
- Meetings:
- Delivery issues:

## Diagnosis
- Delivery:
- Audience:
- Signal:
- Messaging:
- Offer:

## Decisions
- Continue:
- Change:
- Stop:
- Test next:

## Next week
- [ ] Action
- [ ] Action
```

## Decision Rule

Scale only when:

- delivery is healthy;
- list sample is accurate;
- positive replies are meaningful;
- objections are understood;
- the team can handle replies and meetings.
