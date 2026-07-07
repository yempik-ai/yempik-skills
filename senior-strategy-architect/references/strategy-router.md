# Strategy Router

Use this file to classify the request and choose the minimum playbooks needed. If multiple domains apply,
pick the primary bottleneck first, then add supporting playbooks.

## Universal routing rule

Map the user's wording to the business problem behind it, not just to keywords.

Examples:
- “Strategia marketing” may mean demand generation, positioning, content, paid acquisition, launch, or retention.
- “Business strategy” may mean model design, market selection, competitive advantage, operating model, or capital allocation.
- “Growth strategy” may mean acquisition, activation, retention, referral, monetization, or growth loops.
- “GTM” means launching or scaling a specific product/offering into a specific market with aligned product, marketing, sales, pricing, and success motions.

## Primary strategy types

### Marketing strategy
Use `playbooks/marketing-strategy.md` when the user wants to create demand, capture demand,
improve campaigns, choose channels, define audiences, improve messaging, or generate pipeline/revenue.

### Go-to-market strategy
Use `playbooks/go-to-market-strategy.md` when launching a new product, entering a new segment or market,
relaunching an offer, aligning sales/marketing/product, or moving from idea to revenue.

### Business strategy
Use `playbooks/business-strategy.md` when the user asks about business model, competitive advantage,
market selection, resource allocation, unit economics, portfolio, moat, or company-level direction.

### Growth strategy
Use `playbooks/growth-strategy.md` when the goal is user/customer growth, growth loops, funnel conversion,
activation, retention-led growth, referrals, virality, or experiment systems.

### Product strategy
Use `playbooks/product-strategy.md` when the user asks what to build, roadmap, product bets, PMF, UX priorities,
feature prioritization, product-market fit, MVP, or product metrics.

### Brand and positioning strategy
Use `playbooks/brand-positioning-strategy.md` when the request concerns brand identity, differentiation,
positioning, category narrative, message architecture, distinctive assets, or perception.

### Sales strategy
Use `playbooks/sales-strategy.md` for outbound, inbound sales, pipeline, sales process, enterprise selling,
buyer journey, qualification, demos, negotiation, sales scripts, or revenue team design.

### Pricing strategy
Use `playbooks/pricing-strategy.md` for price levels, packaging, value metric, discounting, tiers, freemium,
usage pricing, value-based pricing, margin, or monetization model.

### Content strategy
Use `playbooks/content-strategy.md` when the request concerns organic content, SEO, social content,
thought leadership, newsletter, creator/personal brand, editorial calendar, or sales-enablement content.

### Retention and monetization strategy
Use `playbooks/retention-monetization-strategy.md` when the user asks about churn, activation, engagement,
customer success, loyalty, upsell, cross-sell, NRR, repeat purchase, lifecycle marketing, or monetization.

### Competitive strategy
Use `playbooks/competitive-strategy.md` when the user asks how to beat, respond to, position against, or analyze competitors,
substitutes, market structure, strategic threats, or differentiation.

### Fundraising/investor narrative
Use `playbooks/fundraising-investor-narrative.md` for pitch decks, investor narrative, fundraising strategy,
seed/Series A story, market sizing, traction narrative, use of funds, or investor objection handling.

### Marketplace/platform strategy
Use `playbooks/marketplace-platform-strategy.md` for two-sided marketplaces, platforms, network effects,
liquidity, cold start, supply/demand seeding, take rate, or trust/safety.

### Partnerships/community strategy
Use `playbooks/partnerships-community-strategy.md` for partner ecosystems, co-selling, referral/reseller motions,
affiliates, integrations, community-led growth, ambassador programs, or member value.

## Bottleneck router

If the prompt is vague, classify by likely bottleneck:

| Symptom | Likely bottleneck | First playbook |
|---|---|---|
| People do not understand why they should care | Positioning/value proposition | brand-positioning, marketing |
| We have a product but no repeatable acquisition | Channel-market fit | gtm, growth, marketing |
| Many leads but few customers | Conversion, trust, sales process | sales, marketing, pricing |
| Paid ads work but margins are weak | CAC/payback/pricing/retention | pricing, retention, growth |
| Lots of content, little revenue | Content lacks strategic job | content, marketing, sales |
| Users sign up but disappear | Activation/retention | product, retention, growth |
| Competitors look similar | Differentiation/competitive advantage | competitive, brand, business |
| New product launch feels messy | GTM architecture | gtm |
| Founder needs investors | Narrative/proof/milestones | fundraising |
| Marketplace has empty demand or supply | Liquidity/cold start | marketplace |
| Community is active but business impact unclear | Business objective/member value mismatch | partnerships-community |

## Output routing

For ambiguous requests, do not say “it depends” and stop. Say:

1. “I’m treating this as [primary strategy type] because [reason].”
2. “I’m also borrowing from [secondary playbook] because [reason].”
3. “Assumptions: [short list].”
4. Continue with a useful strategy or ask high-impact questions.
