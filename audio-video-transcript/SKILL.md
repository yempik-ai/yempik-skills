---
name: audio-video-transcript
description: >-
  Transcribe local audio/video files (mp3, wav, m4a, flac, ogg, mp4, mov, mkv,
  webm and similar) entirely on-device with Whisper, then produce ONE markdown
  file containing a structured recap PLUS the full timestamped transcript. Use
  this skill whenever the user uploads or points to an audio or video file and
  wants it transcribed, summarized, "sbobinato", turned into notes, meeting
  minutes, or a written recap — even if they just drop a media file and say
  "trascrivi questo", "fammi il transcript", "riassumi questa call/registrazione",
  or "what's in this recording". Trigger for podcasts, interviews, meetings,
  lectures, voice memos, and webinar recordings. Do NOT use for YouTube links
  (use the youtube-transcript skill) or for files whose text is already provided.
---

# Audio / Video Transcript + Recap

Turn a local media file into a single, standardized markdown document:
a recap at the top, the full timestamped transcript below. Everything runs
locally — audio never leaves the machine.

The work splits in two:

- **`scripts/transcribe.py`** does the deterministic part: convert the file
  with ffmpeg and run Whisper locally to get timestamped segments + clean text.
- **You (Claude)** read that raw transcript and write the intelligent recap,
  then assemble the final `.md`.

## Workflow

### 1. Locate the input
Find the media file the user referenced (check the uploads directory and the
conversation). Supported: mp3, wav, m4a, aac, flac, ogg, opus, mp4, mov, mkv,
webm, avi, and similar. Video files are fine — the script strips the audio.

### 2. Run the transcription script
```bash
python scripts/transcribe.py "<path-to-file>" --out "<output-dir>"
```
Useful options:
- `--model large-v3` — highest accuracy (slower; great on Apple Silicon).
  Default is `medium`. Use `small` for speed on long files / weak CPUs.
- `--language it` — force a language instead of auto-detecting. Auto-detect is
  reliable for clean audio; force it for noisy or code-switched recordings.

The script picks the fastest available backend automatically (mlx-whisper on
Apple Silicon, else faster-whisper, else openai-whisper) and installs
faster-whisper once if none is present. It needs `ffmpeg` on the system
(`brew install ffmpeg` on macOS).

It writes `<name>.transcript.txt` (timestamped segments + full text) and
`<name>.segments.json` into the output dir, and prints a JSON summary.

If transcription fails because ffmpeg is missing, tell the user the one-line
install command rather than trying to work around it.

### 3. Read the raw transcript
Open the generated `<name>.transcript.txt`. The header lines (`# duration`,
`# language`, `# model`, `# word_count`) give you the metadata for the final
document. The timestamped segments give you anchors for the transcript section.

### 4. Write the recap
Read the whole transcript and write a recap **in the same language as the
audio** (e.g. Italian audio → Italian recap), unless the user asked otherwise.
The recap is the value-add: it must be genuinely useful, not a restatement.

Adapt the recap to the *kind* of recording — don't force empty sections:
- **Meeting / call** → decisions made + action items (with owners if named) are
  the priority.
- **Interview / podcast** → main themes, notable points, memorable quotes.
- **Lecture / webinar** → concepts explained, structure, takeaways.
- **Voice memo / note** → tighten it into clear bullet points.

Always include the "In sintesi" and "Punti chiave" blocks. Include the others
only when the content supports them. Keep bullets concrete and specific
(names, numbers, dates) rather than vague.

### 5. Assemble the final markdown
Combine recap + transcript into ONE file using the template below, save it to
the output directory as `<name>.md`, and present it to the user. Do NOT leave
the transcript and recap as separate files — the deliverable is a single `.md`.
The intermediate `.transcript.txt` / `.segments.json` can stay as by-products.

## Output template (use exactly this structure)

```markdown
# {Titolo descrittivo} — Trascrizione & Recap

> **File:** {nome file originale}
> **Durata:** {hh:mm:ss}
> **Lingua:** {lingua rilevata}
> **Parole:** {word_count}
> **Trascritto il:** {data}  ·  **Modello:** {model}

## 📋 Recap

### In sintesi
{2–4 frasi che spiegano di cosa si tratta e l'esito, leggibili da sole}

### Punti chiave
- {punto concreto}
- {punto concreto}

### Decisioni / Conclusioni        ← includi solo se pertinente
- {decisione}

### Action item                    ← includi solo se pertinente
- [ ] {azione} — {responsabile se citato}

### Argomenti trattati             ← includi solo se pertinente
- {tema} ({timestamp di inizio})

---

## 📝 Trascrizione completa

[00:00:00] {testo}
[00:00:14] {testo}
...
```

## Notes & limits
- **Long files**: transcription time scales with audio length and model size.
  Warn the user a 1-hour recording may take a while; suggest `--model small`
  if they want speed over precision.
- **Speaker labels**: this skill does not separate speakers (diarization) by
  default. If the user explicitly needs "who said what", say it's a heavier
  add-on (pyannote + a Hugging Face token) and offer to wire it up separately.
- **Accuracy**: clean speech transcribes well; heavy background noise, crosstalk,
  or strong accents lower quality. `large-v3` helps most in hard cases.
- **Privacy**: everything is local — no audio or text is uploaded anywhere.
