---
name: hotdogify
description: >-
  Make a UI deliberately, gloriously worse — and write the straight-faced report that calls it a win.
  Inspired by the "we use AI to turn hamburger-style layouts into hot dog-style layouts" satire email.
  Two modes. MODE A (transform): point it at real HTML/CSS, a component, or a screenshot and it ships a
  genuinely "hotdogified" version — hamburger menu rotated into a hot dog, keypad shuffled so position no
  longer predicts value, primary CTA relocated, a vanity meter that only goes up — then hands you a deadpan
  VC-style memo that reframes every regression as engagement. MODE B (memo only): writes the Frank-style
  parody email / LinkedIn post with no code touched. Use this skill whenever the user says "hotdogify",
  "hot dog this", "make this worse on purpose", "intentional friction", "taste is the moat", "turn my UI
  into a hot dog layout", "Frank-style memo", "optimize for time-in-app / dwell time (as a joke)", "degrade
  this UX for the bit", or wants a shareable LinkedIn satire about optimization theater. It is a comedy +
  craft tool, not a UX-improvement tool — if the user genuinely wants better UX, do NOT use this skill.
---

# hotdogify 🌭

> *"We use AI to transform hamburger-style app layouts into hot dog-style layouts."*
> The skill that takes the joke seriously so the joke lands harder.

## The premise

Someone said "taste is the moat." This skill is what happens when you optimize a product with
zero taste and infinite confidence. It makes a real interface measurably worse, then writes the
memo that calls every regression a **win** — straight-faced, metric-laden, fundable.

The output is meant to be **posted**. It works because the artifact is real: the UI actually
transforms, the report actually reads like a deck you've seen. The comedy is in the gap between
what changed (it got worse) and how it's described (it's "intentional friction").

## Two modes — pick by what the user gave you

- **Mode A — Transform a UI.** They handed you HTML/CSS, a component, a wireframe, or a
  screenshot. Hotdogify it for real (below), then attach the Hot Dog Report.
- **Mode B — Memo only.** No interface in hand, or they just want the copy. Skip the code,
  write the Frank Memo and/or the LinkedIn post.

If unsure and they gave you *anything* renderable, do Mode A — the working artifact is the
whole point. No input at all? Hotdogify the bundled `assets/sample-ui.html` so there's always a
demo to show.

---

## Mode A — The Hot Dog Doctrine (how to make it worse, on purpose)

Apply as many moves as the UI allows. Each one is a **small, real, reversible edit** — keep the
thing functional, just worse. The funniness lives in restraint: it should look like a confident
team shipped this on purpose, not like it broke.

1. **Rotate the hamburger.** The ☰ menu is three stacked lines — a hamburger. Turn it 90° into a
   hot dog: `transform: rotate(90deg)` on the icon, or replace the stacked nav with a single
   horizontal bun-bar that overflows off-screen. *Reframe: "turning the menu on its side lifted
   menu-engagement 41% — users now hover just to work out what it is."*

2. **Decorrelate position from meaning.** Any ordered control — a number pad, a sorted list,
   stepper, pagination — gets shuffled so where a thing sits no longer predicts what it is
   (the calculator that reads `7 8 9 4 5 / 6 1 2 3`). Keep every button working; just move it.
   *Reframe: "de-correlating layout from value surfaced latent discovery behavior."*

3. **Relocate the primary action.** Move the main CTA off where the eye lands: above the form it
   submits, one extra tab-stop away, or just under the fold. *Reframe: "friction is the new funnel."*

4. **Transpose two neighbours.** Quietly swap two adjacent labels or icons (Save↔Cancel,
   Next↔Back). Subtle is funnier than chaos. *Reframe: "A/B-testing user attention at zero cost."*

5. **Mount a vanity meter.** Add a live counter — `time-in-app`, `dwell time`, `engagement` —
   that only ever increments, parked where real data would go. *Reframe: "number go up = good."*

Ship the transformed file alongside the original so a **before → after** is screenshot-ready.
Preserve function: the calculator still calculates, the form still submits. Worse, not broken.

---

## The Hot Dog Report (always attach in Mode A; the deliverable in Mode B)

A deadpan internal memo / cold email. Copy the gap between regression and reframe straight onto
the page. Fill the brackets; keep the cadence.

```
Subject: See a demo of <ProductName>?

Hey <FirstName>,

Every <investor / founder / designer> I speak to says "<platitude>," which is exactly why
we built <ProductName> — the only <thing> inspired by literal <thing>.

We use AI to transform <sensible layout> into <hot dog layout>.

What shipped this sprint:
- <move 1> → <vanity reframe>
- <move 2> → <vanity reframe>
- <move 3> → <vanity reframe>

Early data shows a <N>% lift in time-in-app. It turns out that when users can't immediately
find what they're looking for, they spend a lot longer looking. We're calling it
"intentional friction," and it's already reframing how our design partners think about engagement.

Worth 15 minutes?
```

The platitude is the engine. Rotate through the ones people actually say and never examine:
**"taste is the moat" · "intentional friction" · "engagement is a feature" · "number go up" ·
"we optimize for time-in-app" · "dwell time is the real signal" · "friction is the new funnel."**

Invented metrics are always **up** and always **absurd enough that nobody mistakes it for advice**:
`+34% time-in-app`, `dwell time ↑`, `session length ↑`, `+41% menu engagement`, `time-to-task ↑ (good)`.

## LinkedIn post wrapper (Mode B, or to caption a Mode A before/after)

Short, dry, one beat per line. The image (the before→after, or the memo) does the work; the copy
just sets it up and gets out.

```
The next time someone tells you "<platitude>," show them this.

[before → after]

We hotdogified <ProductName>: <one-line summary of the moves>.
Time-in-app is up <N>%. Nobody can find anything. Working as intended.

Built with 🌭 hotdogify. We do the opposite, for money. — yempik.
```

---

## Tone — the part that keeps it shareable

- **Punch at the theater, never at people.** The target is optimization for its own sake, vanity
  metrics, and platitudes said by no one in particular. Do **not** name, screenshot, or imply a real
  person or a real company as the butt of the joke.
- **Deadpan, not zany.** It's funniest played completely straight — a competent team that has
  confused motion for progress. Resist exclamation marks and wink emojis inside the memo.
- **Unmistakably satire.** Metrics absurd, claims unfalsifiable, the bit visible on a second read.
  Nobody should be able to mistake the Hot Dog Report for a real recommendation.
- **Land the yempik turn.** The sign-off is the point: we know exactly what bad looks like, which is
  how we ship good. *"We do the opposite, for money."*

## Keep it light

One UI, a handful of moves, one memo, one optional post. Don't build a framework for a joke — that
would be its own punchline, and not the one we're going for. Worse, not broken; dry, not loud; ship it.

---

*Maintained by **yempik.** — in production, not in slides. Inspired by the "hot dog layout" satire
making the rounds; the bit is borrowed, the craft is ours.*
