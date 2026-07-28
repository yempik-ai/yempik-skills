# Policy 05: Reply Handling and Objections

## Classification (deterministic, before any action)

| Class | Recognition | Action | State change |
|---|---|---|---|
| `interest_with_slot` | the prospect proposes a date and time | confirm within the hour, then send the invite | -> `meeting_set` |
| `interest_without_slot` | interest declared without a date | propose 2-3 concrete time slots, never "whenever works for you" | stays `replied` |
| `information_request` | questions about the product | answer, then re-propose the CTA once | stays `replied` |
| `deferral` | explicit future date | record the `reactivation_date`, no touch before it | -> `nurture` |
| `refusal` | explicit no | close politely, commit to not re-contacting | -> `lost` |
| `auto_reply` | out of office, automatic acknowledgment | **no state change** | unchanged |
| `internal_routing` | points to a colleague | restart from the named contact | new stakeholder |
| `bounce` | mailer-daemon, decommissioned mailbox | dead channel, look for an alternative, flag it | -> `dead_channel` |

**Hard rule:** an auto-reply is never interest. Written rule in the commercial state file
(`commercial_state_file`), section "Maintenance rules", originating from the ACCOUNT-H case.

## Handling procedure

1. **Classify.** Apply the taxonomy, quoting literally the phrase that determines the class.
2. **Check the state.** Compare against the pipeline row; if it diverges, flag the discrepancy.
3. **Act.** `interest_with_slot` -> draft a confirmation within the hour; `interest_without_slot`
   -> draft with 2-3 concrete time slots; `deferral` -> record the reactivation date, no further
   touch; `refusal` -> draft a polite closing message and a commitment not to re-contact;
   `internal_routing` -> new stakeholder, restart by naming who routed it; `auto_reply` -> no
   state change.
5. **Record.** Update the evidence, the state and the next step, with a date.

## Response time

Prepare the confirmation within `reply_response_target` (reference default: 1 working hour) of
a reply expressing interest.

Evidence: ACCOUNT-A replies, is offered concrete time slots under an hour later, and confirms
shortly after. ACCOUNT-C replies and confirms within 20 minutes. In the two cleanest
conversions, the full cycle closes in under an hour.

## Objections: the three observed and how they were handled

### 1. Integration with the existing system (the most frequent and the hardest)

**Appeared in:** ACCOUNT-A (INCUMBENT-SOFTWARE-1, concern about the initial import), ACCOUNT-B
(INCUMBENT-SOFTWARE-3, closed systems inherited through acquisitions).

**Correct handling:** state what is ready and what is not, offer a dated re-contact.

**Forbidden:** promising integrations that have not been built. Real phrase used: "I would
rather not sell you a connection that is not ready today."

### 2. Privacy and data handling

**Appeared in:** ACCOUNT-B (personal data of the residents), ACCOUNT-U (data protection
officer questions on compliance obligations).

**Correct handling:** explain the architecture, do not reassure generically. Real content:
personal and sensitive data stays out of memory and out of training; the AI sees only
operational information (floor, street number, description of the issue).

**Forbidden:** promising legal compliance. The outbound doctrine reference explicitly rules
this out: flag the uncertainty and propose a verification.

### 3. There is already an AI solution

**Appeared in:** ACCOUNT-B (a partner already active on calls and email, pay-per-use).

**Correct handling:** concede the point, then shift the comparison to where the real
difference is: taking ownership of the workflow, not answering the phone.

**Forbidden:** attacking the existing vendor.

## When a reply changes the state of another object

If a reply contradicts a pipeline row or a file, the agent flags the conflict and proposes
the correction; it updates autonomously only when the evidence is unambiguous (doctrine D6,
D8). It never resolves a conflict between two authoritative sources silently.
