#!/usr/bin/env python3
"""Create a privacy-conscious inventory for an Agent Reliability Audit.

The scanner records file metadata and bounded structural signals. It does not decide
whether knowledge is correct, current, approved, or safe; those judgments require the
audit protocol and source inspection.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_EXTENSIONS = {
    ".csv",
    ".htm",
    ".html",
    ".json",
    ".jsonl",
    ".md",
    ".rst",
    ".toml",
    ".tsv",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

IGNORED_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".next",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

GOVERNANCE_FIELDS = {
    "approver",
    "date",
    "effective_date",
    "last_reviewed",
    "owner",
    "review_after",
    "reviewed",
    "sensitivity",
    "source",
    "status",
    "superseded_by",
    "supersedes",
    "updated",
    "valid_until",
    "version",
}

DATE_RE = re.compile(r"\b(?:19|20)\d{2}-[01]\d-[0-3]\d\b")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$")
URL_OR_MD_LINK_RE = re.compile(r"https?://|\[[^\]]+\]\([^)]+\)")
OPEN_MARKER_RE = re.compile(
    r"\b(?:TODO|FIXME|TBD|OPEN QUESTION|DA FARE|DA VERIFICARE)\b", re.IGNORECASE
)
DECISION_RE = re.compile(
    r"\b(?:decision|decided|decisione|deciso|approved|approvato)\b", re.IGNORECASE
)
EXCEPTION_RE = re.compile(
    r"\b(?:except|exception|unless|tranne|eccezion|salvo)\w*\b", re.IGNORECASE
)
POSSIBLE_SECRET_RE = re.compile(
    r"(?im)^\s*(?:api[_-]?key|password|passwd|secret|access[_-]?token)\s*[:=]\s*\S+"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory text-like workspace files for an Agent Reliability Audit."
    )
    parser.add_argument("root", type=Path, help="Workspace or source root to scan")
    parser.add_argument(
        "--output", "-o", type=Path, help="Write JSON here; defaults to stdout"
    )
    parser.add_argument(
        "--extensions",
        help="Comma-separated extensions, e.g. .md,.txt,.json (defaults to safe text types)",
    )
    parser.add_argument(
        "--max-files", type=int, default=10_000, help="Stop after this many candidate files"
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=5_000_000,
        help="Do not parse/hash files larger than this many bytes",
    )
    return parser.parse_args()


def parse_extensions(raw: str | None) -> set[str]:
    if not raw:
        return DEFAULT_EXTENSIONS
    result = set()
    for item in raw.split(","):
        value = item.strip().lower()
        if not value:
            continue
        result.add(value if value.startswith(".") else f".{value}")
    if not result:
        raise ValueError("--extensions did not contain any usable extension")
    return result


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = FRONTMATTER_KEY_RE.match(line)
        if not match:
            continue
        key = match.group(1).lower().replace("-", "_")
        value = match.group(2).strip().strip("\"'")
        if key in GOVERNANCE_FIELDS:
            fields[key] = value[:200]
    return fields


def file_record(path: Path, root: Path, max_bytes: int, now: datetime) -> dict:
    stat = path.stat()
    relative = path.relative_to(root).as_posix()
    modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
    base = {
        "path": relative,
        "extension": path.suffix.lower(),
        "bytes": stat.st_size,
        "modified_at": modified.isoformat(),
        "age_days": max(0, (now - modified).days),
    }
    if stat.st_size > max_bytes:
        return {**base, "parse_status": "too_large", "max_bytes": max_bytes}

    data = path.read_bytes()
    text = data.decode("utf-8", errors="replace")
    frontmatter = parse_frontmatter(text)
    heading = HEADING_RE.search(text)
    dates = sorted(set(DATE_RE.findall(text)))[:10]

    return {
        **base,
        "parse_status": "parsed",
        "sha256": hashlib.sha256(data).hexdigest(),
        "lines": text.count("\n") + (1 if text else 0),
        "title": (heading.group(1).strip() if heading else path.stem)[:300],
        "governance": frontmatter,
        "signals": {
            "iso_dates_sample": dates,
            "reference_marker_count": len(URL_OR_MD_LINK_RE.findall(text)),
            "open_marker_count": len(OPEN_MARKER_RE.findall(text)),
            "decision_marker_count": len(DECISION_RE.findall(text)),
            "exception_marker_count": len(EXCEPTION_RE.findall(text)),
            "possible_secret_assignment": bool(POSSIBLE_SECRET_RE.search(text)),
        },
    }


def scan(root: Path, extensions: set[str], max_files: int, max_bytes: int) -> dict:
    now = datetime.now(timezone.utc)
    records = []
    skipped = Counter()
    unsupported_extensions = Counter()

    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        for name in sorted(files):
            path = Path(current) / name
            if path.suffix.lower() not in extensions:
                skipped["unsupported_extension"] += 1
                unsupported_extensions[path.suffix.lower() or "[no extension]"] += 1
                continue
            if len(records) >= max_files:
                skipped["max_files_reached"] += 1
                continue
            try:
                records.append(file_record(path, root, max_bytes, now))
            except (OSError, UnicodeError) as exc:
                skipped[f"read_error:{type(exc).__name__}"] += 1

    extensions_count = Counter(item["extension"] for item in records)
    parsed = [item for item in records if item.get("parse_status") == "parsed"]
    with_governance = [item for item in parsed if item.get("governance")]

    def has_any(item: dict, fields: set[str]) -> bool:
        return bool(fields.intersection(item.get("governance", {})))

    summary = {
        "generated_at": now.isoformat(),
        "root": str(root),
        "candidate_file_count": len(records),
        "parsed_file_count": len(parsed),
        "total_bytes": sum(item["bytes"] for item in records),
        "extensions": dict(sorted(extensions_count.items())),
        "skipped": dict(sorted(skipped.items())),
        "unsupported_extensions": dict(sorted(unsupported_extensions.items())),
        "governance_signals": {
            "files_with_any_frontmatter_governance": len(with_governance),
            "files_with_owner": sum(has_any(item, {"owner"}) for item in parsed),
            "files_with_status": sum(has_any(item, {"status"}) for item in parsed),
            "files_with_source": sum(has_any(item, {"source"}) for item in parsed),
            "files_with_review_signal": sum(
                has_any(item, {"reviewed", "last_reviewed", "review_after", "valid_until"})
                for item in parsed
            ),
            "files_with_supersession_signal": sum(
                has_any(item, {"supersedes", "superseded_by", "version"}) for item in parsed
            ),
        },
        "warning": (
            "Structural signals are inventory aids, not findings. Age is not proof of "
            "staleness; readability is not proof of authorization; marker counts are not "
            "proof of governance or quality."
        ),
    }
    return {"summary": summary, "files": sorted(records, key=lambda item: item["path"])}


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    if args.max_files < 1 or args.max_bytes < 1:
        print("error: --max-files and --max-bytes must be positive", file=sys.stderr)
        return 2

    try:
        extensions = parse_extensions(args.extensions)
        payload = scan(root, extensions, args.max_files, args.max_bytes)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(
            f"Inventoried {payload['summary']['candidate_file_count']} files -> {output}",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
