#!/usr/bin/env python3
"""Is this repo still what it says it is?

Seven checks. The first three are the ones that matter: they prove the GDD is
the real vault byte for byte, and that nothing has quietly edited the harness
that judges the run or the code the copy is checked against.

That last point is the whole reason the manifest marks files frozen. A green
build is worth nothing if the way it went green was someone changing
`cascadeRam` to match the copy instead of changing the copy to match
`cascadeRam`.

Writes nothing. Standard library only.

    python3 tools/selftest.py
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Suite:
    def __init__(self):
        self.rows = []

    def check(self, name: str, ok: bool, detail: str = "") -> bool:
        self.rows.append((name, ok, detail))
        return ok

    def report(self) -> int:
        width = max(len(r[0]) for r in self.rows)
        for name, ok, detail in self.rows:
            print(f"  {'ok  ' if ok else 'FAIL'}  {name.ljust(width)}  {detail}")
        bad = sum(1 for _, ok, _ in self.rows if not ok)
        print(f"\n{len(self.rows) - bad}/{len(self.rows)} checks pass")
        return 1 if bad else 0


def main() -> int:
    s = Suite()

    # 1. the GDD is the frozen vault, byte for byte
    gm = json.loads((ROOT / "gdd" / "MANIFEST.json").read_text())
    drift = [
        rel for rel, meta in gm["files"].items()
        if not (ROOT / "gdd" / rel).exists() or sha256(ROOT / "gdd" / rel) != meta["sha256"]
    ]
    s.check("gdd matches its manifest", not drift,
            f"{gm['note_count']} notes" + (f", {len(drift)} drifted: {drift[:3]}" if drift else ""))

    # 2. nothing has touched the frozen half of the game slice
    xm = json.loads((ROOT / "game" / "MANIFEST.json").read_text())
    frozen = {r: m for r, m in xm["files"].items() if m["frozen"]}
    moved = [
        rel for rel, meta in frozen.items()
        if not (ROOT / "game" / rel).exists() or sha256(ROOT / "game" / rel) != meta["sha256"]
    ]
    s.check("frozen game files unchanged", not moved,
            f"{len(frozen)} frozen" + (f", CHANGED: {moved}" if moved else ""))

    # 3. the pristine originals are the upstream ones
    bad_pristine = []
    for rel in xm["mutable"]:
        p = ROOT / "gaps" / "pristine" / Path(rel).name
        if not p.exists() or sha256(p) != xm["files"][rel]["sha256"]:
            bad_pristine.append(rel)
    s.check("pristine originals intact", not bad_pristine,
            f"{len(xm['mutable'])} files" + (f", bad: {bad_pristine}" if bad_pristine else ""))

    # 4. the harness runs at all
    r = subprocess.run(["bun", "game/src/game/dev/teach-sim.ts"], cwd=ROOT,
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    s.check("teach-sim runs", bool(out) and ("OK:" in out[0] or "TEACH FAIL" in out[0]),
            out[0][:64] if out else "no output")

    # 5. the scanner runs and agrees with the harness about coverage
    r = subprocess.run(["bun", "tools/code_scan.ts", "--json"], cwd=ROOT,
                       capture_output=True, text=True)
    scan_ok = r.returncode == 0
    n_unc = 0
    if scan_ok:
        scan = json.loads(r.stdout)
        n_unc = scan["counts"]["uncovered"]
        harness_red = out and "TEACH FAIL" in out[0]
        scan_ok = bool(n_unc) == bool(harness_red)
    s.check("code_scan agrees with the harness", scan_ok, f"{n_unc} uncovered")

    # 6. the checkers still catch what they claim to
    r = subprocess.run(["python3", "tools/run_fixtures.py"], cwd=ROOT,
                       capture_output=True, text=True)
    line = next((l for l in r.stdout.splitlines() if "fixture cases pass" in l), "")
    s.check("fixtures pass", r.returncode == 0, line.strip())

    # 7. every tool at least starts
    tools = sorted(p.name for p in (ROOT / "tools").glob("*.py"))
    broken = []
    for t in tools:
        r = subprocess.run(["python3", "-c", f"import ast,sys;ast.parse(open('tools/{t}').read())"],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            broken.append(t)
    s.check("tools parse", not broken, f"{len(tools)} tools" + (f", broken: {broken}" if broken else ""))

    print("selftest\n")
    return s.report()


if __name__ == "__main__":
    raise SystemExit(main())
