---
name: clay-prospecting
description: >-
  Operational runbook for using the Clay MCP like a GTM engineer: targeted
  contact search, waterfall-style enrichment, custom research data points,
  credit discipline, and warm-path exclusion. Use WHENEVER the user asks to run
  Clay, enrich contacts or companies, find decision makers, build a prospect
  list, or get verified direct emails via the Clay MCP. Complements
  gtm-engineering-outbound (the strategy layer): this skill is the execution
  layer on the Clay MCP tools.
---

# Clay Prospecting

Run Clay like a GTM engineer: anchored to strategy, surgical with credits, hands off warm relationships. For strategy (ICP, messaging, deliverability systems) use `gtm-engineering-outbound`; this skill governs execution on the Clay MCP.

Reply in the user's language.

## Rule zero: the perimeter

**Clay is only for targets where no warm path exists.**

- People the user knows personally, sees regularly, or can reach through a direct intro: never enrich, never outbound. The channel is the relationship.
- 1st-degree connections and active relationships tracked in the user's CRM or company brain: same rule.
- If a target already sits in the user's pipeline as a warm or direct relationship, Clay is noise: stop.
- In doubt, ask the user BEFORE spending credits, not after.

## Rule one: context-first (never run blind)

Before any run, read and respect:

1. **The current strategic priority** (strategy docs, decision log if a company brain exists): the run must serve the active objective, not generic hunting. If it conflicts with an active decision, do not run it; flag it.
2. **The written ICP**: filters and exclusions come from documents, not improvisation.
3. **Existing lists** (BD folders, engagement logs, pipeline): the workspace usually already contains the candidates; Clay's job is to enrich them, rarely to discover from scratch.
4. **The user's tone-of-voice rules** for any copy produced.

## MCP runbook (the tools and how they chain)

The Clay MCP server exposes tool families that may rotate between sessions (e.g. `search-contacts` / `search-contacts-by-name` vs `find-and-enrich-contacts-at-company` / `find-and-enrich-list-of-contacts`). The flow is identical:

1. **Search/Find** → returns a `taskId` + contacts with base fields (name, title, company, LinkedIn). Key parameters: company domains (never bare company names), `job_title_keywords` for decision makers, low `limitPerCompany` (2-4), up to 10 domains per call.
2. **Enrich** → `add-contact-data-points` / `add-company-data-points` on that `taskId`. Standard points: `Email`, `Summarize Work History`, `Find Thought Leadership`. Custom points: any research question (prompting below).
3. **Poll** → `get-task-context`: enrichment is async ("in-progress" → "completed"). `"No results found."` is a definitive outcome, not an error: record it and plan the fallback (LinkedIn DM, generic inbox addressed to the person by name).
4. **Never** claim a data point does not exist without calling `get-task-context` first. Never fabricate values.

Channel fit (per Clay's own guidance): the MCP is for rep-scale, ad-hoc work on 1-20 targeted contacts. For 20+ volumes or recurring workflows, propose the Clay platform (tables/Functions) instead of forcing the MCP.

## Custom data point prompting (Claygent style)

- Second person, imperative: "Visit this company's website and check whether they sell AI services".
- Explicit fallback logic: "If there is no services page, check the blog; if nothing, answer 'not verifiable'".
- Constrained output format: "Answer only: YES / NO / not verifiable + one line of evidence".
- Keep outputs short (under 50 words): tokens cost credits.
- One question per data point, never bundled questions.

## Credit discipline (what experts actually do)

1. **Filter BEFORE enriching.** A row outside the ICP must never reach a paid enrichment. This is the single most expensive beginner mistake.
2. **Test small.** New search or custom prompt: 1-3 entities first, check output, then scale.
3. **Dedupe** on LinkedIn URL or domain+name before enriching (searches return duplicates).
4. **Enrich only what you will use.** If the motion is LinkedIn DM, the email data point is waste.
5. **One run = one written objective** (target, why now, which metric it serves). If you cannot write it, do not run it.

## Signals that qualify (strongest first)

1. Existing engagement (they commented on or posted about the user's themes) → first touch is a value comment, never a cold pitch.
2. They already use the relevant stack (fit = fast adoption).
3. Verbalized pain matching the offer → the exact pitch.
4. Dynamic triggers: recent job change (~90-day window), newly incorporated company, relevant hiring.
5. Static ICP fit alone is NOT enough for a first touch: require at least one dynamic signal on top.

## Output contract (a run produces artifacts, not chat)

1. **A file in the workspace**: person, role, company, motivated ICP fit, observed signal, first-touch channel, email with status (verified / not found / enriching).
2. **Facts separated from hypotheses.** Clay data are facts with a source; inferred fit is a marked hypothesis.
3. **First-touch drafts** from the user's approved templates, personalized on the real signal, one CTA.
4. **No autonomous sending.** Drafts only; sending is always the user's call. Suggested cadence: 2/day, follow-up after 4-6 days.
5. **Verify emails before any volume send** (keep bounce rate under 2%; below ~10 sends judgment is fine, above that use a dedicated verification pass).
6. **Log the run** (decision log, pipeline, open questions) and correct any stale data the run disproves.

## Anti-patterns (observed in real sessions)

- Enriching a contact the user could reach with a coffee. Ask about warm paths first.
- Expanding prospect lists while the active strategy says to reduce acquisition. The run serves the strategy, not the other way around.
- Wide, lukewarm blasts instead of few right touches: for high-touch programs, 9 true fits beat 30 names.
- Trusting the tool's first response: enrichment lands later; always `get-task-context` before concluding.
- Violating the user's copy rules in drafts (check tone-of-voice docs before writing).
