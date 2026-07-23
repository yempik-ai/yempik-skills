---
name: yempik-company-brain
description: Use when Yempik Company Brain MCP tools (brain_search, brain_propose_item) are available and the conversation surfaces durable company knowledge — a decision confirmed, a rule or process stated, a pricing change, a client or vendor fact — or when answering questions that touch company knowledge (pricing, clients, positioning, processes, past decisions).
metadata:
  author: yempik
  homepage: "https://brain.yempik.ai"
---

# Yempik Company Brain

## Overview

The Company Brain is the workspace's governed memory: decisions, processes, rules, facts,
glossary, people, and clients, curated by humans. Core principle: **capture proactively,
propose-only**. A durable fact that lives only in a chat log is lost to the company;
proposing it costs one low-risk call — `brain_propose_item` creates a pending candidate in
a human review Inbox and can never activate truth or cause external effects. Humans ratify
or reject from the Inbox; you never publish truth directly.

## When to capture

Propose when a turn contains any of these:

- A decision is confirmed ("ok, let's do X", "confermiamo", "we're going with...")
- A rule or standing process is stated ("from now on...", "the policy is...")
- Pricing, positioning, or product scope changes
- A durable client/vendor fact emerges: contract terms, constraints, key contacts, an
  explicit refusal or do-not-contact signal

Do NOT propose: ephemeral or task-local details, options still being weighed, secrets or
credentials, personal data irrelevant to company operations.

## The capture protocol

1. **Session start:** call `whoami` once — you need the `brain:propose` scope; if missing,
   tell the user to adjust the grant in Yempik Connections.
2. **Dedup first:** `brain_search` the topic and `brain_list_items` with state
   `"candidate"`. If an active item already covers it and the new information updates or
   contradicts it, use `brain_propose_revision` (target_item_id, full revised body_md,
   reason). If a live candidate already covers it, stop — do not pile on duplicates.
3. **Propose:** `brain_propose_item` with type `decision|process|rule|fact|glossary|person|client`,
   a specific title, and a body that states the fact, its scope, and any date or condition.
4. **request_id:** a fresh UUID per proposal. Reuse the same UUID only to retry the same
   proposal (idempotent) — never for a different one.
5. **Tell the user in one line** what you proposed and that it is pending in the Inbox.
6. **Never block the main task:** propose alongside the user's actual request, not instead
   of it.

## Grounding

Before answering anything that touches company knowledge (pricing, clients, positioning,
processes, past decisions): `brain_search` first, answer from the results, cite them.
For "what is our current position on X" use `brain_get_current_decision` — it follows
supersede chains. For multi-domain strategy questions only, use `brain_resolve_question`.

## Rationalizations

| Excuse | Reality |
|---|---|
| "The user didn't ask me to save this" | Proactive capture is the point. Propose-only means a human reviews it — you are not publishing. |
| "It might be a duplicate" | That is what step 2 is for. If the search comes back clean, propose. |
| "Writing feels risky" | It cannot activate truth or touch external systems. Reading and proposing carry the same risk: none. |
| "I'll capture it at the end" | Sessions get truncated. Propose when the fact emerges. |

## Red flags

- A decision was confirmed in conversation and the session ends with zero proposals.
- You answered a pricing/client question from memory without calling `brain_search`.
- You reused a request_id for a different proposal.

## Quick reference

| Need | Tool |
|---|---|
| Ground an answer | `brain_search`, then `brain_read_item` |
| Current position on X | `brain_get_current_decision` |
| New durable fact | `brain_propose_item` |
| Update/contradict an active item | `brain_propose_revision` |
| Check what happened to a proposal | `brain_get_proposal_status` |
| Pending candidates (dedup) | `brain_list_items` with state `"candidate"` |
