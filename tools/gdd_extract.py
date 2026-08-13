#!/usr/bin/env python3
"""Structural feature candidates from the frozen GDD.

This does the part a regex does better than a model: enumerate the notes,
filter out the ones that are not features, and pull the three places the vault
names code.

It deliberately does NOT decide what is player-facing or write the
"what the player must understand" line. Those are judgment, and they belong to
the gdd-reader seat. What comes out of here is a candidate list with its
provenance attached.

    python3 tools/gdd_extract.py                 summary
    python3 tools/gdd_extract.py --json          the full candidate list
    python3 tools/gdd_extract.py --note <path>   one note, with its extraction
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GDD = ROOT / "gdd"

# Areas that describe the game the player plays. Everything else in the vault
# is process, business, or house style.
FEATURE_AREAS = ("20-mechanics", "30-content", "40-presentation", "70-teaching")

# Excluded with the reason, so the run report can state what was dropped and
# why rather than silently narrowing the corpus.
EXCLUSIONS = [
    ("superseded", lambda p, fm: "superseded" in p.parts, "describes a deleted system"),
    ("unwritten", lambda p, fm: fm.get("status") == "unwritten", "no decision exists yet"),
    ("rulings", lambda p, fm: fm.get("source") == "rulings", "house style law, not a feature"),
    ("index", lambda p, fm: p.parts[0] in ("00-index", "_templates"), "index or template"),
    ("non-feature-area", lambda p, fm: p.parts[0] not in FEATURE_AREAS, "not a feature area"),
]

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
SOURCE_CALLOUT = re.compile(r"^> \[!info\] Source\n((?:^> .*\n)+)", re.M)
CODE_TOKEN = re.compile(r"`([A-Za-z0-9_./-]+\.tsx?)(?::([A-Za-z0-9_.]+))?`|`([A-Za-z_][A-Za-z0-9_]*)`")
AUGMENT_BYLINE = re.compile(r"^\*\*(Boost|Config)\*\*\s*·\s*`([^`]+)`(.*)$", re.M)
WINDOW_BYLINE = re.compile(r"^`([a-zA-Z]+)`\s*·\s*`([^`]+\.tsx)`", re.M)
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def frontmatter(text: str) -> dict:
    m = FM.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip('"')
    return out


def body(text: str) -> str:
    m = FM.match(text)
    return text[m.end() :] if m else text


def source_symbols(text: str) -> list:
    """Code symbols from the `> [!info] Source` callout."""
    m = SOURCE_CALLOUT.search(text)
    if not m:
        return []
    block = m.group(1)
    out = []
    for file_tok, sym, bare in CODE_TOKEN.findall(block):
        if file_tok:
            out.append(f"{file_tok}:{sym}" if sym else file_tok)
        elif bare and out:
            # A bare `symbol` continues the last named file.
            last_file = out[-1].split(":")[0]
            out.append(f"{last_file}:{bare}")
    return out


def thesis(text: str) -> str:
    """The one-sentence claim after the H1 and the Source callout.

    Positionally consistent across the vault, and the closest thing to a
    machine-extractable feature statement.
    """
    lines = body(text).splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s or s.startswith(("#", ">", "|", "-", "*", "`", "!")):
            continue
        return s
    return ""


def extract(path: Path) -> dict:
    rel = path.relative_to(GDD)
    text = path.read_text()
    fm = frontmatter(text)
    b = body(text)

    dropped = None
    for name, test, why in EXCLUSIONS:
        if test(rel, fm):
            dropped = {"rule": name, "why": why}
            break

    rec = {
        "note": rel.as_posix(),
        "area": rel.parts[0],
        "title": fm.get("title", ""),
        "status": fm.get("status", ""),
        "source": fm.get("source", ""),
        "owner": fm.get("owner", ""),
        "excluded": dropped,
        "symbols": source_symbols(b),
        "thesis": thesis(text),
        "links": sorted(set(WIKILINK.findall(b))),
        "bytes": len(text),
    }

    aug = AUGMENT_BYLINE.search(b)
    if aug:
        rec["augment"] = {"kind": aug.group(1), "codeId": aug.group(2)}
        rec["symbols"] = rec["symbols"] or [f"content/kit.ts:AUGMENTS.{aug.group(2)}"]

    win = WINDOW_BYLINE.search(b)
    if win:
        rec["window"] = {"screenId": win.group(1), "file": win.group(2)}
        rec["symbols"] = rec["symbols"] or [win.group(2)]

    return rec


def all_notes() -> list:
    return [extract(p) for p in sorted(GDD.rglob("*.md"))]


def main() -> int:
    args = sys.argv[1:]

    if "--note" in args:
        target = args[args.index("--note") + 1]
        print(json.dumps(extract(GDD / target), indent=2))
        return 0

    notes = all_notes()
    kept = [n for n in notes if not n["excluded"]]

    if "--json" in args:
        print(json.dumps({"schema": "kp-gdd-candidates/1", "candidates": kept}, indent=2))
        return 0

    print(f"{len(notes)} notes in gdd/, {len(kept)} feature candidates\n")
    print("excluded:")
    for name, _, why in EXCLUSIONS:
        n = sum(1 for x in notes if x["excluded"] and x["excluded"]["rule"] == name)
        if n:
            print(f"  {n:4}  {name:18} {why}")
    print("\nkept, by area:")
    for area in FEATURE_AREAS:
        rows = [n for n in kept if n["area"] == area]
        withsym = sum(1 for n in rows if n["symbols"])
        print(f"  {len(rows):4}  {area:18} {withsym} carry code symbols")
    print(f"\n{sum(1 for n in kept if n.get('augment'))} augments, "
          f"{sum(1 for n in kept if n.get('window'))} windows resolved by byline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
