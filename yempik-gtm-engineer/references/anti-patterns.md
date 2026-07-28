# Anti-patterns

Some of these are real errors that were made and corrected. Others are anti-patterns
already documented elsewhere in this skill. Items 2 and 3 are Italian-register specific;
see the note under each.

## 1. Decorative personalisation

> ❌ "I saw your website and was struck by how professionally you manage your
> buildings."

This holds for any recipient, so it holds for none. **Test:** if the sentence stays
true after swapping the company name, rewrite it.

## 2. Em-dash (Italian-register specific)

> ❌ "<PRODUCT> takes ownership of the work [EM-DASH] from the report to the close
> [EM-DASH] without switching your incumbent system."
>
> *(the character is written as a placeholder: this file cannot contain it without
> violating the rule it documents.)*

A real error made on day 1: a whole draft set redone. The rule was extended to every
company output on day 2, after an em-dash was found in a price quote. Fixed: colons,
commas, parentheses, a middot.

This example is Italian-market copy. The em-dash ban itself is universal (see
`doctrine.md` D5), but the full register rule and its allowed exceptions live in
`references/languages/it.md`; the English-register equivalent is in
`references/languages/en.md`.

## 3. English loanwords toward the customer (Italian-register specific)

> ❌ "<PRODUCT> automatizza il workflow e sostituisce i tool legacy del vostro stack."

Banned toward the customer: "workflow", "tool", "legacy" and similar loanwords (founder
rule, day 7). Approved Italian replacements: "flusso di lavoro", "strumento",
"gestionale attuale". Allowed exceptions: "call", "test".

This is a register rule, not a universal one: it governs Italian customer-facing copy
specifically. See `references/languages/it.md` for the full banned-token list and
declared exceptions, and `references/languages/en.md` for the English-register
equivalent (no superlatives, no "just checking in", no "circle back", no exclamation
marks).

## 4. Two CTAs

> ❌ "Would a 25-minute call work for you? Alternatively I would be happy to send a
> recorded demo, or you can reply with two dates that work for you."

Three exits instead of one: the decision becomes costly and the reply rate drops.

## 5. Unapproved claim

> ❌ "<PRODUCT> integrates with INCUMBENT-SOFTWARE-3 and automatically migrates data
> from closed incumbent systems."

False at the time of writing. It is exactly the ACCOUNT-B objection. A claim like this
survives until onboarding and then blows up the pilot.

## 6. Auto-reply read as interest

> ❌ Pipeline line: "ACCOUNT-H: reply received, interest to nurture."

The auto-reply only said "message assigned to the relevant department." The rule was
born here: never turn an auto-reply into interest.

## 7. Third touch

> ❌ "I am following up once more on this, in case it slipped by you..."

Forbidden by the 2-touch cap. ACCOUNT-E case: after the second nudge the channel is
closed, and the choice of the phone channel belongs to the founder.

## 8. Guessed email address

> ❌ The email is not published; `firstname.lastname@domain.example` is tried by
> analogy.

Forbidden: "if you cannot find it, flag it in the brief instead of inventing or
guessing the address." A wrong address produces a bounce that damages the domain's
reputation.

## 9. Outbound on a warm relationship

> ❌ Preparing a sequence for a contact the founder sees every week.

A real error on day 1, on contacts from <COMMUNITY>. It produced the zero rule.

## 10. Duplicate draft

> ❌ Creating a follow-up for an account the founder has already replied to by hand.

A real risk on day 18: the files indicated 5 drafts ready, the email connector showed
they had already been sent. Avoided only by the live-system check.
