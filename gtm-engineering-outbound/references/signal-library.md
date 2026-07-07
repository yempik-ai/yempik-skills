# Signal Library

Use this when building ICP criteria, enrichment prompts, list schemas, or message angles.

## What Counts As A Signal

A signal is an observable fact that makes a prospect more relevant, urgent, qualified, or segmentable.

Good signal:

- "Company runs active TikTok ads but has low organic video quality."
- "Founder recently changed role/title and is likely rebuilding GTM."
- "Company uses HubSpot but appears under-resourced for implementation."

Weak signal:

- "Company has a website."
- "Founder posted on LinkedIn."
- "They have a nice mission."

## Signal Map Columns

Use this schema:

| Signal | Source | Enrichment method | Why it matters | Copy angle | Confidence | Caveat |
| --- | --- | --- | --- | --- | --- | --- |

## Common Signal Families

| Family | Examples | Useful for |
| --- | --- | --- |
| Firmographic | industry, size, geography, funding, revenue proxy | Fit and list filtering |
| Technographic | HubSpot, Shopify, Criteo, The Trade Desk, analytics tools | Pain inference and replacement/integration angles |
| Hiring | open roles, new GTM hires, sales/marketing hiring | Growth, budget, urgency |
| Leadership change | new CEO, founder role change, new VP Sales/Marketing | Timing and strategic reset |
| Content/community | follows a relevant page, joins community, attends event, posts on topic | Awareness and warm relevance |
| Ads/activity | Meta Ads Library, Google presence, TikTok activity, TV/video ads | Marketing maturity and budget |
| Website quality | outdated site, no booking flow, poor localization, weak conversion path | Service/agency angles |
| Team gap | no designer, no RevOps, no performance marketer, small GTM team | Capacity pain |
| Compliance/process | public certifications, sustainability report, security page gaps | Regulated/enterprise angles |
| Marketplace/reviews | low rating, review themes, recent openings, franchise growth | Local and multi-location plays |

## B2B SaaS / Services

Candidate signals:

- Uses a target tool: HubSpot, Salesforce, Intercom, Shopify, Webflow, Criteo, The Trade Desk.
- Hiring for sales, SDR, RevOps, paid media, lifecycle, or partnerships.
- Recently funded or launched a new market/product.
- Founder or GTM leader changed title recently.
- Has case-study gap, pricing ambiguity, weak onboarding, or unclear positioning.
- Active in a relevant LinkedIn community or follows a niche page.

## Local Business

Candidate signals:

- New opening or expansion.
- High review volume but repeated negative themes.
- No booking/reservation flow.
- Website/mobile friction.
- Active local ads.
- Franchise or multi-location growth.
- Seasonal demand patterns.

## E-commerce

Candidate signals:

- Shopify/WooCommerce/Magento stack.
- Active Meta/TikTok ads.
- Poor creative quality or inconsistent posting.
- High product count but weak collection/category structure.
- International shipping or localization gap.
- Amazon marketplace presence or absence.
- Review themes around delivery, sizing, support, or product clarity.

## Company-First vs People-First

Start **company-first** when account criteria matter most:

- industry, size, stack, ads, funding, location, business model.

Start **people-first** when reachable buyer presence matters most:

- job title, seniority, community membership, LinkedIn behavior, recent role change.

People-first is often safer for outbound because it confirms at least one reachable buyer exists.

## Enrichment Rules

- Use deterministic filters first: geography, industry, size, job title.
- Use AI classification for criteria that databases do not store cleanly: B2B/B2C, producer/non-producer, creative quality, maturity, team gap.
- Validate a manual sample before scaling.
- Keep a confidence column. Not every AI-inferred signal should drive copy.
- Store negative signals and exclusions, not only positives.
