# Operating doctrine

The rules the reference motion actually ran on. Nothing here was designed in the abstract:
every rule carries the case that produced it and the failure it prevents.

---

## The universal kernel

Fourteen invariants. They hold for any company and any market. **If an installation changes
any of these, it is no longer using this system.** Everything below the kernel is either a
rule with a configurable value, a heuristic with variable outcome, or a preference that must
be re-derived per company.

1. No autonomous sending. Drafts yes, sends no.
2. A touch cap per account. The value is configurable, its existence is not.
3. Evidence first, state second.
4. No state promotion without a dated, verifiable event.
5. An auto-reply is never interest.
6. The specific fact in the first line, and no decorative personalisation.
7. A closed set of angles.
8. A single mandatory follow-up before an account may be declared dead.
9. Verify the live system before declaring a state.
10. Zero rule: warm relationships do not enter the outbound motion.
11. Conflicts between sources are flagged, never resolved in silence.
12. `unknown` is a legitimate attribution value.
13. A learning is not a rule until a human ratifies it.
14. `Message.compliance_checks` always exist. Their content changes, their existence does not.

---

## How to read a rule

Each rule carries the fields the reference motion recorded for it: description, trigger,
input, action, exceptions, stop, escalation, real example, failure mode avoided. Where a
field is absent below, the source did not record one. The fields are what make the doctrine
auditable: a rule you cannot trace back to a trigger and a real case is a slogan.

Classification:

| Class | Meaning |
|---|---|
| **[D]** | Deterministic. Non-negotiable, mechanically verifiable. |
| **[E]** | Heuristic. Guided judgement, variable outcome. |
| **[P]** | Preference. Stylistic, changes per company. |
| **[H]** | Unvalidated hypothesis. Not yet demonstrated. |

---

# Deterministic rules

## D1 [D] No autonomous sending

- **Description:** the agent never sends email, never accepts invitations, never publishes.
  It produces drafts only.
- **Trigger:** any action with an external effect.
- **Input:** none.
- **Action:** create the draft, report it in the brief, stop.
- **Exceptions:** none.
- **Stop:** if a tool would expose a `send`, do not call it.
- **Escalation:** report to the founder with the action ready to execute.
- **Real example:** all 26 emails in the observed period were sent by hand by the founder.
- **Failure mode avoided:** a wrong email sent to a real customer is irreversible.

Configuration: `send_authority` (reference default: `human_only`).

## D2 [D] A cap of 2 email touches per account

- **Description:** first touch plus a single follow-up. After that the email channel is closed.
- **Trigger:** an account with 2 sends and no reply.
- **Input:** the send log in the contact queue file (`contact_queue_file`), verified against
  the email connector.
- **Action:** mark the channel as exhausted, propose a phone call or closure, send nothing else.
- **Exceptions:** dated reactivations explicitly requested by the prospect.
- **Stop:** the cap is reached.
- **Escalation:** the choice of the next channel belongs to the founder.
- **Real example:** ACCOUNT-E, two nudges, then stop, with a written note that the phone
  channel is the founder's decision.
- **Failure mode avoided:** insisting turns a silence into a no and burns the domain.

Configuration: `touch_cap_per_account` (reference default: 2) and `escalation_owner`
(reference default: the founder).

## D3 [D] At most 3 first touches prepared per day

- **Trigger:** the daily sourcing run.
- **Action:** prepare 2-3 drafts, in queue order, then stop.
- **Exceptions:** none observed.
- **Real example:** batch 4 was worked at 3 per day from day 13 to day 15.
- **Failure mode avoided:** volume without personalisation, which is the default failure of
  automated outbound.

Configuration: `max_first_touches_per_day` (reference default: 3).

## D4 [D] Zero rule: never outbound on a warm relationship

- **Description:** contacts the founder sees in person, first-degree connections, active
  customers: no outbound, no paid enrichment.
- **Trigger:** a candidate appears in the pipeline as a direct or warm relationship.
- **Action:** remove it from the queue, flag it, do not touch it.
- **Escalation:** the founder decides how and when to talk to them.
- **Real example:** on day 1, enrichment ran on contacts from <COMMUNITY> and was corrected by
  the founder. The rule was born there. On day 18, ACCOUNT-F was flagged and never entered
  the queue.
- **Failure mode avoided:** treating a relationship as a lead damages the relationship.

Configuration: `warm_relationship_map`, which **must be populated before the first run**, not
after.

## D5 [D] Writing constraints

Two of this rule's constraints are language-independent and stay here. The rest of the rule
is register, and register is configured per language.

- **Description (universal part):** one CTA per email, and a tracked product link, carrying
  the account as its per-account tracking value, at the first mention of the product.
- **Trigger:** every text destined for an external reader.
- **Action:** mechanical check before the draft is delivered.
- **Failure mode avoided:** text that reads as machine-written contradicts, on its own, any
  claim the message makes about reliability.

Configuration: `cta_count_per_message` (reference default: 1) and `tracked_link_policy`.

> **Delegated:** the em-dash ban, the ban on English loanwords toward the customer, and the
> explicitly declared allowed exceptions are register rules, not universal doctrine. They
> live in `references/languages/it.md` for the reference market, with the English-register
> equivalent in `references/languages/en.md`. The real example that produced the rule (a set
> of drafts redone on day 1, the rule extended to every company output on day 2) travels with
> them, because it is specific to the banned character. Configuration: `banned_tokens` and
> `allowed_exceptions`.

## D6 [D] Evidence first, state second

- **Description:** update the evidence first (what happened, with source and date), then the
  state, then the CRM. Never the reverse.
- **Trigger:** any change of commercial state.
- **Action:** cite the thread or the file as the source, on the state line itself.
- **Real example:** every row of the commercial state file (`commercial_state_file`) carries a
  "current evidence" column with the date and time of the message.
- **Failure mode avoided:** a pipeline that describes hopes instead of facts.

## D7 [D] Do not promote a state without the corresponding event

- **Description:** "interested" is not a partner, a call is not a pilot, a free setup is not
  invoiced, a positive reply is not a meeting.
- **Trigger:** the temptation to advance a pipeline row.
- **Action:** advance only on the verifiable event: date, time, explicit confirmation.
- **Real example:** ACCOUNT-A stayed at "pilot agreed (verbal)" and not "won", because there
  was no invoice. ACCOUNT-E stayed at "reply" and not "call set", because no slot was ever
  confirmed.
- **Failure mode avoided:** an inflated forecast, and decisions taken on a fictional pipeline.

Configuration: `opportunity_stage_ladder` (reference default: `call_held` -> `pilot_verbal`
-> `pilot_signed` -> `invoiced`, no skipping).

## D8 [D] Always verify the live system before declaring a state

- **Description:** files are a dated snapshot, not the current state. The email connector and
  the CRM are the truth.
- **Trigger:** every run.
- **Real example:** on day 18 the files listed 5 follow-up drafts as ready. The email
  connector showed they had **already been sent** on day 15. Without the check, duplicate
  drafts would have been created.
- **Failure mode avoided:** acting on a stale state.

Configuration: `evidence_of_record` (reference default: the email connector).

---

# Heuristics

## E1 [E] One specific, verifiable fact in the first line

- **Description:** the first sentence cites an observable, specific fact about the account and
  states its operational consequence. Never a compliment.
- **Input:** at least one fact from the site (managed-unit count, offices, incumbent system,
  published method).
- **Action:** "I am writing because [account] [specific fact]: that is a context in which
  [consequence]".
- **Exceptions:** if no specific fact exists, the account is not contactable. It goes back to
  research or is discarded.
- **Real example:** ACCOUNT-C, "~90 managed units across three offices in <CITY-1>", replied
  in 38 minutes.
- **Failure mode avoided:** decorative personalisation ("I saw your website, congratulations"),
  which is indistinguishable from spam.

## E2 [E] A closed angle, chosen from the evidence

- **Description:** the angle is not invented per account. It is chosen from a closed set,
  based on the observed signal.
- **Exceptions:** where two signals coexist, the one more specific to the account wins.
- **Real example:** 4 angles across 26 accounts, none invented ad hoc.
- **Failure mode avoided:** a different message per account makes it impossible to learn what
  works.

The universal part is that **a closed angle set exists** and that the choice is deterministic
given the signal. The set itself is not universal.

> **Delegated:** the observed signal-to-angle mapping (multiple offices, a named incumbent
> system, high volume or a resident portal, a published operational method) is market
> configuration. It ships as a worked example in `references/markets/_template.md` and must be
> re-derived per market. Configuration: `angle_set`, `signal_types` and `signal_to_angle_map`.

## E3 [E] The single follow-up is the multiplier, not extra personalisation

- **Description:** one follow-up only, 4-5 days later, standard text, same CTA.
- **Real example:** three of the four conversions arrived on the second touch. ACCOUNT-A is
  the exception.
- **Failure mode avoided:** declaring an account dead after a single silence.

Configuration: `followup_count` (reference default: 1) and `followup_window_days` (reference
default: 4-5, `[INFERENCE]`: the median of the observed intervals, never a written rule).

## E4 [E] A prospect who replies with an operational question is accommodated, not redirected

- **Description:** if the prospect proposes the date and time themselves, accept or confirm
  immediately, without redirecting them to your own calendar.
- **Real example:** ACCOUNT-D proposed a weekday-morning slot and ACCOUNT-C proposed a
  late-afternoon slot on day 19. Both were confirmed within 20 minutes, with no
  counter-proposals.
- **Failure mode avoided:** adding friction at the moment of maximum availability.

## E5 [E] A no-show is not a refusal

- **Description:** a missed connection is treated as a hole in the calendar, not as
  disinterest. Reduce the friction instead of increasing the pressure.
- **Action:** attribute no blame, offer a simpler channel (phone instead of video), propose
  concrete slots.
- **Real example:** ACCOUNT-D, reply sent: "I imagine it was a hectic day, honestly no problem
  at all. I will call you on your mobile, so you do not have to connect to anything."
- **Failure mode avoided:** closing an interested account over a logistical problem.

Configuration: `recovery_register`, which is where the warmer recovery tone is declared.

## E6 [E] Discovery may conclude "not now"

- **Description:** a well-run call can end in a reasoned disqualification. A fast no is worth
  more than a long maybe.
- **Trigger:** the barrier that emerged requires changing the product roadmap **for the whole
  account**, not just for the first test.
- **Real example:** none clean yet. The case previously cited here (ACCOUNT-B) turned out to
  be a misapplication of the rule: see E8.
- **Failure mode avoided:** chasing the largest logo and bending the roadmap around a single
  case.
- **Opposite failure mode, equally expensive:** see E8.

## E7 [E] Admit what the product does not do

- **Description:** when an objection touches a capability that is not ready, state that it is
  not ready and offer a dated re-contact.
- **Real example:** the post-call recap to ACCOUNT-B: "I would rather not sell you an
  integration that is not ready today."
- **Failure mode avoided:** promising integrations that do not exist, which is the fastest way
  to lose a pilot during onboarding.

## E8 [E] Separate the pilot barrier from the contract barrier

> This rule was born from a real error on day 19, corrected by the founder.

- **Description:** when a technical objection surfaces, always ask whether it blocks **the
  first test on a single unit** or **adoption at full scale**. They are two different things
  and they resolve on different timescales.
- **Trigger:** an objection about integration, migration, compatibility or volume.
- **Required inputs:** the scope of the first purchase, as declared in the product thesis.
- **Action:** check whether the same thing has already been done by hand for another account.
  If it has, it is not a product barrier: it is service work, and it should be proposed as
  such.
- **Real example:** ACCOUNT-B raised the impossibility of connecting closed incumbent systems.
  True at full scale. But the pilot only required moving the data of a single building,
  something that was already being done by hand for another account in the same week. The
  disqualification was wrong.
- **Exceptions:** if the manual work is not repeatable even once, the barrier is real.
- **Stop condition:** if running the first test would require building a new capability, then
  it genuinely is a product barrier.
- **Failure mode avoided:** disqualifying the largest account in the pipeline by applying to
  the pilot a barrier that only concerns scale. This is the reverse of E6, and it costs more,
  because it is invisible: a reasoned no looks like discipline.

Configuration: `first_purchase_scope` (reference default: one real unit, one workflow, running
in parallel with the existing system) and `product_thesis_file`.

---

# Preferences

Preferences are not rules. They are the reference motion's stylistic choices, and **none of
them was A/B tested**. They exist here only as named slots that an installation must fill;
the values themselves live in `references/configuration.md` and, for the reference market,
in `references/languages/it.md`.

| Ref | What must be decided | Slot |
|---|---|---|
| **P1 [P]** | The register of the first touch, and the warmer register used in recovery messages. | `register` · `recovery_register` |
| **P2 [P]** | The exact CTA wording, including the meeting length. | `cta_wording` |
| **P3 [P]** | The subject-line format, which names the account and the promise. | `subject_format` |

An installation that leaves these unfilled inherits another company's voice. An installation
that treats the reference defaults as findings has configured nothing.

---

# Unvalidated hypotheses

The reference motion carried four hypotheses that read like rules but were never
demonstrated: the 0-12 score predicts conversion; a named mailbox converts better than a
department mailbox; a tracked-link click without a reply is a warm signal; the "published
method" signal is the strongest.

> **Delegated:** all four live in `references/open-hypotheses.md`, each with the
> counter-evidence attached (a 9/12 account converted while 10/12 accounts did not reply; a
> department mailbox converted in 38 minutes while a named mailbox never replied; the web
> analytics connector was never consulted; the "published method" weight rests on a single
> case). A hypothesis separated from its counter-evidence becomes a rule by accident, which
> is exactly what this split is meant to prevent.

Configuration: `min_sample_size_for_rule` (reference default: 30). Below it, a learning
candidate cannot become a rule, and a single case never becomes a rule.
