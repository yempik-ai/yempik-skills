# screen-recap (Claude Code)

A skill that, at the end of the work, records **only a demo / end-to-end test of the result** and returns a **short recap + the video**, instead of a wall of text.

**Claude Code only** (local CLI on macOS): the shell runs on the Mac, so `screencapture` actually records the screen. In sandbox environments (Cowork) it doesn't work — the Cowork version was removed on purpose.

## Idea
You don't record work already done: you record a **demonstration performed right now**, focused, ~20–90 seconds.
```
development (NOT recorded) → rec_start → demo/E2E test → rec_stop → recap + video
```

## Structure
```
screen-recap/
├── SKILL.md                  # instructions for Claude (it reads them itself)
├── README.md                 # this file
├── scripts/
│   ├── rec_start.sh          # starts the recording (screencapture in background)
│   └── rec_stop.sh           # stops and finalizes the .mov/.mp4
└── hooks/                    # OPTIONAL: automatic full-session
    ├── on_prompt_submit.sh
    ├── on_stop.sh
    └── settings.example.json
```

## macOS prerequisite — one-time
*System Settings → Privacy & Security → Screen Recording* → enable **Terminal** (or iTerm / VS Code) and restart the app.
Without it, `screencapture` produces a **black** video: that's issue #1, not a bug.

## Usage (default = the demo only)
1. `bash scripts/rec_start.sh` — start (output in `./recordings`).
2. Run **only** the demo/test. For a website: `npm run dev` → walk through the flow on `http://localhost:3000`.
3. `bash scripts/rec_stop.sh` — stop, prints the video path.
4. A 3–6 line recap + the path.

## Advanced alternative — automatic full-session (not recommended)
To record the whole task automatically, wire up the hooks:
1. In `hooks/settings.example.json` replace `/ABSOLUTE/PATH/screen-recap` with the real path.
2. Paste the `hooks` block into `~/.claude/settings.json` or `<project>/.claude/settings.json`.
3. `UserPromptSubmit` starts, `Stop` stops.

Not recommended because long tasks produce huge, unreadable videos. The default mode (the demo only) is almost always the right one.

## Known limits
- No Cowork (Linux sandbox, no `screencapture`).
- MDM-managed Mac: the Screen Recording permission must be unlocked by IT.
- Code-only tasks with no visible output: nothing to show → by default it skips the video.
- Stop via `SIGINT`: that's the correct way to make `screencapture` finalize the file. Worth confirming on your Mac on the first real run.
