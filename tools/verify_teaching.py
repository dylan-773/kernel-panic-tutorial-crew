#!/usr/bin/env python3
"""Shape and constraint check on generated teaching items.

Every rule here is one the shipped harness enforces, restated so a violation is
caught before the code is written into the slice rather than after. The limits
are read out of `bun tools/code_scan.ts --json`, never retyped, so this file
cannot drift from the game.

This asks "is it well formed". It does not ask "is it true"; that is
verify_copy.py and the copy-critic.

    python3 tools/verify_teaching.py runs/<RUN>/generated/*.json
    python3 tools/verify_teaching.py --scan <cached.json> <files...>
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASHES = ("—", "–")
ACTIONS = ("coachmark", "tip", "label", "waiver", "none")
# Anything that puts words in front of a player has to say where its numbers
# came from. `none` writes nothing, so it is the only action without claims.
NEEDS_CLAIMS = ("coachmark", "tip", "label", "waiver")


def load_scan(cached: str = "") -> dict:
    if cached:
        return json.loads(Path(cached).read_text())
    out = subprocess.run(
        ["bun", "tools/code_scan.ts", "--json"], cwd=ROOT, capture_output=True, text=True
    )
    if out.returncode != 0:
        raise SystemExit(f"verify_teaching: code_scan failed\n{out.stderr}")
    return json.loads(out.stdout)


class Check:
    def __init__(self, label: str):
        self.label = label
        self.fails: list = []

    def __call__(self, ok, msg: str):
        if not ok:
            self.fails.append(msg)
        return bool(ok)


CLASSNAME = re.compile(r'className="([^"{}]+)"')


def no_dash(c: Check, where: str, text: str) -> None:
    for d in DASHES:
        c(d not in text, f"{where} contains an em or en dash; game copy never does")


def known_classes(c: Check, where: str, jsx: str) -> None:
    """Every className in generated JSX must already exist in styles.css.

    styles.css is frozen, so a seat cannot style anything it invents. A new
    class name is therefore not a small liberty, it is an element that renders
    with no styling at all, and nothing else in the pipeline would notice:
    teach-sim never looks at CSS, and the anchor check below only covers
    `kp-teach-<anchor>`.

    Caught the first time by a generated `dv-ram-carry` badge that shipped
    unstyled. Reuse an existing class, or the element is not buildable here.
    """
    css = (ROOT / "game" / "src" / "styles.css").read_text()
    for group in CLASSNAME.findall(jsx):
        for name in group.split():
            if not name or name.startswith("kp-teach-"):
                continue
            c(f".{name}" in css,
              f'{where} uses className "{name}", which has no rule in styles.css. '
              f"styles.css is frozen, so reuse an existing class")


def check_moment(c: Check, m: dict, scan: dict, taken_orders: set) -> None:
    lim = scan["limits"]
    ids = {e["id"] for e in scan["inventory"]}

    for field in ("id", "teaches", "surface", "when", "anchor", "order", "notBeforeDay", "title", "lines"):
        c(field in m, f"moment is missing required field `{field}`")
    if c.fails:
        return

    c(bool(m["teaches"]), "moment teaches nothing")
    for t in m["teaches"]:
        c(t in ids, f'moment teaches unknown mechanic "{t}"; it is not in MECHANIC_INVENTORY')

    c(m["surface"] in lim["surfaces"], f'surface "{m["surface"]}" is not a TeachSurface')
    c(m["when"] in lim["whens"],
      f'when "{m["when"]}" is not a TeachWhen. A new trigger is a reducer change, not a string')
    c(m["anchor"] in lim["anchors"],
      f'anchor "{m["anchor"]}" has no kp-teach-{m["anchor"]} rule in styles.css')

    c(m["order"] not in taken_orders,
      f'order {m["order"]} is already taken; precedence must be total')
    taken_orders.add(m["order"])

    c(0 <= m["notBeforeDay"] <= lim["finalDay"],
      f'notBeforeDay {m["notBeforeDay"]} is outside 0..{lim["finalDay"]}')

    title = m["title"]
    c(bool(title), "moment title is empty")
    c(title == title.upper(), f'title "{title}" is not ALL CAPS; system text always is')
    no_dash(c, "title", title)

    lines = m["lines"]
    c(isinstance(lines, list) and 1 <= len(lines) <= lim["maxLines"],
      f"moment has {len(lines) if isinstance(lines, list) else '?'} lines; the cap is {lim['maxLines']}. Teach one thing")
    for i, line in enumerate(lines or []):
        c(len(line) <= lim["maxCoachLine"],
          f"line {i + 1} is {len(line)} characters; the cap is {lim['maxCoachLine']}")
        no_dash(c, f"line {i + 1}", line)


def check_budget(c: Check, item: dict, scan: dict, added: dict) -> None:
    """Per-surface caps, counting what this run is about to add."""
    m = item.get("moment")
    if not m or "surface" not in m:
        return
    s = m["surface"]
    cur = scan["budget"]["surfaces"].get(s, {"moments": 0, "firstSight": 0})
    total = cur["moments"] + added.setdefault(s, {"moments": 0, "firstSight": 0})["moments"] + 1
    first = cur["firstSight"] + added[s]["firstSight"] + (1 if m.get("when") == "firstSight" else 0)
    added[s]["moments"] += 1
    if m.get("when") == "firstSight":
        added[s]["firstSight"] += 1

    c(total <= scan["budget"]["maxMomentsPerSurface"],
      f'surface "{s}" would hold {total} moments; the cap is {scan["budget"]["maxMomentsPerSurface"]}')
    c(first <= scan["budget"]["maxFirstSightPerSurface"],
      f'surface "{s}" would fire {first} unconditional callouts; the cap is '
      f'{scan["budget"]["maxFirstSightPerSurface"]}. Make one conditional or fold them together')


def check_item(path: Path, scan: dict, taken_orders: set, added: dict) -> Check:
    c = Check(path.name)
    try:
        item = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        c(False, f"not valid JSON: {e}")
        return c

    c(item.get("schema") == "kp-generated/1", "schema must be kp-generated/1")
    c(bool(item.get("gap")), "missing `gap`")
    action = item.get("action")
    c(action in ACTIONS, f"action must be one of {', '.join(ACTIONS)}")
    if action not in ACTIONS:
        return c

    ids = {e["id"] for e in scan["inventory"]}
    lim = scan["limits"]

    if action == "coachmark":
        if c("moment" in item, "action coachmark needs a `moment`"):
            check_moment(c, item["moment"], scan, taken_orders)
            check_budget(c, item, scan, added)
        if c("mount" in item, "action coachmark needs a `mount`; a moment with no mount renders nothing"):
            mount = item["mount"]
            for f in ("file", "anchorLine", "jsx"):
                c(f in mount, f"mount is missing `{f}`")
            if "jsx" in mount and "moment" in item:
                c(f'id="{item["moment"].get("id")}"' in mount["jsx"],
                  "mount jsx does not carry the moment id")

    elif action == "tip":
        if c("tip" in item, "action tip needs a `tip`"):
            t = item["tip"]
            for f in ("id", "teaches", "control", "text"):
                c(f in t, f"tip is missing `{f}`")
            c(bool(t.get("teaches")), "tip teaches nothing")
            for m in t.get("teaches", []):
                c(m in ids, f'tip teaches unknown mechanic "{m}"')
            c(bool(t.get("control")), "tip has no control; a tooltip has to hang on something")
            text = t.get("text", "")
            c(1 <= len(text) <= lim["maxTipLen"],
              f"tip text is {len(text)} characters; the cap is {lim['maxTipLen']}")
            no_dash(c, "tip text", text)

    elif action == "waiver":
        if c("waiver" in item, "action waiver needs a `waiver`"):
            w = item["waiver"]
            c(w.get("id") in ids, f'waiver names unknown mechanic "{w.get("id")}"')
            c(len(w.get("text", "")) >= 20,
              "waiver text is under 20 characters; the harness treats that as no waiver at all")
            c(bool(w.get("expiresIf")),
              "waiver has no expiresIf; a waiver that cannot expire is a claim nobody will recheck")
            no_dash(c, "waiver text", w.get("text", ""))

    elif action == "label":
        if c("label" in item, "action label needs a `label`"):
            lb = item["label"]
            for f in ("file", "before", "after", "why"):
                c(f in lb, f"label is missing `{f}`")
            if "file" in lb:
                target = ROOT / "game" / lb["file"]
                if c(target.exists(), f'label file {lb["file"]} does not exist'):
                    c(lb.get("before", "\x00") in target.read_text(),
                      "label `before` is not a literal string in the target file")
            no_dash(c, "label after", lb.get("after", ""))
            known_classes(c, "label after", lb.get("after", ""))
        c("waiver" in item,
          "a tier 0 label retires the need for teaching, so the inventory row has to carry a waiver saying so")
        if "waiver" in item:
            w = item["waiver"]
            c(w.get("id") in ids, f'waiver names unknown mechanic "{w.get("id")}"')
            c(len(w.get("text", "")) >= 20, "waiver text is under 20 characters")

    elif action == "none":
        c(bool(item.get("why")), "action none needs a `why`; declining to build is a decision, not a silence")

    # Any item may carry a `mount`, not just a coachmark: a tip that needs a
    # control to hang on has to add one. apply_patch.py applies every mount it
    # finds, so every mount gets checked here regardless of action.
    if item.get("mount"):
        mount = item["mount"]
        if "jsx" in mount:
            known_classes(c, "mount jsx", mount["jsx"])
        if "file" in mount:
            target = ROOT / "game" / mount["file"]
            if c(target.exists(), f'mount file {mount["file"]} does not exist'):
                c(mount.get("anchorLine", "") in target.read_text(),
                  "mount anchorLine is not a literal line in the target file")

    if action in NEEDS_CLAIMS:
        claims = item.get("claims")
        c(isinstance(claims, list), "missing `claims`; every generated line names the symbol behind its numbers")
        for i, cl in enumerate(claims or []):
            for f in ("text", "symbol", "resolves"):
                c(f in cl, f"claim {i + 1} is missing `{f}`")
    return c


def main() -> int:
    args = sys.argv[1:]
    cached = ""
    if "--scan" in args:
        i = args.index("--scan")
        cached = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if not args:
        print("usage: verify_teaching.py [--scan cached.json] <generated/*.json>", file=sys.stderr)
        return 2

    scan = load_scan(cached)
    taken = set(scan["orders"]["used"])
    added: dict = {}
    results = []
    for a in args:
        results.append(check_item(Path(a), scan, taken, added))

    bad = [r for r in results if r.fails]
    for r in results:
        if r.fails:
            print(f"FAIL {r.label}")
            for f in r.fails:
                print(f"  - {f}")
        else:
            print(f"ok   {r.label}")
    print()
    if bad:
        print(f"verify_teaching: {sum(len(r.fails) for r in bad)} problem(s) in {len(bad)} of {len(results)} items")
        return 1
    print(f"verify_teaching: {len(results)} items, all well formed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
