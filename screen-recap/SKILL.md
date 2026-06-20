---
name: screen-recap
description: >-
  Record a TARGETED demo or end-to-end test of the result and deliver it as a VIDEO + short recap,
  instead of a wall of text. Records the REAL SCREEN with screencapture — never slides or title cards.
  Captures ONLY the final demonstration (~20-90s), not the whole session. ONLY for Claude Code (local
  CLI on macOS); it does not work in sandbox environments like Cowork. Use this skill when the user wants
  to SEE that something works instead of reading about it — "show me what you did", "run a test and
  record it", "show me the demo/the flow", "record the verification", "video recap", "record the e2e
  test" — and as the last verification step before declaring done (e.g. after building a landing page,
  record the E2E test of the form/CTA on localhost). Do NOT use it for text-only/code-only tasks with no
  visible result, unless explicitly requested. Requires the macOS Screen Recording permission.
---

# Screen Recap — record the demo/test, deliver a short recap + video

## What it does and why
At the end of the work it records **only a targeted demo or end-to-end test** of the result and delivers it as a **video + short recap**, instead of a wall of text. It does not record the whole session: only the final demonstration that proves the thing works.

## Where it runs
**Claude Code only** (local CLI on macOS): the shell runs on the Mac, so it can use `screencapture` to actually record the screen. In sandbox environments (e.g. Cowork) it does not work — don't use this skill there.

## Golden rule — the real screen
The clip shows the **real screen** recorded during the demo. Never slides, title cards, or graphical reconstructions. If you can't record the screen (e.g. the permission is missing), **say so and stop** — don't invent a substitute.

## Key idea — no "recording the past"
You don't record work already done: you record a demonstration performed right now.
```
development (NOT recorded) → rec_start → demo / E2E test → rec_stop → recap + video
```

## When it triggers
1. **On request:** "show me what you did", "run a test and record it", "show me the flow".
2. **As the last verification step** before declaring "done".

Don't record if there's no **visible** result to show (text-only/code-only tasks), unless explicitly requested.

## How to use it
1. **Start:** `bash scripts/rec_start.sh [output_folder]` (default `./recordings`).
2. **Run ONLY the demo/test.** For a web app: start the dev server and walk through the flow in the browser — e.g. `npm run dev` → open `http://localhost:3000` → scroll, click the CTA, submit the form, success state.
3. **Stop:** `bash scripts/rec_stop.sh` → finalizes the `.mov` (and creates a `.mp4` if ffmpeg is present), prints the path.
4. **Recap:** 3–6 lines + the **absolute path** of the video.

## macOS permission — one-time
*System Settings → Privacy & Security → Screen Recording* → enable the app that launches Claude Code (Terminal / iTerm / VS Code) and restart it. Without it, the video comes out **black**: that's issue #1, not a bug in the skill.

## Automatic mode (optional)
To record every task hands-free, install the hooks in `hooks/` (see `README.md`): `UserPromptSubmit`→start, `Stop`→stop. **Not recommended** for long tasks (huge videos): the default is to record only the demo.

## Recap format — always short
```
Done: <1 line>
How: <2–3 bullets>
Outcome/Verification: <1 line: what the video shows>
Video: <absolute path>
```

## Skill files
- `scripts/rec_start.sh`, `scripts/rec_stop.sh` — start/stop macOS recording.
- `hooks/` — optional automatic mode (`on_prompt_submit.sh`, `on_stop.sh`, `settings.example.json`).
