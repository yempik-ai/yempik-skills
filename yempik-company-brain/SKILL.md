---
name: yempik-company-brain
description: Use when Yempik Company Brain MCP tools (brain_standing_rules, brain_search, brain_propose_item) are available and the task is estimating, quoting, pricing, setting margins, writing a proposal or a plan, or drafting an email or document for a client or partner; when the conversation surfaces durable company knowledge (a decision confirmed, a rule or process stated, a pricing change, a client or vendor fact); or when answering questions that touch company knowledge (pricing, clients, positioning, processes, past decisions).
metadata:
  author: yempik
  homepage: "https://brain.yempik.ai"
  version: "1.2.0"
---

# Yempik Company Brain

## Overview

The Company Brain is the workspace's governed memory: decisions, processes, rules, facts,
glossary, people, and clients, curated by humans. Core principle: **capture proactively,
propose-only**. A durable fact that lives only in a chat log is lost to the company;
proposing it costs one low-risk call: `brain_propose_item` creates a pending candidate in
a human review Inbox and can never activate truth or cause external effects. Humans ratify
or reject from the Inbox; you never publish truth directly.

## Standing rules first

Some of the Brain is not background: it is the owner's standing rules: how the company
prices, staffs, quotes and commits. A search ranks them by word overlap with everything
else, so a task phrased in the client's words can miss the rule that governs it. The
Brain therefore serves them in one call instead of leaving them to be searched for.

Before **any** estimate, quote, price, margin, plan, proposal, email or document for a
client or partner:

1. Call `brain_standing_rules` (input `{}`, optional `as_of`) **once per session**. It
   returns every active rule that binds, with a `rules_hash`. The same hash travels as
   `standing_rules_hash` on `whoami` and `brain_search`: when it differs from the one you
   fetched, the rules changed: fetch them again.
2. Then `brain_search` with **the task's own words** ("preventivo sito per un nuovo cliente, 3 mesi"),
   not the Brain's vocabulary, for the facts specific to this client and this job.
3. Apply the rules. They bind unless the owner overrides them in the conversation. When you
   depart from one, because the owner told you to, say which rule you are overriding, by
   title or id, in the deliverable or in your reply. Never drop a rule silently, and never
   override one on your own judgement: if a rule looks wrong for this case, apply it and
   say why you would question it.

A rule with standing `proposed` binds too: it is the owner's stated intent, not yet
ratified. Apply it and say it is not yet ratified.

## When to capture

Propose when a turn contains any of these:

- A decision is confirmed ("ok, let's do X", "confermiamo", "we're going with...")
- A rule or standing process is stated ("from now on...", "the policy is...")
- Pricing, positioning, or product scope changes
- A durable client/vendor fact emerges: contract terms, constraints, key contacts, an
  explicit refusal or do-not-contact signal

Do NOT propose: ephemeral or task-local details, secrets or credentials, personal data
irrelevant to company operations. Options still being weighed are not a decision: propose
them only when the owner's reasoning is worth keeping for later, and then as `brainstorm`.

## The capture protocol

1. **Session start:** call `whoami` once: you need the `brain:propose` scope; if missing,
   tell the user to adjust the grant in Yempik Connections.
2. **Dedup first:** `brain_search` the topic and `brain_list_items` with state
   `"candidate"`. If an active item already covers it and the new information updates or
   contradicts it, use `brain_propose_revision` (target_item_id, full revised body_md,
   reason). If a live candidate already covers it, stop: do not pile on duplicates.
3. **Propose:** `brain_propose_item` with type `decision|process|rule|fact|glossary|person|client`,
   a specific title, and a body that states the fact, its scope, and any date or condition.
   Pass `epistemic_status` by classifying **the speech act, not the topic**. Not everything
   the owner says is a rule; sometimes it is reasoning worth keeping for later:
   - `proposed`: the owner states intent or a rule: "da ora in poi", "confermiamo",
     "la regola è", "decido", "from now on", "we're going with". The owner's own words
     are never a `hypothesis`.
   - `brainstorm`: reasoning and options kept for later: "pensavo", "ragioniamo",
     "potremmo", "e se…". Never a rule.
   - `hypothesis`: an inference or working assumption: "ipotesi", "forse", "probabilmente",
     or something *you* inferred rather than the owner stated. Binds nobody.
   - `verified`: only for a fact checked against a source you cite.
   Never claim `ratified`: only the Inbox reviewer ratifies. Same topic, different acts:
   "da ora in poi le offerte valgono 30 giorni" is a `proposed` rule; "pensavo a offerte
   valide 30 giorni, ragioniamoci" is a `brainstorm`.
4. **request_id:** a fresh UUID per proposal. Reuse the same UUID only to retry the same
   proposal (idempotent), never for a different one.
5. **Tell the user in one line** what you proposed and that it is pending in the Inbox.
6. **Never block the main task:** propose alongside the user's actual request, not instead
   of it.

When you are about to make more than two or three related proposals (importing a document, restructuring a
process, retiring what a new decision replaced), open a changeset first and pass its `changeset_id` to every
proposal. One person reviews one diff instead of twenty cards, and `brain_get_changeset` tells you what they
decided. A line you cannot read is reported as a count, not hidden: say so rather than describing the batch
as complete.

A whole document (a process page, a spec, an interview) goes through `brain_propose_document`: the markdown
body, an item type, a `document_type` (canonical > specification > research_note > interview >
marketing_draft > mockup), and, non-negotiable, its connections: the entities and relations the document
explicitly names, or `standalone: true` with a reason when it genuinely connects to nothing. A proposal that
declares neither is rejected. For a corpus, the `kb-import` routine is the shape: `routine_start_run`, open
one changeset, propose up to `max_documents` documents into it (the shared 60/hour propose budget, common to every agent on the
owner's grants, is the ceiling: pace, don't fight it), checkpoint after each, then `routine_complete_run` with `changeset_id` so
the platform submits the batch for review. A larger corpus takes further runs, each with its own changeset.

To merge duplicate entities, `brain_propose_entity_merge` accepts `entity_ids` for 2 to 4 entities of the same
visibility, `surviving_entity_id`, `reason`, and required `changeset_id`. It proposes a candidate only: do
not delete or archive entities, and do not execute an approved merge yourself; the platform executes only
after a human approval. For one-domain cleanup, `kb-refactor` is the shape: `routine_start_run`, open one
changeset that states the domain, propose revisions, retirements, relations, and merges bound to it (at most
`max_proposals`), checkpoint after each, then `routine_complete_run` with `changeset_id`.

## Routines: the server never schedules you

External routines are governed by the platform but executed, and timed, by you, the
client. MCP is inbound-only: no cron on the server side will ever wake you. Once a human
activates a routine from the Inbox, read `routine_describe_contract.scheduling`:

- `mode: "recurring"`: create a scheduled task in your own environment (Claude scheduled
  tasks, ChatGPT tasks, a cron job) that runs the lease protocol (`routine_start_run` →
  `routine_get_context` → do the work → `routine_checkpoint_run` → `routine_complete_run`)
  at `default_cadence`, or at whatever cadence the workspace agreed on at activation.
  Choose where the schedule lives: when the work only needs connectors, prefer a CLOUD
  scheduled task, because a local one runs only while the machine is awake, and a missed cadence
  shows up as overdue in the workspace. Schedule locally only when the work genuinely
  needs local files or tools; when the output is durable knowledge, propose it to the
  Brain instead of writing a local file, so any client can read it.
- `mode: "on_demand"`: never schedule it. Run it when the user asks: an import or a
  cleanup is a project, not a routine.

The full mounting flow, end to end: `routine_list_templates` → `routine_describe_contract`
→ `routine_validate_config` → `routine_propose` → a human activates in the Inbox → you
create the client-side schedule → each firing runs the lease protocol. Durable findings
come back as candidates in the same Inbox: the schedule lives with you, the truth stays
governed.

## Grounding

For decision questions, objections or convictions, call `brain_decision_brief` before search.

Before answering other questions that touch company knowledge (pricing, clients, positioning,
processes, past decisions): `brain_search` first, answer from the results, cite them.
Trust `epistemic_status` over title wording: only `ratified` or `verified` is decided;
`proposed` is the owner's stated intent: apply it and say it is not yet ratified;
`hypothesis` is an inference that binds nobody; `brainstorm` is reasoning kept for later,
never a rule.
For "what is our current position on X" use `brain_get_current_decision`: it follows
supersede chains. For multi-domain strategy questions only, use `brain_resolve_question`.

When one search does not settle it (who a client works with, what a decision depends on),
follow the connections with `brain_neighbors` instead of running three more searches.
`brain_neighbors` shows ratified connections only; the pending ones come back from
`brain_read_item` and `brain_get_entity`. Connections and items marked `candidate` are
proposals under review: cite them only while saying so.

When the topic is an initiative, product, client or concept the Brain tracks (the same
question answered differently in two campaigns, a price that holds in one track and not
another), find the node with `brain_list_entities` and call `brain_get_context_view`: it
returns every initiative the subject takes part in, with the claims inside each and the
contradictions between them. Keep each claim inside the initiative it belongs to, cite at
most three claims per initiative, the ones that bear on the question, and say how many you
left out; quote qualifiers like "HYPOTHESIS" or "non ratificato" verbatim, and name the
conflicts before reasoning past them. Coexisting truths are normal here.

### La forma della risposta

These six rules apply to every answer that touches the Brain, not only after
`brain_get_context_view`. They are in Italian because that is the language the owner asks
and reads in.

1. Rispondi in **massimo 12 righe / ~900 caratteri**. Cita al massimo **5 item** e chiudi con
   "Nel Brain ce ne sono altri N: te li apro?". **Non elencare mai tutto quello che il Brain ha.**
2. Struttura fissa: **Posizione registrata · Cosa la contraddice o la limita · Alternative già
   considerate · Cosa manca per decidere · Cosa cambierebbe il quadro.** Salta una sezione solo
   se è vuota, e dillo.
3. **Un'ipotesi non è mai una precondizione.** Non scrivere mai "prima di X bisogna Y" citando
   un item `hypothesis` o `brainstorm`: scrivi "Y è un'ipotesi del <data>, non un vincolo".
   **Una proposta dell'owner si applica e si dichiara non ancora ratificata:** un item
   `proposed` vale come indicazione dell'owner: "Y (proposta dell'owner del <data>, non
   ancora ratificata)".
4. **L'owner può contraddire il Brain.** Se la sua convinzione confligge con un claim, registra
   la convinzione, nomina il claim che la limita e chiedi se aggiornarlo, senza correggerlo
   dall'alto.
5. **Dichiara sempre la solidità** di ciò che citi: deciso / proposto dall'owner / ipotizzato /
   aperto. Non promuovere mai un'ipotesi a decisione, nemmeno per brevità, e non declassare
   una proposta dell'owner a ipotesi.
6. **Porta un'alternativa non richiesta** quando il Brain ne registra una: una riga, con l'id, e
   la condizione che la riaprirebbe.

## Rationalizations

| Excuse | Reality |
|---|---|
| "The user didn't ask me to save this" | Proactive capture is the point. Propose-only means a human reviews it: you are not publishing. |
| "It might be a duplicate" | That is what step 2 is for. If the search comes back clean, propose. |
| "Writing feels risky" | It cannot activate truth or touch external systems. Reading and proposing carry the same risk: none. |
| "I'll capture it at the end" | Sessions get truncated. Propose when the fact emerges. |
| "It's just a quick estimate, the rules won't matter" | Estimates are exactly where the owner's rules live. One `brain_standing_rules` call per session is the cost. |
| "The owner said it, but I'm not sure it's final" | Then it is `proposed`, not `hypothesis`: the owner's stated intent, applied and flagged as not yet ratified. |

## Red flags

- A decision was confirmed in conversation and the session ends with zero proposals.
- You answered a pricing/client question from memory without calling `brain_search`.
- You estimated, quoted, priced or drafted a client document without calling
  `brain_standing_rules`.
- You departed from a standing rule without naming the rule you overrode.
- You proposed the owner's "da ora in poi" as `hypothesis`, or their brainstorming as a rule.
- You reused a request_id for a different proposal.

## Quick reference

| Need | Tool |
|---|---|
| Before an estimate, quote, plan or client document | `brain_standing_rules` once per session, then `brain_search` with the task's words |
| Ground an answer | `brain_search`, then `brain_read_item` |
| Current position on X | `brain_get_current_decision` |
| New durable fact | `brain_propose_item` |
| Update/contradict an active item | `brain_propose_revision` |
| Check what happened to a proposal | `brain_get_proposal_status` |
| Pending candidates (dedup) | `brain_list_items` with state `"candidate"` |
| Who/what connects to X | `brain_neighbors` from the item or entity |
| Everything about a client/person/product | `brain_list_entities`, then `brain_get_entity` |
| The initiatives a topic belongs to, side by side | `brain_get_context_view` |
| A bounded decision question, objection or conviction | `brain_decision_brief` first |
| A relationship the Brain does not record | `brain_propose_relation` (both endpoints must exist) |
| A whole document, connections declared | `brain_propose_document` (or the `kb-import` routine for a corpus) |
| Many related proposals at once | `brain_open_changeset`, pass `changeset_id`, then `brain_submit_changeset` |
| Knowledge that no longer holds | `brain_propose_retirement` (inside a changeset) |
| A proposal you now know is wrong | `brain_withdraw_proposal`, or `brain_withdraw_changeset` for the whole batch |
| A routine that should run daily/weekly | client-side scheduled task running the lease protocol (see `scheduling` in the contract) |
