---
name: close-gaps
description: Read the frozen Kernel Panic design vault, scan the game's teaching layer, find the mechanics the GDD describes that nothing teaches, decide what to build and in what order, generate the code, gate it on whether the copy is true, apply it, and prove the game's own harness goes from red to green.
disable-model-invocation: true
---

# /close-gaps

You are the ORCHESTRATOR of the tutorial crew. You spawn the four seats, carry
each one's output into the next, run the checks between them, and apply the
result to the vendored slice.

**You do not author teaching content yourself.** If you find yourself choosing
an `order`, writing a coachmark line, or deciding a gap is tier 1, you have
taken a seat's job. If a seat returns something unusable, re-spawn it with the
problem quoted.

**You do not read `gaps/`.** It holds the answer key for the planted gaps. The
crew's whole claim is that it rediscovered them from the GDD and the code.

Invocation: `/close-gaps [run-id]`

- `run-id` optional, defaults to `<YYYY-MM-DD>-<letter>`, next free letter.

Examples: `/close-gaps` · `/close-gaps 2026-08-13-a`

---

## 0. Preflight

```
python3 tools/run_fixtures.py          # 21/21
python3 tools/make_gap.py --check      # how many gaps are open
```

If fixtures fail, **stop and report.** The checkers are what make the run
mean anything and a run on broken checkers proves nothing.

If `--check` reports 0 open gaps, the slice is at upstream. Plant them:

```
python3 tools/make_gap.py
```

Never close a gap by editing `game/` yourself, and never fix a red check by
loosening the check.

## 1. Capture the before state

```
mkdir -p runs/<RUN>/{generated,critic,diff}
bun game/src/game/dev/teach-sim.ts > runs/<RUN>/teach-sim.before.txt 2>&1 || true
bun tools/code_scan.ts > runs/<RUN>/code-scan.before.txt
```

**A non-zero exit here is the point, not a build failure to route around.** The
harness naming five uncovered mechanics is the before state. Read the file
yourself; you will need the exact names for the report.

## 2. Brief

Write `runs/<RUN>/BRIEF.md`: the run id, the harness's before output, the count
of open gaps, and one line on what the run is for. Keep it under twenty lines.

## 3. GDD Reader

Spawn `gdd-reader`. Tell it the `<RUN>` id and nothing about what is missing.

When it returns:

```
python3 -c "import json;d=json.load(open('runs/<RUN>/features.json'));print(len(d['features']),'features')"
```

A features file with fewer than 20 entries or with every candidate marked
player facing is a failed read: re-spawn once, naming what it skipped.

## 4. Gap Prioritizer

Spawn `gap-prioritizer`. **Quote the uncovered mechanic ids from
`teach-sim.before.txt` into the prompt, and the feature count.** The handoff is
explicit, not implied.

When it returns, read `runs/<RUN>/gaps.json` yourself and check three things:

- every gap has a non-empty `ladderStop` that names a ladder question
- every gap's `because` cites at least one of the five signals by name
- `rank` is total, with no ties

Any of those missing is a failed prioritization, which is the one thing this
crew cannot ship without. Re-spawn once, naming the gaps that failed.

**If every gap came back as a coachmark, say so in the re-spawn.** Four
coachmarks out of four is the pattern matching failure the seat is warned
about.

## 5. Teaching Author

Spawn `teaching-author`. **Quote the ranked gap list with each gap's `action`
and `tier`.**

## 6. Check the drafts

```
python3 tools/verify_teaching.py runs/<RUN>/generated/*.json
python3 tools/verify_copy.py --report runs/<RUN>/copy-report.json runs/<RUN>/generated/*.json
```

Both must exit 0 before the critic sees anything. Re-spawn the author with the
exact error text, once. Still failing, stop and report.

Note that `verify_teaching` accumulates `order` and surface budgets across the
files, on purpose: two items picking the same order is a real collision.

## 7. Copy Critic

Spawn `copy-critic`. Point it at `runs/<RUN>/copy-report.json`.

When it returns:

```
python3 tools/verify_copy.py --kind verdict runs/<RUN>/critic/*.json
```

A verdict that cannot substantiate its quote fails here. **A critic that has to
downgrade an objection has produced a correct outcome, not an error.**

Read the verdicts yourself. Fewer verdict files than generated items is a
failed review: re-spawn once, naming what it skipped.

## 8. Revision round. One round only.

If any verdict is REVISE, re-spawn `teaching-author` with the objection and the
`required` line quoted, and re-run step 6 and the critic on the changed items
only.

**One round.** An item still carrying a REVISE after round 2 ships with the
objection recorded in the report. Never quietly drop a verdict.

## 9. Apply

```
python3 tools/apply_patch.py runs/<RUN>
```

This is the only step that writes `game/`. It writes the diffs into
`runs/<RUN>/diff/`. Never hand edit the slice to make the next step pass.

## 10. The after state

```
bun game/src/game/dev/teach-sim.ts > runs/<RUN>/teach-sim.after.txt 2>&1
bun tools/code_scan.ts > runs/<RUN>/code-scan.after.txt
```

The harness must exit 0. If it does not, read the failure: it is either a real
constraint the drafts violated (re-spawn the author) or the patch landed
somewhere wrong (fix `apply_patch.py`, restore with
`python3 tools/make_gap.py`, and re-apply). **Do not edit `game/` by hand to
make it green.** A green build bought that way is the one thing this repo
exists to make impossible.

## 11. Blindness audit

```
python3 tools/verify_blind.py runs/<RUN>
```

This audits the runtime's own transcript of every tool call this session made,
main loop and subagents alike, so there is no ledger for a seat to forget.
Any reference to `gaps/` invalidates the run, and so does a seat that ran
without touching anything. If this fails, report it as a failure; do not
quietly re-run.

## 12. Build the page and report

```
python3 tools/build_demo.py runs/<RUN>
```

Then write `runs/<RUN>/report.md`: the before output, the gap table with tier
and rank and the cited signal per gap, what was built per gap, the critic's
verdicts, and the after output.

Print, and stop:

- the before line and the after line, both verbatim from the harness
- what was built, by tier, including anything deliberately not built
- the strongest critic finding
- the literal command to open the page: `open out/before-after.html`

Write nothing outside `runs/`, `out/` and `game/`, and write `game/` only
through `tools/apply_patch.py`.
