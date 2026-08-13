#!/usr/bin/env python3
"""Plant the teaching gaps, reproducibly.

Reads gaps/plan.json, restores the two mutable game files from
gaps/pristine/, then surgically removes the coverage named in the plan and
records exactly what it removed in gaps/removed.json.

Restore-then-strip makes this idempotent: run it ten times and the result is
byte-identical, and `--restore` puts the slice back to upstream.

The removals are text-surgical rather than a stored diff so that the "before"
state is derived from the real upstream file every time. Nothing here is
hand-authored, which is the whole point: a grader can delete game/ and
gaps/removed.json, re-run freeze.py and this script, and get the same before
state the committed run started from.

    python3 tools/make_gap.py            plant
    python3 tools/make_gap.py --restore  put it back
    python3 tools/make_gap.py --check    report which gaps are currently open
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
PRISTINE = ROOT / "gaps" / "pristine"

TEACHING = "src/game/content/teaching.ts"
DUEL = "src/components/game/duel.tsx"

# Which exported array each gap kind lives in. Scoping the search matters:
# `id: "ram"` appears twice in teaching.ts, once as a MECHANIC_INVENTORY row
# and once as a TEACH_TIPS entry, and cutting the wrong one produces a
# different failure that looks superficially similar.
SECTION = {
    "teaching-moment": "TEACHING",
    "teach-tip": "TEACH_TIPS",
    "mechanic-waiver": "MECHANIC_INVENTORY",
}


def restore() -> None:
    for rel, name in ((TEACHING, "teaching.ts"), (DUEL, "duel.tsx")):
        (GAME / rel).write_bytes((PRISTINE / name).read_bytes())


def find_section(lines: list, name: str) -> tuple:
    """Line range of an `export const NAME ... = [ ... ];` array."""
    start = next(
        (i for i, l in enumerate(lines) if l.startswith(f"export const {name}")), None
    )
    if start is None:
        raise SystemExit(f"make_gap: no export const {name}")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("];")), None)
    if end is None:
        raise SystemExit(f"make_gap: unterminated {name}")
    return start + 1, end


def find_entry(lines: list, section: str, entry_id: str):
    """Index of the line carrying `id: "<entry_id>"`, inside one array only.

    Matches both the multi-line shape (`id: "x",` on its own line) and the
    one-line shape (`{ id: "x", label: ... },`).
    """
    lo, hi = find_section(lines, section)
    pat = re.compile(r'(^|\{\s*)id:\s*"' + re.escape(entry_id) + r'"\s*,')
    return next((i for i in range(lo, hi) if pat.search(lines[i].strip())), None)


def cut_object(lines: list, section: str, entry_id: str) -> tuple:
    """Remove the object literal in an array whose `id:` field is entry_id.

    Walks back from the id line to the `{` that opens it and forward to the
    matching `}`, so a nested object or a multi-line `lines: [...]` array
    cannot truncate the cut in the wrong place.
    """
    hit = find_entry(lines, section, entry_id)
    if hit is None:
        return lines, None

    start = hit
    while start >= 0 and not lines[start].strip().startswith("{"):
        start -= 1
    if start < 0:
        raise SystemExit(f"make_gap: no opening brace above {entry_id}")

    depth = 0
    end = start
    for i in range(start, len(lines)):
        depth += lines[i].count("{") - lines[i].count("}")
        if depth == 0:
            end = i
            break
    else:
        raise SystemExit(f"make_gap: unbalanced object for {entry_id}")

    removed = "".join(lines[start : end + 1])
    return lines[:start] + lines[end + 1 :], removed


def cut_field(lines: list, section: str, entry_id: str, field: str) -> tuple:
    """Remove one field from the object whose `id:` field is entry_id."""
    hit = find_entry(lines, section, entry_id)
    if hit is None:
        return lines, None

    depth = 0
    start = hit
    while start >= 0 and not lines[start].strip().startswith("{"):
        start -= 1
    for i in range(start, len(lines)):
        depth += lines[i].count("{") - lines[i].count("}")
        if depth == 0:
            end = i
            break
    else:
        raise SystemExit(f"make_gap: unbalanced object for {entry_id}")

    field_at = next(
        (i for i in range(start, end + 1) if lines[i].strip().startswith(f"{field}:")), None
    )
    if field_at is None:
        return lines, None

    # A field value may wrap. Consume until quotes balance and the line ends
    # the assignment.
    last = field_at
    while last <= end:
        text = "".join(lines[field_at : last + 1])
        if text.count('"') % 2 == 0 and text.rstrip().endswith(","):
            break
        last += 1

    removed = "".join(lines[field_at : last + 1])
    return lines[:field_at] + lines[last + 1 :], removed


def cut_mount(lines: list, moment_id: str) -> tuple:
    """Remove the <Teach id="..."> mount line from a component."""
    needle = f'<Teach id="{moment_id}"'
    hit = next((i for i, l in enumerate(lines) if needle in l), None)
    if hit is None:
        return lines, None
    return lines[:hit] + lines[hit + 1 :], lines[hit]


def plant() -> dict:
    plan = json.loads((ROOT / "gaps" / "plan.json").read_text())
    restore()

    teaching = (GAME / TEACHING).read_text().splitlines(keepends=True)
    duel = (GAME / DUEL).read_text().splitlines(keepends=True)
    out = []

    for gap in plan["gaps"]:
        record = {
            "kind": gap["kind"],
            "id": gap["id"],
            "covers": gap["covers"],
            "correct_action": gap["correct_action"],
            "why": gap["why"],
            "removed": [],
        }

        section = SECTION.get(gap["kind"])
        if section is None:
            raise SystemExit(f"make_gap: unknown kind {gap['kind']}")
        if gap["kind"] == "mechanic-waiver":
            teaching, text = cut_field(teaching, section, gap["id"], "waiver")
        else:
            teaching, text = cut_object(teaching, section, gap["id"])

        if text is None:
            raise SystemExit(f"make_gap: nothing matched {gap['id']} in {TEACHING}")
        record["removed"].append({"file": TEACHING, "text": text})

        if gap.get("also_unmount"):
            duel, mount = cut_mount(duel, gap["also_unmount"])
            if mount is None:
                raise SystemExit(f"make_gap: no mount for {gap['also_unmount']} in {DUEL}")
            record["removed"].append({"file": DUEL, "text": mount})

        out.append(record)

    (GAME / TEACHING).write_text("".join(teaching))
    (GAME / DUEL).write_text("".join(duel))

    key = {
        "schema": "kp-gap-removed/1",
        "note": (
            "The answer key. gaps/ is off limits to every agent in the crew; "
            "tools/verify_blind.py fails the run if any agent read it. It is "
            "committed so a reader can check the agent's output against what "
            "was actually taken away."
        ),
        "source_plan": "gaps/plan.json",
        "gaps": out,
    }
    (ROOT / "gaps" / "removed.json").write_text(json.dumps(key, indent=2) + "\n")
    return key


def check() -> int:
    """Report which planted gaps are currently open in the slice."""
    plan = json.loads((ROOT / "gaps" / "plan.json").read_text())
    lines = (GAME / TEACHING).read_text().splitlines(keepends=True)
    duel = (GAME / DUEL).read_text()
    open_gaps = 0
    for gap in plan["gaps"]:
        section = SECTION[gap["kind"]]
        hit = find_entry(lines, section, gap["id"])
        if gap["kind"] == "mechanic-waiver":
            # The row itself always survives; the waiver field is what goes.
            present = hit is not None and cut_field(lines, section, gap["id"], "waiver")[1]
        else:
            present = hit is not None
        mount_ok = True
        if gap.get("also_unmount"):
            mount_ok = f'<Teach id="{gap["also_unmount"]}"' in duel
        state = "closed" if (present and mount_ok) else "OPEN"
        if state == "OPEN":
            open_gaps += 1
        print(f"  {state:6}  {gap['kind']:17} {gap['id']:14} covers {', '.join(gap['covers'])}")
    print(f"{open_gaps} of {len(plan['gaps'])} planted gaps are open")
    return open_gaps


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--restore":
        restore()
        print("restored game/ from gaps/pristine/")
        return 0
    if arg == "--check":
        check()
        return 0

    key = plant()
    print(f"planted {len(key['gaps'])} gaps into the vendored slice\n")
    for g in key["gaps"]:
        files = ", ".join(sorted({r["file"].split("/")[-1] for r in g["removed"]}))
        print(f"  removed {g['kind']:17} {g['id']:14} -> {', '.join(g['covers']):20} ({files})")
    print("\nanswer key: gaps/removed.json")
    print("now red:    bun game/src/game/dev/teach-sim.ts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
