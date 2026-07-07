# GTM Engineering Operating Model

Use this when designing or auditing the whole outbound system.

## System Definition

GTM engineering is the operating layer between strategy and execution. It converts:

- vague target -> explicit ICP and exclusions;
- generic lead list -> qualified audience with signals;
- AI copy -> controlled messaging based on real context;
- one-off campaign -> repeatable outbound asset;
- vanity metrics -> learning loop and decisions.

## Five Stages

1. **Strategic base**: offer, ICP, pain, proof, urgency, buying context.
2. **Audience build**: accounts/people, sources, filters, enrichment, validation.
3. **Signal design**: observable facts that justify relevance and segmentation.
4. **Messaging and delivery**: short copy, sequence, channel, mailbox plan.
5. **Measurement loop**: replies, objections, meetings, deliverability, next iteration.

## System Artifacts

A serious outbound system should produce these files or sections:

- GTM system brief.
- ICP and exclusion criteria.
- Signal map.
- List schema with sources and validation rules.
- Copy and sequence.
- Delivery and deliverability checklist.
- Reply handling and objection categories.
- Weekly review log.
- Decision log: what changed and why.

## Stage Diagnosis

| Stage | Symptom | Main job |
| --- | --- | --- |
| Idea | "We want leads" | Define ICP, pain, proof, and wedge |
| Prototype | First list/copy exists | Validate signals and message relevance |
| Stable | Some replies/meetings | Improve conversion and repeatability |
| Scale | Working segment/channel | Add domains, lists, enablement, review cadence |
| Recovery | Deliverability or reply quality collapsed | Pause pressure, isolate cause, recover reputation |

## Default Stack Pattern

Use categories, not fixed vendors unless the user already has tools:

- AI model for strategy, classification, summarization, and enrichment prompts.
- Data/enrichment tool such as Clay or equivalent.
- Email sequencer/delivery tool such as Smartlead or equivalent.
- CRM or spreadsheet for pipeline and reply outcomes.
- Verification sources: company website, LinkedIn, directories, ads libraries, job boards, review sites, tech stack tools.

Current tool pricing, plans, and limits change often. Verify before advising budgets.

## System Principle

The goal is not "more automation." The goal is fewer arbitrary decisions:

- why this account;
- why this person;
- why now;
- why this message;
- why this channel;
- what we learned from the result.
