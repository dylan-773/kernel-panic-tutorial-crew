#!/usr/bin/env python3
"""Write the generated teaching code into the vendored slice.

The seats produce JSON; this turns it into TypeScript and TSX and puts it where
the harness will judge it. Keeping generation and application apart is what
lets `verify_teaching.py` and `verify_copy.py` run BEFORE anything touches the
slice, and it keeps the seats out of the game files entirely.

Moments are inserted in `order` position rather than appended, because the
registry reads as a precedence list and appending would slowly destroy that.

    python3 tools/apply_patch.py runs/<RUN>
    python3 tools/apply_patch.py --dry-run runs/<RUN>
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
TEACHING_TS = GAME / "src/game/content/teaching.ts"


def ts_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def ts_list(items) -> str:
    return "[" + ", ".join(ts_str(i) for i in items) + "]"


def render_moment(m: dict) -> str:
    out = ["  {"]
    out.append(f'    id: {ts_str(m["id"])},')
    out.append(f'    teaches: {ts_list(m["teaches"])},')
    out.append(f'    surface: {ts_str(m["surface"])},')
    out.append(f'    when: {ts_str(m["when"])},')
    out.append(f'    anchor: {ts_str(m["anchor"])},')
    out.append(f'    order: {m["order"]},')
    out.append(f'    notBeforeDay: {m["notBeforeDay"]},')
    out.append(f'    title: {ts_str(m["title"])},')
    out.append("    lines: [")
    for line in m["lines"]:
        out.append(f"      {ts_str(line)},")
    out.append("    ],")
    out.append("  },")
    return "\n".join(out) + "\n"


def render_tip(t: dict) -> str:
    return (
        "  {\n"
        f'    id: {ts_str(t["id"])},\n'
        f'    teaches: {ts_list(t["teaches"])},\n'
        f'    control: {ts_str(t["control"])},\n'
        f'    text: {ts_str(t["text"])},\n'
        "  },\n"
    )


def section(lines: list, name: str) -> tuple:
    start = next(i for i, l in enumerate(lines) if l.startswith(f"export const {name}"))
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("];"))
    return start + 1, end


def insert_moment(lines: list, moment: dict) -> list:
    lo, hi = section(lines, "TEACHING")
    order_at = re.compile(r"^\s*order:\s*(\d+),")
    at = hi
    for i in range(lo, hi):
        m = order_at.match(lines[i])
        if m and int(m.group(1)) > moment["order"]:
            # Rewind to the `{` that opens this entry.
            j = i
            while j >= lo and lines[j].strip() != "{":
                j -= 1
            at = j
            break
    return lines[:at] + [render_moment(moment)] + lines[at:]


def insert_tip(lines: list, tip: dict) -> list:
    lo, hi = section(lines, "TEACH_TIPS")
    return lines[:hi] + [render_tip(tip)] + lines[hi:]


def add_waiver(lines: list, mech_id: str, text: str) -> list:
    """Attach a waiver to a MechanicEntry, expanding a one-line row if needed."""
    lo, hi = section(lines, "MECHANIC_INVENTORY")
    pat = re.compile(r'(^|\{\s*)id:\s*"' + re.escape(mech_id) + r'"\s*,')
    hit = next((i for i in range(lo, hi) if pat.search(lines[i].strip())), None)
    if hit is None:
        raise SystemExit(f"apply_patch: no inventory row for {mech_id}")

    stripped = lines[hit].strip()
    if stripped.startswith("{") and stripped.endswith("},"):
        # One-line row: re-render it multi-line so the waiver has somewhere to go.
        fields = stripped[1:-2].strip().rstrip(",")
        parts = [p.strip() for p in re.split(r",(?![^\[]*\])", fields) if p.strip()]
        block = ["  {\n"] + [f"    {p},\n" for p in parts]
        block.append(f"    waiver: {ts_str(text)},\n")
        block.append("  },\n")
        return lines[:hit] + block + lines[hit + 1 :]

    # Multi-line row: insert before its closing brace.
    depth = 0
    start = hit
    while start >= lo and not lines[start].strip().startswith("{"):
        start -= 1
    for i in range(start, hi + 1):
        depth += lines[i].count("{") - lines[i].count("}")
        if depth == 0:
            close = i
            break
    return lines[:close] + [f"    waiver: {ts_str(text)},\n"] + lines[close:]


def insert_mount(path: Path, anchor: str, jsx: str) -> bool:
    lines = path.read_text().splitlines(keepends=True)
    at = next((i for i, l in enumerate(lines) if l.rstrip("\n") == anchor.rstrip("\n")), None)
    if at is None:
        at = next((i for i, l in enumerate(lines) if anchor.strip() and anchor.strip() in l), None)
    if at is None:
        return False
    path.write_text("".join(lines[: at + 1] + [jsx.rstrip("\n") + "\n"] + lines[at + 1 :]))
    return True


def replace_label(path: Path, before: str, after: str) -> bool:
    body = path.read_text()
    if before not in body:
        return False
    path.write_text(body.replace(before, after, 1))
    return True


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print("usage: apply_patch.py [--dry-run] runs/<RUN>", file=sys.stderr)
        return 2
    run = Path(args[0])
    if not run.is_absolute():
        run = ROOT / run

    gen_dir = run / "generated"
    items = sorted(gen_dir.glob("*.json"))
    if not items:
        print(f"apply_patch: no generated items in {gen_dir}", file=sys.stderr)
        return 2

    diff_dir = run / "diff"
    diff_dir.mkdir(parents=True, exist_ok=True)
    touched = {TEACHING_TS}
    backup = {}
    for p in [TEACHING_TS, GAME / "src/components/game/duel.tsx"]:
        backup[p] = p.read_text()

    lines = TEACHING_TS.read_text().splitlines(keepends=True)
    applied = []

    for path in items:
        item = json.loads(path.read_text())
        action = item["action"]

        if action == "coachmark":
            lines = insert_moment(lines, item["moment"])
            applied.append(f'moment  {item["moment"]["id"]:16} order {item["moment"]["order"]}')
        elif action == "tip":
            lines = insert_tip(lines, item["tip"])
            applied.append(f'tip     {item["tip"]["id"]:16} teaches {", ".join(item["tip"]["teaches"])}')
        elif action == "none":
            applied.append(f'none    {item["gap"]:16} nothing built, by decision')
            continue

        if item.get("waiver"):
            lines = add_waiver(lines, item["waiver"]["id"], item["waiver"]["text"])
            applied.append(f'waiver  {item["waiver"]["id"]:16} {item["waiver"]["text"][:44]}...')

    TEACHING_TS.write_text("".join(lines))

    # Component edits happen after the data module is settled so a failure
    # there cannot leave half a moment behind.
    for path in items:
        item = json.loads(path.read_text())
        if item.get("mount"):
            target = GAME / item["mount"]["file"]
            touched.add(target)
            if not insert_mount(target, item["mount"]["anchorLine"], item["mount"]["jsx"]):
                print(f'apply_patch: could not place the mount for {item["gap"]}', file=sys.stderr)
                for p, text in backup.items():
                    p.write_text(text)
                return 1
            applied.append(f'mount   {item["mount"]["file"].split("/")[-1]:16} after the anchor line')
        if item.get("label"):
            target = GAME / item["label"]["file"]
            touched.add(target)
            if not replace_label(target, item["label"]["before"], item["label"]["after"]):
                print(f'apply_patch: label `before` not found for {item["gap"]}', file=sys.stderr)
                for p, text in backup.items():
                    p.write_text(text)
                return 1
            applied.append(f'label   {item["label"]["file"].split("/")[-1]:16} '
                           f'{item["label"]["before"][:24]} -> {item["label"]["after"][:24]}')

    if dry:
        for p, text in backup.items():
            p.write_text(text)
        print("dry run, slice restored\n")

    for line in applied:
        print(f"  {line}")

    if not dry:
        for p in sorted(touched):
            rel = p.relative_to(GAME).as_posix()
            pristine = ROOT / "gaps" / "pristine" / Path(rel).name
            if pristine.exists():
                d = subprocess.run(
                    ["diff", "-u", str(pristine), str(p)], capture_output=True, text=True
                )
                (diff_dir / (Path(rel).name + ".patch")).write_text(d.stdout)
        try:
            shown = diff_dir.relative_to(ROOT)
        except ValueError:
            shown = diff_dir
        print(f"\ndiffs against upstream: {shown}/")
        print("now check:  bun game/src/game/dev/teach-sim.ts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
