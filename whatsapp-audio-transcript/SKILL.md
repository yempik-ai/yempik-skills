---
name: whatsapp-audio-transcript
description: >-
  Transcribe WhatsApp voice notes (.opus/.ogg files, filenames like
  "WhatsApp Audio 2026-07-22 at 16.09.25.opus" or "PTT-20260722-WA0003.opus")
  into clean, readable text, fast — entirely on-device with Whisper. Use
  whenever the user uploads or points to a WhatsApp voice message and wants
  it transcribed, read, or turned into text — "trascrivi questo vocale",
  "cosa dice questo audio whatsapp", "trascrivimi il vocale", "sbobina
  questo audio", or just drops a WhatsApp audio file expecting its content
  back as text. Handles a burst of consecutive voice notes (someone
  splitting one thought across 2-4 short clips) as a single continuous
  message. Replies directly in chat with the transcript — no heavy document
  — unless the user asks to save or export it. For long recordings,
  meetings, podcasts, lectures, or interviews use audio-video-transcript
  instead: that skill produces a structured recap + timestamped document,
  which is overkill for a short personal voice note.
---

# WhatsApp Voice Note Transcript

Turn a WhatsApp voice note — or a short burst of them — into clean,
readable text, fast. No recap document, no timestamps in the output: just
what was said, ready to read or paste. Runs entirely on-device with
Whisper; audio never leaves the machine.

## When this applies

- Filenames like `WhatsApp Audio 2026-07-22 at 16.09.25.opus`,
  `PTT-20260722-WA0003.opus`, or short `.opus`/`.ogg` files exported from a
  WhatsApp chat (chat export ZIPs use the same naming).
- The user drops one file, or several consecutive ones — a "voice note
  burst," where someone records their thought across 2-4 short clips
  instead of one long one.
- Typical length: a few seconds to a couple of minutes. If the file is long
  (10+ minutes) or is clearly a meeting/podcast/interview rather than a
  personal voice note, prefer the `audio-video-transcript` skill instead —
  it's built for that (structured recap + timestamped transcript document).

## Workflow

### 1. Locate the input file(s)

Check the uploads directory and the conversation for the audio file(s) the
user is pointing at. If several files look like a burst from the same
sender around the same time (consecutive timestamps in the filename, or
the user says "questi vocali" / "these voice notes"), treat them as one
message split across multiple recordings — order them by filename/
timestamp, not upload order.

### 2. Transcribe

```bash
python scripts/transcribe.py "<file1>" ["<file2>" ...] --out "<tmp-dir>"
```

- Leave `--model` unset (default `medium`) for the best accuracy-to-speed
  tradeoff on short clips — a 30-90s voice note transcribes in a few
  seconds even on `medium`. Drop to `--model small` only if you're
  processing a long batch of notes and speed matters more than nailing
  jargon/names. Bump to `large-v3` if a first pass reads garbled.
- Auto-detect language by default. If the note is business jargon, mixed
  language, or dialect-heavy, forcing `--language it` (or whichever
  language the user's notes are normally in) measurably improves accuracy
  over auto-detect — use it when you know the sender's usual language.
- The script needs `ffmpeg`. If missing, give the user the one-line install
  command instead of working around it.

Each input produces `<name>.transcript.txt` (timestamped segments + full
text) in the output dir. Read the `## FULL TEXT` section of each —
timestamps aren't needed for a voice note reply.

### 3. Assemble the text

- **Single file**: take the full text as-is. Fix obvious Whisper artifacts
  (a mis-heard word that breaks the sentence's meaning, a repeated word) by
  checking it against the surrounding context, but do not paraphrase or
  clean up the actual wording/register — a voice note should read like what
  was said, not like an edited memo.
- **Burst of files**: concatenate the full texts in filename/timestamp
  order into one continuous message, as if recorded in a single take. Only
  add a paragraph break where there's an audible restart worth preserving
  (a "cioè, allora" type restart) — otherwise flow it together.
- Keep the transcript in the language it was spoken. Do not translate
  unless asked.
- If the note is long and rambling (roughly 150+ words, or it visibly jumps
  between unrelated topics), add one short TL;DR line above the transcript
  so the user gets the point before reading the whole thing. Skip the TL;DR
  for short, already-clear notes — it would just be noise.

### 4. Deliver

Reply directly in the chat with the transcript — do not create a saved
file by default, a voice note doesn't warrant one. Format:

```
🎙️ Nota vocale WhatsApp · {durata totale} · {lingua rilevata}

{TL;DR, solo se il messaggio è lungo o disordinato}

{trascrizione, come testo scorrevole}
```

Only save a file (`.md` or `.txt`, same convention as
`audio-video-transcript`) if the user explicitly asks to keep/export it, or
if there are several unrelated notes to process in one batch (e.g. a whole
day's worth of voice notes) — in that case use one file per note, or one
file with a note-by-note breakdown, whichever the user prefers.

## Notes & limits

- **Background noise**: voice notes are often recorded on the street, in a
  car, or in a noisy room. If the transcript comes out garbled, retry once
  with `--model large-v3` before telling the user it's unclear.
- **Dialect / mixed language / slang / jargon**: Whisper handles standard
  speech well; heavy dialect, fast code-switching (e.g. IT/EN mid-sentence),
  or company-specific jargon can produce plausible-sounding but wrong words
  (e.g. a term that sounds like a common word). Cross-check anything that
  breaks the sentence's logic against context rather than transcribing it
  literally, and flag genuinely uncertain passages with `[?]` rather than
  guessing silently.
- **Privacy**: everything runs locally — no audio or text is uploaded
  anywhere.
- **Not for**: meetings, podcasts, interviews, lectures, or anything you'd
  want a timestamped transcript + structured recap for — use
  `audio-video-transcript` for those.
