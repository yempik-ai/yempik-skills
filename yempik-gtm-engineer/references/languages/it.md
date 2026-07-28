# Language adapter: Italian (`it`)

Register rules for Italian customer-facing output. This file instantiates the
language-specific slots of `references/configuration.md` §3 for the reference market. The
universal writing constraints live in `references/doctrine.md` (D5) and are not restated
here.

The adapter is selected by `customer_language` (reference default: `it`).

**None of the preferences in this file was A/B tested.** They are the reference motion's
choices, recorded because they were used, not because they were proven. An installation that
adopts them unchanged has configured nothing.

---

## What this file owns

| Slot | What this adapter supplies |
|---|---|
| `register` | Formal address, dry professional tone |
| `recovery_register` | Warmer, colloquial, used after a no-show or a missed slot |
| `banned_tokens` | The em-dash, plus English loanwords toward the customer |
| `allowed_exceptions` | The loanwords declared one by one as permitted |
| `cta_wording` | The exact Italian CTA sentence |
| `subject_format` | The subject-line template |
| `product_name` | Where the product name appears in Italian copy |

Universal and therefore **not** owned here: `cta_count_per_message` (reference default: 1)
and `tracked_link_policy`. Both are doctrine D5 and apply in every language.

Before any customer-facing text is written, the installing company's binding writing rules
are read from `writing_rules_file`. That slot is a hard gate: it has no default and must
exist before the first run.

---

## Register (`register`)

The first touch uses the Italian formal address, the courtesy pronoun *lei*, never the
informal *tu*, and a dry professional tone.

- No exclamation marks.
- No superlatives, about the product or about the recipient.
- Professional recognition, not flattery: the first line cites what the account does, never
  how well it does it. See `references/anti-patterns.md` on decorative personalisation.

## Recovery register (`recovery_register`)

Recovery messages, sent after a no-show or a missed slot, warm up. The formal address is
kept; only the temperature changes. The reference motion named the likely cause without
assigning blame, in plain colloquial phrasing (observed: "immagino sia stata giornata di
fuoco, nessun problema davvero").

The rule behind the register is doctrine E5: a no-show is a hole in the calendar, so the
message removes friction instead of adding pressure.

---

## Banned tokens (`banned_tokens`)

### 1. The em-dash

Never, in any output.

Wrong:

> "<PRODUCT> prende in carico il lavoro [EM-DASH] dalla segnalazione alla chiusura
> [EM-DASH] senza cambiare gestionale."
>
> *(the character is written as a placeholder token: this file cannot contain it without
> violating the rule it documents.)*

Correct replacements: a colon, commas, parentheses, or a full stop.

Real error, day 1: an entire set of drafts was redone. On day 2 the rule was extended to
**every** company output, not only customer-facing copy, after an em-dash was found in a
quotation.

The rationale is typographic, not Italian: the em-dash is a tell, and text that reads as
machine-written contradicts on its own any claim the message makes about reliability. The
rationale carries into `references/languages/en.md`. The loanword ban below does not.

### 2. English loanwords toward the customer

Banned in Italian customer-facing copy: "workflow", "tool", "legacy" and the like. Founder
rule, day 7.

Wrong:

> "<PRODUCT> automatizza il workflow e sostituisce i tool legacy del vostro stack."

Correct: "flusso di lavoro", "strumento", "gestionale attuale".

Note the asymmetry. "Workflow" is the correct English word in this skill's own prose and in
the English adapter. The ban is about register in Italian, not about the concept.

## Allowed exceptions (`allowed_exceptions`)

Two, declared explicitly: **"call"** and **"test"**. Both are loanwords the founder already
used in their own writing.

The exception list is declared one word at a time. A loanword is allowed because it was
declared in advance, never because it sounded acceptable in the sentence being drafted.

---

## The Italian instances of the message rules

### First line

The formula is universal (`references/policies/04-message-craft.md`). Its Italian instance:

```
Le scrivo perché [ACCOUNT] [FATTO SPECIFICO VERIFICABILE]: è un contesto in cui
[CONSEGUENZA OPERATIVA DEL FATTO].
```

The fact must carry a `source_url`. The consequence is the only place where the agent
interprets, and it stays operational, never emotional.

### Subject line (`subject_format`)

Reference default: `<PRODUCT> × [ACCOUNT]: [promessa]`, where `<PRODUCT>` is the
`product_name` slot. Constant format, names the account and the promise. In the reference
motion the promise was a test on a single unit of the account's portfolio.

Never A/B tested.

### CTA (`cta_wording`)

Reference default: "una call di 25 minuti". An odd, specific number, read as a measured
request rather than an open-ended one.

Observed sentence:

> "Le andrebbe una call di 25 minuti? Le mostro cosa stiamo costruendo e capiamo rapidamente
> se può avere senso per lo studio."

The closing noun ("lo studio") is the market's word for the account and is market-specific;
see `references/markets/_template.md`. The structure is not: one question stating the CTA,
one sentence on what the call covers.

Exactly one CTA per message. That cap is doctrine, not preference.

Never A/B tested.

### Follow-up text

Standard text, same CTA, no additional personalisation. Observed opening:

> "torno brevemente sull'email della scorsa settimana. Stiamo selezionando tre studi per un
> test controllato..."

The follow-up is the multiplier, not extra personalisation (doctrine E3). Rewriting it per
account destroys the only comparison the motion has.

---

## Compliance checks

The active adapter populates `Message.compliance_checks.language_checks` in
`references/schemas/message.schema.json`. For Italian, both keys exist and both are required:

| Key | Passes when |
|---|---|
| `no_em_dash` | The draft contains no em-dash. |
| `no_anglicisms` | The draft contains no English loanword outside `allowed_exceptions`. |

A false value blocks delivery of the draft. It does not produce a warning.

---

## What is Italian here, and what is not

Read this table before writing an adapter for another language.

| Rule | Italian-specific? | Why |
|---|---|---|
| Formal address (*lei*) | Yes | The distinction does not exist in every language. |
| Warmer recovery register | No | The mechanism is doctrine E5; only the phrasing is Italian. |
| Em-dash ban | No | Typographic tell, language-independent. |
| English-loanword ban | Yes | A register rule about Italian copy. |
| Declared allowed exceptions | No | Every ban list needs an explicit exception list. |
| One CTA per message | No | Doctrine D5. |
| Tracked link at first product mention | No | Doctrine D5. |
| Subject format naming account and promise | No | The format is universal; the wording is not. |
| "25-minute call" | No | The mechanism (an odd, specific number) travels; the number is a preference. |
