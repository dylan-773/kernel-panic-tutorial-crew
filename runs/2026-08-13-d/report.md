# Run 2026-08-13-d

## Before, verbatim from the harness

```
TEACH FAIL: 5 problem(s)
  - mechanic "cascade" (Cascade banking) has no teaching moment and no waiver. First contact: duel.
  - mechanic "kitConfig" (Swapping program modes) has no teaching moment and no waiver. First contact: loadout.
  - mechanic "ram" (RAM per turn as the action budget) has no teaching moment and no waiver. First contact: tutorial.
  - mechanic "ramCarry" (Unspent RAM carries into the next turn, capped) has no teaching moment and no waiver. First contact: duel.
  - mechanic "reach2" (Rotating within two steps of your territory) has no teaching moment and no waiver. First contact: tutorial.
```

make_gap.py --check reported 4 of 4 planted gaps open. The GDD reader kept 64
player facing features out of 131 candidates. The prioritizer returned 11 gaps,
not four: the five red mechanic ids collapse into four gaps (ram and ramCarry
share one tip), plus seven found by cross checking the reader's drift notes and
uninventoried candidates against the code.

## The gap table

| rank | gap | tier | action | strongest cited signal |
|---|---|---|---|---|
| 1 | ram-budget (ram, ramCarry) | 1 | tip | harness-red; also first-contact-day (tutorial, day 0) and resource-cost |
| 2 | reach2 | 0 | waiver | harness-red; ladder-tier (the board's dv-legal glow already renders the boundary) |
| 3 | cascade | 2 | coachmark | harness-red; surface-budget (duel had 2 of 4 moments used) and resource-cost |
| 4 | kitConfig | 1 | tip | harness-red; first-contact-day (loadout, no clock, lowest urgency of the red four) |
| 5 | patchCellUse-cost | 2 | coachmark correction | resource-cost (shipped copy says 2 RAM, patch-cells.ts:PLACE_COST is 4) |
| 6 | oneUndo | 1 | tip | resource-cost (takeUndo keeps a sprung trap's drain) |
| 7 | builtVsPower | 0 | waiver | ladder-tier (dv-cut already renders built-but-dark) |
| 8 | splitBoards | 0 | waiver | ladder-tier (cross board manipulation impossible by construction) |
| 9 | winConditions | 0 | waiver | ladder-tier (each ending already states itself where it happens) |
| 10 | theKit | none | declined | ladder-tier (no rung fits without authoring a new MANUAL.TXT section) |
| 11 | gridlockChip | none | declined | harness-red note: waived and green, but the waiver claims an overlay DuelEndKind cannot render |

## What was built

Applied to game/ through apply_patch.py, diffs in runs/2026-08-13-d/diff/:

- Tier 1 tip "ram" (covers ram and ramCarry). Wired the already existing but
  empty tip("ram") call site in duel.tsx. Numbers cite run-reducer.ts:BASE_RAM
  (5), run-reducer.ts:MAX_RAM (9), duel-setup.ts:carryCap (2).
- Tier 0 waiver for reach2. The dv-legal glow on unbuilt junctions is gated by
  duel-power.ts:inReach; built junctions are always legal per
  duel-power.ts:canRotate; ATTACK and DEFEND targeting is governed separately
  by attackTargetLegal and defendTargetLegal. Rescoped after a critic REVISE.
- Tier 2 coachmark "cascade-bank" at the cascadeBanked moment, order 45.
  Thresholds cite kit.ts:cascadeRam (pays from three, correcting the vault's
  known drift note that said four) and kit.ts:surgeTierOf (six, ten).
- Tier 1 tip "modeLocked" (covers kitConfig). Wired the already existing but
  empty tip("modeLocked") call site in loadout.tsx.
- Tier 2 coachmark "patch-cell-use-cost" at order 79, stating 4 RAM per
  patch-cells.ts:PLACE_COST, with a label edit deleting the shipped
  <Teach id="patch-cell-use"> mount whose copy reads "for 2 RAM", so only the
  correct panel can ever reach a player. Restructured after a critic REVISE.

## Deliberately not built

- theKit and gridlockChip: declined by the prioritizer (see gap table).
- oneUndo, builtVsPower, splitBoards, winConditions: authored, then deferred to
  runs/2026-08-13-d/deferred/ with WHY.md. They are uninventoried mechanics,
  and the toolchain has no path for a generated file to introduce a new
  MECHANIC_INVENTORY id and reference it in the same pass: verify_teaching.py
  checks ids against a scan of the unmodified game/, and apply_patch.py runs
  add_waiver() before any label edit could insert the row. Closing them needs a
  tooling change or seeded inventory rows, neither of which is a seat action.
  None of the four is red in the harness.

## Critic verdicts

Round 1: three APPROVE (ram-budget, cascade, kitConfig), two REVISE.

- REVISE 02-reach2: the waiver overclaimed that dv-legal applies only to cells
  inReach returns true for, quoting duel-power.ts "if (!isJunction(c0) ||
  c0.built) return false;" against canRotate's "if (c.built) return true;".
- REVISE 05-patchCellUse-cost: the corrected coachmark at order 79 raced the
  still live wrong one at order 80; both fire on holdingCells, so the player
  would see the right panel, dismiss it, then see the wrong one.

Round 2 after revision: both flipped to APPROVE. Final tally 5 APPROVE,
0 REVISE outstanding. The critic noted one edge it chose not to escalate:
canRotate also excludes fused and enemy locked unbuilt junctions before the
inReach call, judged immaterial next to the fixed structural overclaims.

The strongest critic finding was the patch-cell-use race: a correction that
mounts a second, correct coachmark next to the still live wrong one does not
retire the wrong number, it puts both in front of the player back to back.

## Checks

- verify_teaching.py: 5 items, all well formed (order and surface budgets clean)
- verify_copy.py: 5 files clean, 10 claims resolved against real symbols
- verify_copy.py --kind verdict: 5 verdict files clean
- verify_blind.py: BLIND OK, 4 seats ran, none referenced gaps/, audited from
  the runtime transcript (1035 recorded tool calls across 5 actors)

## After, verbatim from the harness

```
OK: 39 mechanics, 25 taught, 14 waived, 10 coachmarks, 7 tips, 10 tutorial beats
OK: surfaces reached by the run walk: analyze, day, dayOpen, duel, finalePre, finaleWin, opener, result, runEnd, tutIntro, tutOutro, tutorial, upgrade
OK: teaching coverage complete
```
