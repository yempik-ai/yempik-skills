# Policy 01: Account selection

## Admissibility formula (deterministic)

An account enters the queue **only if** all five are true:

```
admissible =
      icp_class in (IN_ICP, BORDERLINE)
  AND is_warm_relationship == false
  AND exclusion_reason == null
  AND signal != null                    # a specific citable fact exists
  AND email_status != not_found
```

If `signal == null`: the account returns to `research`, it does not enter the queue. If after
research the fact does not exist, the account is discarded. **An account without a specific
fact is not contactable.**

If `email_status == not_found`: flag it in the brief. **Never construct an
address by analogy** (an explicit rule recorded in the contact queue file, `contact_queue_file`).

## Queue order

```
order = sort by (score DESC, batch ASC, position_in_batch ASC)
```

Batches are worked through in order: batch N+1 is not touched until batch N has no ready rows
left. Real rule: "Batch 4 is worked on ONLY after batch 3's READY rows are exhausted."

## Permanent exclusions

| Category | Treatment | Example |
|---|---|---|
| Warm relationship | Out of the outbound motion, the founder decides | contacts from <COMMUNITY>, first-degree LinkedIn connections |
| Special case | Dedicated section, never the automatic queue | ACCOUNT-R (delegation chair), ACCOUNT-S (department mailboxes only) |
| Explicit refusal | Closed, never re-contact on this topic | ACCOUNT-J, "thank you, but we are not interested" |
| Dead channel | Marked, deprioritised | ACCOUNT-O, mailbox decommissioned about 12 months before day 1 |
| Dated deferral | Scheduled reactivation on the date | ACCOUNT-I, day 54 |

## Reactivations

```
if reactivation_date <= today and exclusion_reason == null:
    account re-enters the queue with the angle "resume from the deferral"
```

Observed tone rule: "resume from the deferral, do not restart from the first touch" (e.g. "as
agreed previously"). Do not repeat the first touch.
