#!/usr/bin/env python3
"""Is the generated copy accountable to the code?

The shipped harness proves a mechanic is covered. It cannot read English, so a
coachmark that states the wrong number passes every check it has. That is not
hypothetical: the shipped `cascade-bank` moment says a cascade banks RAM at
"Four or more nodes" and `kit.ts:cascadeRam` returns 0 only when `lit < 3`.

This closes the mechanical half of that gap. It does not decide whether a
sentence is true, which needs judgment; it decides whether the sentence can be
checked at all, and it puts the real source in front of the checker.

Three things it enforces:

  1. Every number a player-visible line states is covered by a `claim`.
  2. Every claimed `symbol` resolves to real code in game/.
  3. A critic verdict's `quote` is a literal substring of the file it cites.

    python3 tools/verify_copy.py runs/<RUN>/generated/*.json
    python3 tools/verify_copy.py --report out.json runs/<RUN>/generated/*.json
    python3 tools/verify_copy.py --kind verdict runs/<RUN>/critic/*.json
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game" / "src"

WORDS = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "twice": 2,
}
NUMBER = re.compile(r"\b(\d+)\b|\b(" + "|".join(WORDS) + r")\b", re.I)

# "one" is deliberately NOT checkable. In this copy register it is nearly
# always the indefinite article ("one rotation", "one node at a time", "one
# unturned junction") rather than a quantity any symbol holds, and flagging it
# buried the real findings three deep. A checker that flags everything proves
# nothing. The cost of the exclusion is stated in the README: a wrong "one" in
# generated copy is the critic's to catch, not this tool's.
#
# Digits are always checkable, so "1 RAM" is still caught. Only the word is
# exempt.


def numbers_in(text: str) -> list:
    """Every quantity a line asserts, digits and number words alike."""
    out = []
    for digit, word in NUMBER.findall(text):
        out.append(digit if digit else word.lower())
    return out


def player_copy(item: dict) -> list:
    """Every string this item puts in front of a player."""
    out = []
    if item.get("action") == "coachmark" and item.get("moment"):
        m = item["moment"]
        out.append(("title", m.get("title", "")))
        for i, line in enumerate(m.get("lines") or []):
            out.append((f"line {i + 1}", line))
    if item.get("action") == "tip" and item.get("tip"):
        out.append(("tip text", item["tip"].get("text", "")))
    if item.get("action") == "label" and item.get("label"):
        out.append(("label", item["label"].get("after", "")))
    if item.get("waiver"):
        out.append(("waiver", item["waiver"].get("text", "")))
    return [(w, t) for w, t in out if t]


def find_file(name: str) -> Path:
    """Resolve a bare filename or a partial path against the vendored slice."""
    cand = [p for p in GAME.rglob("*") if p.is_file() and p.as_posix().endswith(name)]
    if not cand:
        stem = name.split("/")[-1]
        cand = [p for p in GAME.rglob(stem) if p.is_file()]
    return sorted(cand, key=lambda p: len(p.as_posix()))[0] if cand else None


def resolve(symbol: str) -> dict:
    """`file.ts:symbolName` -> the real declaration, with its line number."""
    file_part, _, sym = symbol.partition(":")
    sym = sym.split(".")[0]
    path = find_file(file_part)
    if path is None:
        return {"symbol": symbol, "found": False, "why": f"no file matching {file_part} in game/src"}

    rel = path.relative_to(ROOT).as_posix()
    if not sym:
        return {"symbol": symbol, "found": True, "file": rel, "line": 0, "source": ""}

    lines = path.read_text().splitlines()
    pat = re.compile(r"\b(const|let|function|class|type|interface|enum)\s+" + re.escape(sym) + r"\b")
    hit = next((i for i, l in enumerate(lines) if pat.search(l)), None)
    if hit is None:
        pat2 = re.compile(r"^\s*" + re.escape(sym) + r"\s*[:(=]")
        hit = next((i for i, l in enumerate(lines) if pat2.search(l)), None)
    if hit is None:
        return {
            "symbol": symbol, "found": False, "file": rel,
            "why": f"{rel} has no declaration of {sym}",
        }

    # Enough of the body to judge a threshold by, and no more.
    end = hit
    depth = 0
    for i in range(hit, min(hit + 24, len(lines))):
        depth += lines[i].count("{") - lines[i].count("}")
        end = i
        if i > hit and depth <= 0:
            break
        if depth == 0 and lines[i].rstrip().endswith(";"):
            break

    return {
        "symbol": symbol, "found": True, "file": rel, "line": hit + 1,
        "source": "\n".join(lines[hit : end + 1]),
    }


def check_draft(path: Path) -> tuple:
    item = json.loads(path.read_text())
    fails, resolutions = [], []

    claims = item.get("claims") or []
    claim_text = " ".join(c.get("text", "") for c in claims).lower()

    for where, text in player_copy(item):
        for n in numbers_in(text):
            word = next((w for w, v in WORDS.items() if str(v) == n), None)
            covered = n in claim_text or (word and word in claim_text)
            if not covered and n in WORDS:
                covered = str(WORDS[n]) in claim_text
            if not covered:
                fails.append(
                    f'{where} states "{n}" but no claim covers it. '
                    f"Name the symbol that holds the number, or take the number out"
                )

    for c in claims:
        r = resolve(c.get("symbol", ""))
        r["claimed"] = c.get("text", "")
        r["resolves"] = c.get("resolves", "")
        resolutions.append(r)
        if not r["found"]:
            fails.append(f'claim "{c.get("text")}" cites {c.get("symbol")}: {r.get("why")}')

    return fails, {"item": path.name, "gap": item.get("gap"), "resolutions": resolutions}


def check_verdict(path: Path) -> list:
    v = json.loads(path.read_text())
    fails = []
    if v.get("verdict") not in ("APPROVE", "REVISE"):
        fails.append(f'verdict must be APPROVE or REVISE, got {v.get("verdict")}')
    if v.get("verdict") == "REVISE":
        if not v.get("objection"):
            fails.append("a REVISE with no objection is a complaint, not a verdict")
        if not v.get("required"):
            fails.append("a REVISE has to say what would fix it")

    for c in v.get("claims", []):
        quote, symbol = c.get("quote", ""), c.get("symbol", "")
        if not quote:
            fails.append(f'claim "{c.get("text")}" has no quote; a verdict has to substantiate itself')
            continue
        r = resolve(symbol)
        if not r["found"]:
            fails.append(f'claim "{c.get("text")}" cites {symbol}: {r.get("why")}')
            continue
        body = (ROOT / r["file"]).read_text()
        if quote.strip() not in body:
            fails.append(
                f'quote for "{c.get("text")}" is not a literal substring of {r["file"]}: {quote.strip()!r}'
            )
    return fails


def main() -> int:
    args = sys.argv[1:]
    kind = "draft"
    report = ""
    if "--kind" in args:
        i = args.index("--kind")
        kind = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if "--report" in args:
        i = args.index("--report")
        report = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if not args:
        print("usage: verify_copy.py [--kind draft|verdict] [--report f.json] <files>", file=sys.stderr)
        return 2

    total, reports = 0, []
    for a in args:
        p = Path(a)
        if kind == "verdict":
            fails = check_verdict(p)
        else:
            fails, rep = check_draft(p)
            reports.append(rep)
        total += len(fails)
        if fails:
            print(f"FAIL {p.name}")
            for f in fails:
                print(f"  - {f}")
        else:
            print(f"ok   {p.name}")

    if kind == "draft":
        # The juxtaposition IS the product. Printing only the declaration line
        # would hide the threshold the critic has to judge, which is the one
        # thing this tool exists to surface.
        print("\nclaims resolved against the code:")
        for rep in reports:
            for r in rep["resolutions"]:
                if r["found"] and r.get("source"):
                    print(f'\n  {r["symbol"]}   ({r["file"]}:{r["line"]})')
                    print(f'      copy says:  "{r["claimed"]}"')
                    print(f'      author says: {r["resolves"]}')
                    print("      the code:")
                    for line in r["source"].splitlines()[:10]:
                        print(f"        {line}")
        if report:
            Path(report).write_text(
                json.dumps({"schema": "kp-copy-report/1", "items": reports}, indent=2) + "\n"
            )
            print(f"\nwrote {report}")

    print()
    if total:
        print(f"verify_copy: {total} problem(s)")
        return 1
    print(f"verify_copy: {len(args)} file(s) clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
