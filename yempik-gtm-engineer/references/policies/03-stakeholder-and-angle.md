# Policy 03 · Stakeholder and Angle Selection

## Stakeholder: preference order

```
1. named contact with a relevant operational role
2. relevant department mailbox (operations@, units@, office@)
3. generic mailbox (info@)
4. certified mail             -> only if the above are dead
5. web form                   -> not contactable, discard
```

This is `stakeholder_preference_order` (`references/configuration.md` §5).

**Do not overinterpret the preference order.** Real evidence contradicts it in part:
ACCOUNT-C converted from `operations@` in 38 minutes, while the named mailbox
`firstname@account-m.example` did not reply. A monitored mailbox beat an absent named
contact.

## Routing rules

- Auto-reply naming a colleague: restart from that name, citing it explicitly. Real case,
  ACCOUNT-B: "writing to you on the operations lead's referral." Turns a cold contact into
  a semi-warm one at zero cost.
- Generic auto-reply ("assigned to the relevant department"): not interest, does not
  change state.
- Decommissioned mailbox: dead channel, flag it, do not push further.

## Authority: default unknown

`decision_role` starts at `unknown` and is updated only with evidence. The ACCOUNT-B
lesson: the finance analyst replied and took the call, but is neither the operational
owner nor the sponsor. Replying does not mean deciding.

## Angle: deterministic mapping

The angle is chosen from a **closed** set of four, based on the observed signal. Angles
are not invented per account.

**Reference example (this market).** The mapping below is the reference motion's
instance of `angle_set` and `signal_to_angle_map` (`references/configuration.md` §5).
Re-derive the signal-to-angle mapping per market in `references/markets/_template.md`;
do not reuse this table as-is.

```
if signal.type == published_method           -> angle = published_method
elif signal.type == named_incumbent_system    -> angle = replace_ecosystem
elif signal.type == multiple_offices          -> angle = continuity_across_offices
elif signal.type in (declared_volume,
                     customer_portal)         -> angle = workflow_ownership
else                                          -> no angle, return to research
```

If more than one signal is present, the most account-specific one wins: a published
method beats a named incumbent system, which beats the number of offices, which beats
volume.

## Why a closed set

With four angles over 26 accounts, it is still possible to learn which one works. With 26
different angles nothing is learned: every email becomes a single-case experiment.
