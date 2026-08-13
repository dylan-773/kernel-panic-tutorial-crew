#!/usr/bin/env python3
"""The regression suite for the two verifiers.

A checker nobody has tried to fool is a claim, not a check. Every breaking case
asserts three things: the exit code, that the expected message is present, and
that the clean cases stay silent. A linter that flags everything proves nothing,
so `clean` and `shipped-cascade` must both pass.

Each case runs in its own invocation. verify_teaching deliberately accumulates
`order` and per-surface budget across the files in one run, because in a real
run all the generated items land together and two items picking the same order
IS a collision. That is right for a run and wrong for a fixture, so fixtures
never share an invocation.

    python3 tools/run_fixtures.py
    python3 tools/run_fixtures.py -v
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN = "fixtures/scan.json"

# (fixture, tool, expected exit, substrings that must appear)
CASES = [
    # ---- verify_teaching: shape and the harness invariants -----------------
    ("teaching/clean.json", "teaching", 0, []),
    ("teaching/dash.json", "teaching", 1, ["em or en dash"]),
    ("teaching/order-collision.json", "teaching", 1, ["order 40 is already taken"]),
    ("teaching/three-lines.json", "teaching", 1, ["3 lines", "Teach one thing"]),
    ("teaching/lower-title.json", "teaching", 1, ["not ALL CAPS"]),
    ("teaching/bad-when.json", "teaching", 1, ["is not a TeachWhen"]),
    ("teaching/bad-anchor.json", "teaching", 1, ["no kp-teach-corner rule"]),
    ("teaching/unknown-mechanic.json", "teaching", 1, ["not in MECHANIC_INVENTORY"]),
    ("teaching/long-line.json", "teaching", 1, ["the cap is 160"]),
    ("teaching/no-mount.json", "teaching", 1, ["renders nothing"]),
    ("teaching/fake-anchor-line.json", "teaching", 1, ["not a literal line"]),
    ("teaching/no-claims.json", "teaching", 1, ["missing `claims`"]),
    ("teaching/surface-cap.json", "teaching", 1, ["unconditional callouts; the cap is 2"]),
    ("teaching/unknown-class.json", "teaching", 1, ["has no rule in styles.css"]),
    # ---- verify_copy: is the copy accountable ------------------------------
    ("copy/clean.json", "copy", 0, ["cascadeRam", "if (lit < 3) return 0;"]),
    ("copy/uncited-number.json", "copy", 1, ['states "4" but no claim covers it']),
    ("copy/bad-symbol.json", "copy", 1, ["has no declaration of cascadePayout"]),
    # The shipped defect. It is MECHANICALLY CLEAN on purpose: the number is
    # claimed and the symbol resolves. What the tool guarantees is that the
    # contradicting source lands next to the claim, where a critic cannot miss
    # it. That guarantee is what this case asserts.
    ("copy/shipped-cascade.json", "copy", 0,
     ['copy says:  "four or more nodes"', "if (lit < 3) return 0;"]),
    # ---- verify_copy --kind verdict: can a verdict substantiate itself -----
    ("verdict/good.json", "verdict", 0, []),
    ("verdict/bad-quote.json", "verdict", 1, ["not a literal substring"]),
    ("verdict/revise-no-objection.json", "verdict", 1, ["is a complaint, not a verdict"]),
    ("verdict/no-quote.json", "verdict", 1, ["has no quote"]),
]

CMD = {
    "teaching": lambda f: ["python3", "tools/verify_teaching.py", "--scan", SCAN, f],
    "copy": lambda f: ["python3", "tools/verify_copy.py", f],
    "verdict": lambda f: ["python3", "tools/verify_copy.py", "--kind", "verdict", f],
}


def main() -> int:
    verbose = "-v" in sys.argv
    passed, failed = 0, []

    for fixture, tool, want_code, want_text in CASES:
        path = f"fixtures/{fixture}"
        if not (ROOT / path).exists():
            failed.append((fixture, f"fixture missing: {path}"))
            continue
        run = subprocess.run(CMD[tool](path), cwd=ROOT, capture_output=True, text=True)
        out = run.stdout + run.stderr

        problems = []
        if run.returncode != want_code:
            problems.append(f"exit {run.returncode}, expected {want_code}")
        for want in want_text:
            if want not in out:
                problems.append(f"missing from output: {want!r}")

        if problems:
            failed.append((fixture, "; ".join(problems)))
            if verbose:
                print(f"--- {fixture} ---\n{out}")
        else:
            passed += 1
            if verbose:
                print(f"ok {fixture}")

    print(f"\n{passed}/{len(CASES)} fixture cases pass")
    if failed:
        print("\nfailures:")
        for name, why in failed:
            print(f"  {name}: {why}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
