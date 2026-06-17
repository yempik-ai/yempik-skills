---
name: verification
description: Verify that code actually works before claiming it's done. Use this skill whenever you have written, edited, fixed, or refactored code and are about to report success — especially when you're tempted to say "this should work," "that should fix it," or "done" without having run anything. Triggers on any task whose success is checkable: shipping a feature, fixing a bug, wiring an endpoint, changing a query, touching a UI flow, running a migration, or a performance fix. It does not teach you to write code. It makes you prove the code does what you claimed — with tests, a real browser, the database, the logs, and timing.
---

# Verification

## The one rule

**"Done" means "verified working," not "code written."**

Code you haven't run — yours or an AI's — is a hypothesis, not a result. Treat it as guilty until proven innocent and go get the evidence. Running the thing takes minutes; shipping something broken costs trust and a round-trip. Verifying first is almost always cheaper.

## Two banned phrases

- "This should work."
- "That should fix it."

"Should" means you're guessing. Replace the guess with an observation: run it, then say what happened. If you genuinely can't run it (no environment, no credentials, no display), say exactly that — "I couldn't verify X because Y" — instead of dressing a guess up as a conclusion.

## The verification ladder

Climb as high as the stakes warrant. A typo fix needs rungs 1–2; a user-facing feature that touches data deserves the whole ladder. Always be able to say which rungs you climbed and why you stopped.

1. **Static** — does it parse / compile / typecheck / lint? Run the build. The cheapest check; rules out a class of dumb mistakes for free.
2. **Unit** — do the relevant tests pass? Run the suite. New logic with no test covering it is a gap worth naming (and often worth a quick test).
3. **Integration** — do the pieces work *together*? Passing in isolation doesn't mean it's wired into the route, the route into the handler, the handler into the response.
4. **End-to-end** — does the real user flow work? Open the browser or run the CLI and actually do what a user would. Don't trust that the button calls the function — press the button.
5. **State (database)** — did the data really change? Query the DB. "Saved" means the row is there, with the right values, the right foreign keys, no duplicate.
6. **Logs** — is a green response hiding a swallowed error? Read the logs; confirm the happy path and zero errors or warnings you caused.
7. **Performance** — fast enough, and no regression? Time it, count the queries (watch for N+1), check bundle size if relevant. "Works" and "works in 8 seconds" are different outcomes.

## Evidence over assertion

Every claim about behavior is backed by something you observed this session. Do the thing, then show the proof:

- "Tests pass" → the runner summary (`12 passed, 0 failed`).
- "The endpoint returns the user" → the actual response body.
- "It saves to the DB" → the row from the query you ran.
- "No errors" → what you read in the logs.
- "It's fast" → the number (`~120ms`, `3 queries`).

If you didn't observe it, don't claim it.

## Bug fixes: reproduce, then fix, then check the neighbors

1. **Reproduce the failure** before touching anything — run the failing case and watch it fail. If you can't reproduce it, you don't understand it yet; say so and dig in rather than patching blind.
2. **Confirm the fix removes the failure** — rerun the exact same case and watch it pass.
3. **Confirm you didn't break the neighbors** — run the surrounding tests / adjacent flows.

A fix you never saw fail and then pass is not a verified fix.

## When unsure, look it up

Don't verify against your assumptions — they're on trial too. For anything version-sensitive (library APIs, tool flags, framework conventions), check the official docs. A two-minute lookup beats a confident wrong answer. Prefer primary sources.

## Report honestly

End with a plain status:

```
Verified:
- Build + typecheck: clean
- Tests: 14 passed, 0 failed
- Browser: signup → confirmation, account created
- DB: `users` row present with correct email
- Logs: no errors
Not verified:
- Email actually delivering (no mail server in this env) — needs a staging check
```

The "Not verified" section is the most trustworthy line in the report: it tells the reader exactly where the risk still is. Never leave it implicitly empty — if you didn't check something relevant, name it.

## Match depth to stakes

This isn't a license to verify forever. A copy change on a static page doesn't need a database query. The job is to close the gap between "I wrote it" and "I know it works" — not to gold-plate. Climb as far as the task earns, then stop and say where you stopped.

---

*Maintained by Yempik. Concept inspired by Anthropic's "verification" skill, reworded and kept self-contained.*
