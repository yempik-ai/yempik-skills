---
name: reply-classifier
description: Classifies one raw inbound reply thread into the closed 8-class reply taxonomy, quoting the literal sentence that determines the class. It classifies and nothing else, never advancing a state, writing a draft or updating a file.
---

# Reply classifier

Takes one raw reply thread and returns its class. Nothing else.

**Why it is isolated:** a full thread is bulky and its wording matters only to this decision.
Classification is also the point where an agreeable reading inflates the pipeline, so it is
worth doing against the taxonomy alone, with no draft to write and no state to advance.

## Input

The raw thread: the inbound message body, its sender and date, and the outbound message it
replies to. Do not classify from a subject line or a snippet.

## Procedure

1. **Auto-reply detection first, before anything else.** An out-of-office, a "your message has
   been assigned to the relevant department", a ticketing acknowledgement: these are
   `auto_reply`. **An auto-reply is never interest and changes no state.** This check runs
   first because every downstream reading of an automatic acknowledgement is wrong.
   Exception worth catching: an automatic reply that names a colleague is `internal_routing`,
   not `auto_reply`, because it hands you a new stakeholder.
2. **Classify** against the closed taxonomy in `references/policies/05-reply-handling.md`. The
   eight values are the `Message.reply_class` enum and the set is closed: do not coin a ninth.

| Class | Recognised by |
|---|---|
| `interest_with_slot` | the prospect proposes a date and a time |
| `interest_without_slot` | interest declared, no date |
| `information_request` | questions about the product |
| `deferral` | an explicit future date |
| `refusal` | an explicit no |
| `auto_reply` | out of office, automatic acknowledgement |
| `internal_routing` | points to a named colleague |
| `bounce` | mailer-daemon, decommissioned mailbox |

3. **Quote literally.** Return the exact sentence that determines the class, verbatim, as
   `reply_quote`. A paraphrase is what inflates interest, which is why the field exists.
4. **When it is ambiguous, present both readings** with the sentence supporting each, and say
   which action each implies. Do not pick one to be helpful. An ambiguous reply resolved in the
   optimistic direction is how a `replied` row becomes a fictional `meeting_set`.
5. **Never advance state.** This pass proposes a class and a recommended action; the state
   change belongs to the calling routine, and only on a dated, verifiable event. If the class
   contradicts the pipeline row, report the discrepancy instead of correcting either side.

## Output

```json
{
  "thread_id": "",
  "reply_class": "interest_without_slot",
  "reply_quote": "the literal determining sentence, verbatim",
  "ambiguous": false,
  "alternative_reading": null,
  "recommended_action": "propose 2-3 concrete slots",
  "state_change_proposed": "none",
  "pipeline_discrepancy": null
}
```

When `ambiguous` is `true`, `alternative_reading` carries the second class and its own
supporting quotation, and `recommended_action` names the action for each reading rather than
choosing between them.
