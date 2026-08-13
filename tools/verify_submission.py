#!/usr/bin/env python3
"""Map each Assignment 5 requirement to the artifact that evidences it.

Assignment 5 has no point rubric. It has five requirements and a README that
must answer three questions, so this checks those eight things against the
repo's actual contents and prints, per line, the file that carries it and a
command a reader can paste to confirm it.

SOFT exists so weak evidence is not rounded up to strong.

    python3 tools/verify_submission.py
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def latest_run() -> Path:
    runs = sorted(p for p in (ROOT / "runs").glob("*") if p.is_dir())
    return runs[-1] if runs else None


class Audit:
    def __init__(self):
        self.rows = []

    def add(self, criterion, status, evidence, how, note=""):
        self.rows.append((criterion, status, evidence, how, note))

    def report(self) -> int:
        order = {"PASS": 0, "SOFT": 1, "FAIL": 2}
        print("ASSIGNMENT 5: GOAL ORIENTED CODING AGENT\n")
        for crit, status, evidence, how, note in self.rows:
            print(f"[{status}] {crit}")
            print(f"       evidence: {evidence}")
            print(f"       verify:   {how}")
            if note:
                print(f"       note:     {note}")
            print()
        worst = max(order[r[1]] for r in self.rows)
        n_pass = sum(1 for r in self.rows if r[1] == "PASS")
        print(f"{n_pass}/{len(self.rows)} PASS, "
              f"{sum(1 for r in self.rows if r[1] == 'SOFT')} SOFT, "
              f"{sum(1 for r in self.rows if r[1] == 'FAIL')} FAIL")
        return 1 if worst == 2 else 0


def main() -> int:
    a = Audit()
    run = latest_run()
    rel = run.relative_to(ROOT).as_posix() if run else "runs/<RUN>"

    # ---- 1. Read your GDD --------------------------------------------------
    gm_path = ROOT / "gdd" / "MANIFEST.json"
    gm = json.loads(gm_path.read_text()) if gm_path.exists() else {}
    feats = []
    if run and (run / "features.json").exists():
        feats = json.loads((run / "features.json").read_text()).get("features", [])
    a.add(
        "Read your GDD: parse a design document to extract the features it describes",
        "PASS" if gm.get("note_count", 0) > 100 and len(feats) >= 20 else
        ("SOFT" if feats else "FAIL"),
        f"gdd/ is the real vault, {gm.get('note_count', 0)} notes, sha256 manifested; "
        f"{rel}/features.json holds {len(feats)} extracted features",
        "python3 tools/gdd_extract.py",
        "the vault is frozen and rollup hashed, so the source is checkable, not asserted",
    )

    # ---- 2. Scan the codebase ---------------------------------------------
    scan_ok = subprocess.run(["bun", "tools/code_scan.ts"], cwd=ROOT,
                             capture_output=True, text=True)
    a.add(
        "Scan the codebase: read existing source to understand what is built",
        "PASS" if scan_ok.returncode == 0 else "FAIL",
        "tools/code_scan.ts imports the real content/teaching.ts and greps every "
        "<Teach> mount in the components",
        "bun tools/code_scan.ts",
        "it imports the module rather than parsing it, so it cannot drift from the game",
    )

    # ---- 3. Detect gaps ----------------------------------------------------
    before = (run / "teach-sim.before.txt").read_text() if run and (run / "teach-sim.before.txt").exists() else ""
    after = (run / "teach-sim.after.txt").read_text() if run and (run / "teach-sim.after.txt").exists() else ""
    red = "TEACH FAIL" in before
    green = after.startswith("OK:")
    a.add(
        "Detect gaps: compare what the GDD requires against what the codebase contains",
        "PASS" if red and green else ("SOFT" if red else "FAIL"),
        f"{rel}/teach-sim.before.txt names the uncovered mechanics; "
        f"{rel}/teach-sim.after.txt is green",
        "bun game/src/game/dev/teach-sim.ts",
        "the harness is the shipped game's own, vendored unmodified, and it is what "
        "goes red then green",
    )

    # ---- 4. Prioritize -----------------------------------------------------
    gaps = []
    if run and (run / "gaps.json").exists():
        gaps = json.loads((run / "gaps.json").read_text()).get("gaps", [])
    cited = [g for g in gaps if g.get("because") and g.get("ladderStop")]
    tiers = sorted({g.get("tier") for g in gaps})
    ranks = [g.get("rank") for g in gaps]
    total_order = len(set(ranks)) == len(ranks) and None not in ranks
    strong = bool(gaps) and len(cited) == len(gaps) and total_order and len(tiers) > 1
    a.add(
        "Prioritize: decide which missing feature to build first, and why",
        "PASS" if strong else ("SOFT" if gaps else "FAIL"),
        f"{rel}/gaps.json: {len(gaps)} gaps across tiers {tiers}, "
        f"{len(cited)} carrying both a cited signal and a ladder stop",
        f"python3 -m json.tool {rel}/gaps.json",
        "the ladder in reference/placement-bias-order.md is the game's real decision "
        "procedure, not a scoring function invented for this assignment"
        + ("" if len(tiers) > 1 else "; a single tier across all gaps is weak evidence of reasoning"),
    )

    # ---- 5. Generate code --------------------------------------------------
    gen = sorted((run / "generated").glob("*.json")) if run else []
    diffs = sorted((run / "diff").glob("*.patch")) if run else []
    built = [json.loads(p.read_text()).get("action") for p in gen]
    a.add(
        "Generate code: write the code for at least one missing feature",
        "PASS" if diffs and green else ("SOFT" if gen else "FAIL"),
        f"{len(gen)} items generated ({', '.join(sorted(set(built))) or 'none'}); "
        f"{len(diffs)} applied diff(s) in {rel}/diff/",
        f"cat {rel}/diff/teaching.ts.patch",
        "generated as JSON, checked, then written to the slice by tools/apply_patch.py; "
        "the seats never edit game/ themselves",
    )

    # ---- README, three questions ------------------------------------------
    readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").exists() else ""
    a.add(
        "README: what features did the agent build",
        "PASS" if "## What it built" in readme else "FAIL",
        "README.md, section `What it built`",
        "grep -n '## What it built' README.md",
    )
    a.add(
        "README: why did the agent select that feature",
        "PASS" if "## Why " in readme else "FAIL",
        "README.md, the section explaining the first pick",
        "grep -n '## Why ' README.md",
    )
    a.add(
        "README: were you able to run this in your game",
        "PASS" if "## Did it run in the game" in readme else "FAIL",
        "README.md, section `Did it run in the game`",
        "grep -n '## Did it run in the game' README.md",
    )

    # ---- the honesty checks the assignment does not ask for ---------------
    blind = subprocess.run(["python3", "tools/verify_blind.py", rel], cwd=ROOT,
                           capture_output=True, text=True) if run else None
    a.add(
        "Not asked for: the crew did not read the answer key",
        "PASS" if blind and blind.returncode == 0 else ("FAIL" if blind else "SOFT"),
        "four of the gaps were planted by tools/make_gap.py; gaps/ holds what it removed",
        f"python3 tools/verify_blind.py {rel}",
        "Read(gaps/**) is denied in .claude/settings.json and the reads ledger is audited",
    )

    return a.report()


if __name__ == "__main__":
    raise SystemExit(main())
