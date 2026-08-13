#!/usr/bin/env python3
"""Freeze the vendored GDD and game slice.

Writes gdd/MANIFEST.json and game/MANIFEST.json (sha256 per file, plus a
rollup), and copies the two mutable game files into gaps/pristine/ so the
gap planter can always start from a byte-exact original.

A file is FROZEN unless the pipeline is allowed to edit it. Only two are
mutable: the teaching data module and the one component the coachmark mounts
in. Everything else, including the harness that judges the run and the code
the copy is checked against, must stay byte-identical to upstream. That is
what stops a green build from being bought by editing the checker.

Run once at vendor time. selftest.py verifies against what it wrote.
"""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The two files the pipeline is allowed to change.
MUTABLE = [
    "src/game/content/teaching.ts",
    "src/components/game/duel.tsx",
]

UPSTREAM = "kernel-panic/kernel-panic-site/app/src"
UPSTREAM_VAULT = "kernel-panic/vault (Obsidian design vault)"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rollup(files: dict) -> str:
    h = hashlib.sha256()
    for name in sorted(files):
        h.update(name.encode())
        h.update(files[name]["sha256"].encode())
    return h.hexdigest()


def freeze_gdd(frozen_on: str) -> int:
    gdd = ROOT / "gdd"
    files = {}
    for p in sorted(gdd.rglob("*.md")):
        rel = p.relative_to(gdd).as_posix()
        files[rel] = {"bytes": p.stat().st_size, "sha256": sha256(p)}
    manifest = {
        "schema": "kp-gdd-manifest/1",
        "source": UPSTREAM_VAULT,
        "frozen": frozen_on,
        "note_count": len(files),
        "gdd_sha256": rollup(files),
        "files": files,
    }
    (gdd / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return len(files)


def freeze_game(frozen_on: str) -> tuple:
    game = ROOT / "game"
    pristine = ROOT / "gaps" / "pristine"
    pristine.mkdir(parents=True, exist_ok=True)
    files = {}
    for p in sorted(game.rglob("*")):
        if not p.is_file() or p.name == "MANIFEST.json":
            continue
        rel = p.relative_to(game).as_posix()
        mutable = rel in MUTABLE
        files[rel] = {
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
            "frozen": not mutable,
        }
        if mutable:
            dest = pristine / Path(rel).name
            dest.write_bytes(p.read_bytes())
    manifest = {
        "schema": "kp-game-manifest/1",
        "source": UPSTREAM,
        "frozen": frozen_on,
        "file_count": len(files),
        "frozen_count": sum(1 for f in files.values() if f["frozen"]),
        "mutable": MUTABLE,
        "game_sha256": rollup(files),
        "files": files,
    }
    (game / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return len(files), manifest["frozen_count"]


def gaps_are_open() -> bool:
    """Is the slice currently carrying planted gaps?

    Freezing then would copy the gapped files into gaps/pristine/ and make the
    "before" state the new upstream, quietly destroying the only copy of the
    real one. Worth a guard: it is a one command mistake with no error message
    of its own, and the next make_gap run just reports that it matched nothing.
    """
    plan_file = ROOT / "gaps" / "plan.json"
    teaching = ROOT / "game" / MUTABLE[0]
    if not plan_file.exists() or not teaching.exists():
        return False
    body = teaching.read_text()
    plan = json.loads(plan_file.read_text())
    for gap in plan["gaps"]:
        if f'id: "{gap["id"]}",' not in body:
            return True
    return False


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: freeze.py <YYYY-MM-DD> [--force]", file=sys.stderr)
        return 2
    on = sys.argv[1]

    if gaps_are_open() and "--force" not in sys.argv:
        print(
            "freeze: the slice is currently gapped, so freezing would record the\n"
            "        BEFORE state as pristine and lose the real upstream.\n"
            "        Restore first:  python3 tools/make_gap.py --restore\n"
            "        Or re-vendor from the game repo, then freeze again.",
            file=sys.stderr,
        )
        return 1
    notes = freeze_gdd(on)
    total, frozen = freeze_game(on)
    print(f"gdd/MANIFEST.json      {notes} notes")
    print(f"game/MANIFEST.json     {total} files, {frozen} frozen, {total - frozen} mutable")
    print(f"gaps/pristine/         {len(MUTABLE)} originals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
