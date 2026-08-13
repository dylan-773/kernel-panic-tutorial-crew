#!/usr/bin/env python3
"""Did any seat read the answer key?

Four of this repo's gaps were planted by tools/make_gap.py, and gaps/ records
exactly what was removed and what the right answer was. A run where a seat read
that is a run that demonstrated nothing.

This audits **the harness's own transcript**, not a self report. Claude Code
writes every tool call it makes to ~/.claude/projects/<mangled-cwd>/, with
subagent calls in a sidecar directory, so the record is written by the runtime
rather than by the agent being audited. An earlier version of this tool asked
each seat to append to a ledger; the first real run produced no ledger at all,
which is the failure mode you would expect from asking the subject to file its
own paperwork.

Two layers, and it is worth being exact about which is which.
`.claude/settings.json` denies `Read(gaps/**)`, so the permission layer refuses
the read outright: that is prevention. This is detection, and it covers shell
reads too, because a `cat gaps/removed.json` shows up in the recorded command
string.

    python3 tools/verify_blind.py runs/<RUN>
    python3 tools/verify_blind.py --list runs/<RUN>    show every path touched
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN = re.compile(r"(^|[\s'\"/=(])gaps/", re.I)

# Fields on a tool_use input that can carry a path or a command.
PATHY = ("file_path", "path", "pattern", "command", "notebook_path", "glob")


def transcript_dir() -> Path:
    """Claude Code mangles the cwd into a directory name under ~/.claude/projects."""
    return Path.home() / ".claude" / "projects" / str(ROOT).replace("/", "-")


def tool_calls(root: Path):
    """(agent, tool, text) for every recorded tool call, main session and subagents."""
    for f in sorted(root.rglob("*.jsonl")):
        agent = "orchestrator"
        meta = f.with_suffix(".meta.json")
        if meta.exists():
            try:
                m = json.loads(meta.read_text())
                agent = m.get("agentType") or m.get("name") or "subagent"
            except Exception:
                agent = "subagent"
        for line in f.read_text(errors="replace").splitlines():
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = d.get("message") or {}
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            for c in content:
                if not (isinstance(c, dict) and c.get("type") == "tool_use"):
                    continue
                inp = c.get("input") or {}
                text = " ".join(str(inp[k]) for k in PATHY if inp.get(k))
                yield agent, c.get("name", "?"), text


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = "--list" in sys.argv
    if not args:
        print("usage: verify_blind.py [--list] runs/<RUN>", file=sys.stderr)
        return 2

    tdir = transcript_dir()
    if not tdir.exists():
        print(f"BLIND FAIL: no transcript at {tdir}; the run cannot show what it read")
        return 1

    by_agent, violations, total = {}, [], 0
    for agent, tool, text in tool_calls(tdir):
        total += 1
        stats = by_agent.setdefault(agent, {"calls": 0, "tools": set()})
        stats["calls"] += 1
        stats["tools"].add(tool)
        if text and FORBIDDEN.search(text):
            violations.append((agent, tool, text[:120]))
        if show and text:
            print(f"  {agent:16} {tool:8} {text[:96]}")

    print(f"transcript: {tdir.name}")
    print(f"{total} recorded tool calls across {len(by_agent)} actors\n")
    for agent, s in sorted(by_agent.items()):
        print(f"  {agent:18} {s['calls']:4} calls  ({', '.join(sorted(s['tools']))})")

    # A seat that ran but touched nothing is as suspicious as one that read the key.
    seats = [a for a in by_agent if a not in ("orchestrator", "subagent")]
    idle = [a for a in seats if by_agent[a]["calls"] < 3]

    if violations:
        print(f"\nBLIND FAIL: {len(violations)} reference(s) to gaps/")
        for agent, tool, text in violations:
            print(f"  {agent} via {tool}: {text}")
        return 1
    if idle:
        print(f"\nBLIND FAIL: seat(s) with almost no recorded activity: {idle}")
        return 1

    print(f"\nBLIND OK: {len(seats)} seat(s) ran, none referenced gaps/")
    print("audited from the runtime's transcript, not from a self report")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
