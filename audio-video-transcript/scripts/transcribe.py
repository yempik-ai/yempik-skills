#!/usr/bin/env python3
"""
transcribe.py — Local audio/video -> timestamped transcript.

Does the deterministic heavy lifting only:
  1. Convert any audio/video file to 16kHz mono WAV via ffmpeg.
  2. Transcribe locally with the best available Whisper backend
     (mlx-whisper on Apple Silicon > faster-whisper > openai-whisper).
  3. Write two artifacts next to the chosen output dir:
       <name>.transcript.txt  -> timestamped segments + clean full text
       <name>.segments.json   -> machine-readable segments + metadata

The recap/summary is intentionally NOT produced here — that is written by
Claude after reading the .transcript.txt, so it stays smart and adaptive.

Usage:
  python transcribe.py INPUT [INPUT ...] [--out DIR] [--model NAME]
                       [--language CODE] [--no-install]

Examples:
  python transcribe.py meeting.mp4
  python transcribe.py interview.mp3 --model large-v3 --language it
  python transcribe.py *.wav --out ./transcripts
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime

AUDIO_VIDEO_EXTS = {
    ".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".opus", ".wma",
    ".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v", ".flv", ".3gp", ".aiff",
}


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def fmt_ts(seconds):
    seconds = max(0, int(round(seconds)))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        log("ERROR: ffmpeg not found. Install it first:")
        log("  macOS:  brew install ffmpeg")
        log("  Debian: sudo apt install ffmpeg")
        sys.exit(2)


def to_wav(src, tmpdir):
    """Extract/convert to 16kHz mono 16-bit WAV (what Whisper expects)."""
    dst = os.path.join(tmpdir, "audio.wav")
    cmd = [
        "ffmpeg", "-y", "-i", src,
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        dst,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0 or not os.path.exists(dst):
        log(f"ERROR: ffmpeg failed to convert {src}")
        log(proc.stderr[-1500:])
        sys.exit(3)
    return dst


def media_duration(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True,
        )
        return float(out.stdout.strip())
    except Exception:
        return None


def pick_backend(no_install):
    """Return a backend name, installing faster-whisper if nothing is present."""
    import importlib.util as iutil

    def has(name):
        return iutil.find_spec(name) is not None

    # Prefer Apple-Silicon-optimized mlx, then faster-whisper, then openai.
    if has("mlx_whisper"):
        return "mlx"
    if has("faster_whisper"):
        return "faster"
    if has("whisper"):
        return "openai"

    if no_install:
        log("ERROR: no Whisper backend installed and --no-install was set.")
        log("Install one of:  pip install faster-whisper   (or mlx-whisper on Apple Silicon)")
        sys.exit(4)

    log("No Whisper backend found. Installing faster-whisper (one-time)...")
    rc = subprocess.run(
        [sys.executable, "-m", "pip", "install", "faster-whisper"],
    ).returncode
    if rc != 0:
        # Sandboxed/system Python may need this flag.
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--break-system-packages",
             "faster-whisper"],
        )
    if has("faster_whisper"):
        return "faster"
    log("ERROR: could not install a Whisper backend automatically.")
    log("Please run:  pip install faster-whisper")
    sys.exit(4)


def transcribe_faster(wav, model_name, language):
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="auto", compute_type="auto")
    segments, info = model.transcribe(
        wav, language=language, vad_filter=True, beam_size=5,
    )
    segs = [{"start": s.start, "end": s.end, "text": s.text.strip()}
            for s in segments]
    return segs, getattr(info, "language", language)


def transcribe_mlx(wav, model_name, language):
    import mlx_whisper
    repo = model_name
    if "/" not in model_name:  # map plain names to mlx-community repos
        repo = f"mlx-community/whisper-{model_name}-mlx"
    kwargs = {"path_or_hf_repo": repo}
    if language:
        kwargs["language"] = language
    result = mlx_whisper.transcribe(wav, **kwargs)
    segs = [{"start": s["start"], "end": s["end"], "text": s["text"].strip()}
            for s in result.get("segments", [])]
    return segs, result.get("language", language)


def transcribe_openai(wav, model_name, language):
    import whisper
    model = whisper.load_model(model_name)
    result = model.transcribe(wav, language=language, verbose=False)
    segs = [{"start": s["start"], "end": s["end"], "text": s["text"].strip()}
            for s in result.get("segments", [])]
    return segs, result.get("language", language)


def normalize_model_name(model, backend):
    # openai-whisper has no "large-v3" by default name? it does. Keep as-is.
    return model


def write_outputs(out_dir, base, src, segs, lang, model, backend, duration):
    os.makedirs(out_dir, exist_ok=True)
    txt_path = os.path.join(out_dir, f"{base}.transcript.txt")
    json_path = os.path.join(out_dir, f"{base}.segments.json")

    full_text = " ".join(s["text"] for s in segs).strip()
    word_count = len(full_text.split())

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript artifact (raw) — {base}\n")
        f.write(f"# source_file: {os.path.basename(src)}\n")
        f.write(f"# duration: {fmt_ts(duration) if duration else 'unknown'}\n")
        f.write(f"# language: {lang}\n")
        f.write(f"# model: {model}  backend: {backend}\n")
        f.write(f"# transcribed_at: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"# word_count: {word_count}\n")
        f.write("#\n")
        f.write("## TIMESTAMPED SEGMENTS\n")
        for s in segs:
            f.write(f"[{fmt_ts(s['start'])}] {s['text']}\n")
        f.write("\n## FULL TEXT (no timestamps)\n")
        f.write(full_text + "\n")

    meta = {
        "source_file": os.path.basename(src),
        "duration_seconds": duration,
        "language": lang,
        "model": model,
        "backend": backend,
        "transcribed_at": datetime.now().isoformat(timespec="seconds"),
        "word_count": word_count,
        "segments": segs,
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    return txt_path, json_path, word_count


def main():
    ap = argparse.ArgumentParser(description="Local audio/video -> timestamped transcript")
    ap.add_argument("inputs", nargs="+", help="Audio/video file(s)")
    ap.add_argument("--out", default=".", help="Output directory (default: current dir)")
    ap.add_argument("--model", default="medium",
                    help="Whisper model: tiny/base/small/medium/large-v3 (default: medium)")
    ap.add_argument("--language", default=None,
                    help="Force language code (e.g. it, en). Default: auto-detect")
    ap.add_argument("--no-install", action="store_true",
                    help="Do not auto-install a backend if none is present")
    args = ap.parse_args()

    check_ffmpeg()
    backend = pick_backend(args.no_install)
    log(f"Using backend: {backend} | model: {args.model} | "
        f"language: {args.language or 'auto'}")

    results = []
    for src in args.inputs:
        if not os.path.exists(src):
            log(f"SKIP (not found): {src}")
            continue
        ext = os.path.splitext(src)[1].lower()
        if ext not in AUDIO_VIDEO_EXTS:
            log(f"WARNING: unrecognized extension '{ext}', trying anyway: {src}")

        base = os.path.splitext(os.path.basename(src))[0]
        log(f"\n=== {src} ===")
        duration = media_duration(src)
        with tempfile.TemporaryDirectory() as tmp:
            wav = to_wav(src, tmp)
            log("Transcribing... (this can take a while for long files)")
            model = normalize_model_name(args.model, backend)
            if backend == "mlx":
                segs, lang = transcribe_mlx(wav, model, args.language)
            elif backend == "faster":
                segs, lang = transcribe_faster(wav, model, args.language)
            else:
                segs, lang = transcribe_openai(wav, model, args.language)

        txt, js, wc = write_outputs(args.out, base, src, segs, lang,
                                    model, backend, duration)
        log(f"OK: {wc} words, language={lang}")
        log(f"  -> {txt}")
        log(f"  -> {js}")
        results.append({"source": src, "transcript_txt": txt,
                        "segments_json": js, "words": wc, "language": lang,
                        "duration_seconds": duration})

    # Machine-readable summary to stdout for the caller (Claude) to consume.
    print(json.dumps({"transcribed": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
