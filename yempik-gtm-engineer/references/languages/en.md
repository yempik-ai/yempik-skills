# Language adapter: English (`en`)

Register rules for English customer-facing output. This file instantiates the
language-specific slots of `references/configuration.md` §3 when `customer_language` is set
to `en`. The universal writing constraints live in `references/doctrine.md` (D5) and are not
restated here.

**`[INFERENCE]`. No English message was sent in the reference motion.** Every rule below is
derived by principle from `references/languages/it.md`: the mechanism was observed in
Italian, the English wording was not. There is no `en-exemplars.md`, because there is nothing
to put in it. The first installation to run this adapter should record what it sends and
replace the derived defaults with observed ones.

---

## What carried over, and what did not

| Italian rule | Carries to English? | Why |
|---|---|---|
| Em-dash ban | **Yes** | The rationale is typographic, not Italian: the character is a tell that the text was machine-written, and that contradicts on its own any reliability claim the message makes. |
| One CTA per message | **Yes** | Doctrine D5, universal. |
| Tracked product link at the first product mention | **Yes** | Doctrine D5, universal. |
| Subject format naming the account and the promise | **Yes**, as a format | The template travels; the wording does not. |
| A declared list of allowed exceptions | **Yes** | Every ban list needs an explicit exception list, or the ban is negotiated per draft. |
| Warmer register in recovery messages | **Yes** | The mechanism is doctrine E5; only the phrasing was Italian. |
| Formal address (*lei*) | **No** | English has no grammatical courtesy distinction. The nearest lever is naming: title plus surname on the first touch, first name once the prospect has used it. |
| Ban on English loanwords | **No** | A register rule about Italian copy. It is replaced below by an English-register ban list. |
| "una call di 25 minuti" | **No** | The mechanism, an odd and specific number read as a measured request, travels. The words do not. |

---

## Register (`register`)

Dry, professional, declarative. The reader is a practitioner deciding whether to spend
twenty-five minutes, not an audience.

- Title plus surname on the first touch. First name only after the prospect has used it.
- No exclamation marks.
- No superlatives, about the product or about the recipient. Professional recognition, not
  flattery: the first line cites what the account does, never how well it does it. See
  `references/anti-patterns.md` on decorative personalisation.
- Short declaratives. Cut "I wanted to reach out", "I hope this finds you well", "in order
  to". They add length without adding a fact.

The installing company's binding writing rules are read from `writing_rules_file` before any
customer-facing text is written. That slot is a hard gate: it has no default and must exist
before the first run.

## Recovery register (`recovery_register`)

Recovery messages, sent after a no-show or a missed slot, warm up: name the likely cause,
assign no blame, offer the simpler channel. Only the temperature changes. Doctrine E5: a
no-show is a hole in the calendar, so the message removes friction instead of adding
pressure.

---

## Banned tokens (`banned_tokens`)

### 1. The em-dash

Never, in any output, in any language. Replace with a colon, commas, parentheses, or a full
stop.

This adapter cannot show the character without violating the rule it documents; the Italian
adapter carries the worked example, with the character written as a placeholder token.

### 2. English-register filler

Banned in English customer-facing copy:

- **Superlatives and marketing adjectives.** "Powerful", "seamless", "best-in-class",
  "game-changing", "unlock", "leverage".
- **"Just checking in"** and its variants. A follow-up with no new content is a chaser, and
  the chaser is already banned by the touch cap: see doctrine D2 and E3.
- **"Circle back", "touch base", "reach out"** and the rest of the sales-idiom register. They
  signal a sequence rather than a person.
- **Exclamation marks.** None, anywhere.

The test is the same one that governs decorative personalisation: if the sentence stays true
when you swap the company name out, rewrite it.

## Allowed exceptions (`allowed_exceptions`)

Declared one word at a time, before the first run, and only for words the founder already
uses in their own writing. A word is allowed because it was declared in advance, never
because it read acceptably in the draft being written.

The Italian adapter's two exceptions ("call", "test") are ordinary English nouns and need no
declaration here.

---

## The English instances of the message rules

### First line

The formula is universal (`references/policies/04-message-craft.md`). Its English instance:

```
I am writing because [ACCOUNT] [SPECIFIC VERIFIABLE FACT]: that is a context in which
[OPERATIONAL CONSEQUENCE OF THE FACT].
```

The fact must carry a `source_url`. The consequence is the only place where the agent
interprets, and it stays operational, never emotional.

### Subject line (`subject_format`)

The reference format is `<product_name> × [account]: [promise]`. Constant across the motion,
names the account and names the promise. No English instance was observed; the format is
inherited, the promise wording is the installation's to write.

### CTA (`cta_wording`)

**No English default.** The slot must be filled at install.

What transfers is the mechanism, not the words: a single request, with a duration that is odd
and specific rather than rounded, so that it reads as measured. Exactly one CTA per message;
that cap is doctrine D5, not a preference.

### Follow-up text

One follow-up, standard text, same CTA, no additional personalisation (doctrine E3, slots
`followup_count` and `followup_window_days`). A follow-up rewritten per account destroys the
only comparison the motion has, and a follow-up with nothing new in it is the "just checking
in" message banned above.

---

## Compliance checks

The active adapter populates `Message.compliance_checks.language_checks` in
`references/schemas/message.schema.json`. For English:

| Key | Status | Passes when |
|---|---|---|
| `no_em_dash` | Required | The draft contains no em-dash. |
| `no_anglicisms` | Not applicable | The check has no meaning in an English adapter. Omit the key rather than setting it to `true`. |

A workspace that adds a ban to `banned_tokens` adds the matching key here. A false value
blocks delivery of the draft. It does not produce a warning.
