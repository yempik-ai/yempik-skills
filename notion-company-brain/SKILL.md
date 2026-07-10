---
name: notion-company-brain
description: >-
  Turn Notion into the team layer of a file-first company brain, with governance.
  Use this skill whenever a team wants to connect Notion (via the official Notion MCP)
  to a company brain that lives in versioned files: mapping the Notion workspace,
  deciding what syncs in which direction, defining conflict rules (which source wins),
  and enforcing safe writes (draft + human confirmation, no deletions, full audit log).
  Trigger when users say "sync our brain with Notion", "connect Notion to the company
  brain", "the team reads on Notion but strategy lives in files", or when an agent is
  about to write to a shared Notion workspace for the first time. Category term:
  "company brain".
---

# Notion as the team layer of a company brain

> Skill from the **cowork-os** kit. Pattern: **files are the source of truth, Notion is where the team reads and works, the agent keeps them aligned** through the official Notion MCP. Governance first, sync second.

## The problem this solves

Most company Notions are built in a week and grow organically. That is fine: Notion is where people actually read and collaborate. The problem starts when an AI agent gets write access to it with no rules. Unconfirmed hypotheses land next to confirmed decisions, pages get overwritten, nobody knows which version is true, and the knowledge base is polluted in days.

This skill sets up the governance BEFORE the sync. The technical connection takes minutes; the value is in the rules.

## The three roles

| Layer | Role | Source of truth for |
|---|---|---|
| **Files** (versioned repo: context, decisions, processes) | where strategy is reasoned and governed | strategy, positioning, decisions, processes |
| **Notion** | where the team reads and works daily | team-facing views, docs the team edits natively |
| **Transactional systems** (CRM, calendar, billing) | operational records | pipeline, deals, events, invoices |

Every piece of data gets exactly ONE source of truth. Everything else is a view.

## Phase 1: Map the Notion workspace

Never sync into a workspace you have not mapped. Inspect it (Notion MCP search/fetch) and fill the map with the user, one area at a time:

| Notion area | Database/page | Contains | Source of truth |
|---|---|---|---|
| _example: Strategy_ | _page/db id_ | positioning, plans | **files** (Notion = team read layer) |
| _example: Meeting notes_ | _db id_ | call transcripts | Notion (raw) → distilled into files |
| _example: Pipeline_ | _db id_ | deals, stages | **CRM** (Notion/files = view) |
| _example: Client intel_ | _db id_ | client sheets | shared, bidirectional (see conflict rules) |

Template: `templates/notion-map.md`.

## Phase 2: Decide what syncs, and in which direction

| Content | Syncs to Notion? | Direction | Why |
|---|---|---|---|
| Consolidated strategy / positioning | yes | files → Notion | the team reads it there |
| Active decisions | yes, summary only | files → Notion | only `active` status, never raw candidates |
| Client intelligence | yes | bidirectional | shared truth, conflict rules apply |
| Raw transcripts / inbox | inbound only | Notion → files | Notion is the source, files distill |
| Unvalidated hypotheses, open questions | **no** | stays in files | never pollute the shared knowledge base |
| Drafts and intermediate reasoning | **no** | stays private | only consolidated output ships |
| Sensitive data (pricing, personal data) | case by case | explicit approval only | never auto-push |

## Phase 3: Conflict rules (who wins)

Write these down explicitly with the user. Sensible defaults:

1. **Pipeline / transactional data** → the transactional system wins (CRM, not Notion, not files).
2. **Strategy / positioning / decisions** → the **files** win after a working cycle, then get pushed to Notion. Notion is not where strategy is edited.
3. **Shared content (e.g. client intel)** → the most recent version **with an explicit source** wins. If both sides are recent and diverge: **flag the conflict to the human, never resolve silently**.
4. **In doubt** → never overwrite Notion automatically. Propose a draft.

## Phase 4: Write rules (non-negotiable)

1. **No silent push. Ever.** Every write to Notion is draft + explicit human confirmation.
2. **Consolidated content only.** Facts and `active` decisions. Raw hypotheses stay in files.
3. **Cite source + date** on every synced block. Idempotent updates: update the existing page, never duplicate.
4. **No destructive operations.** The agent never deletes, archives, or moves pages or records. If something looks removable, it proposes the removal; a human executes it.
5. **Audit log.** Every executed write is appended to an action log (what, where, when, confirmed by whom). Template: `templates/action-log.md`.

## Cadence

Initial import in session, then fetch on demand when the team updates Notion. A periodic sync routine is optional and comes last, only after the map and the rules have survived a couple of weeks of real use.

## Failure modes to check before calling it done

- A write happened without confirmation → stop, log it, tighten the flow.
- The same fact lives in two places with no declared winner → go back to Phase 3.
- Notion contains hypotheses or drafts → clean up, revisit Phase 2 filters.
- The action log has gaps → writes are happening outside the governed path.

## What this skill does NOT do

It does not migrate or restructure the user's Notion, does not replace a CRM, and does not decide strategy. It governs the boundary between an agent, a file-based brain, and a shared Notion workspace.
