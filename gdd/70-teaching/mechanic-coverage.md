---
title: Mechanic coverage
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[teaching-waivers]]", "[[teaching-system]]", "[[verification-gate]]"]
---

# Mechanic coverage

> [!info] Source
> `content/teaching.ts:MECHANIC_INVENTORY`; `tutorial/ledger.md` Coverage table (43 rows, including retired and planned).
>
> Verified against `teach-sim.ts` output on 2026-08-05: **39 mechanics, 25 taught, 14 waived, 9 coachmarks, 7 tips, 10 tutorial beats.**

The inventory of everything a player must understand, and how each one is covered.

```ts
{ id, label, firstContact, waiver?, waiverPremise? }
```

## The four statuses

| Status | Means |
|---|---|
| **TAUGHT** | a beat, coachmark or tip resolves it |
| **WAIVED** | deliberately not taught, with a written reason. See [[teaching-waivers]] |
| **PLANNED** | acknowledged, not yet covered |
| **RETIRED** | no longer a player-facing mechanic |

## The mechanic ids

The real primary key of the teaching system, cited from the coverage table, the waiver log, the gate files and the copy orders:

`rotate` · `flood` · `scan` · `defend` · `attack` · `telegraph` · `cascade` · `par` · `ram` · `ramCarry` · `patchCellUse` · `patchShapes` · `patchCraft` · `strainChip` · `jobBoard` · `manualRef` · `analyzeTell` · `threatTier` · `kitConfig` · `programTiers` · `augmentDraft` · `augmentCadence` · `boostSlots` · `boostSwap` · `dayUpgrade` · `nightPatch` · `patchCellBuy` · `darkWebBuy` · `slotBuy` · `reach2` · `turnCap` · `patchDrop` · `gridlockChip` · `credits` · `saveSlots` · `runReset` · `finaleGate` · `finaleOppOpens` · `augmentEffects` · `modeEffects` · `journalRunGate`

Retired: `augmentPoolDry`. Considered and not added: `pieceDragCarry`.

## The enforcement

`teach-sim.ts` fails the build unless **every** inventory entry resolves to a moment, beat, tip or written waiver. Its output:

```
OK: 39 mechanics, 25 taught, 14 waived, 9 coachmarks, 7 tips, 10 tutorial beats
```

then the surfaces the run walk reached, then `OK: teaching coverage complete`. On failure it prints an itemized `TEACH FAIL` list naming the gap and exits 1.

It also verifies **reachability**: every moment's surface must be reached by an actual walk through a run. `WINDOW_SURFACES` are exempt as reachable by construction.

## Two ids that should not be here any more

`flood` and `gridlockChip` both describe the pre-[[split-boards]] duel. There is no flood-claim and no gridlock outcome. They are stale inventory entries against a deleted model. See [[territory-and-claiming]].

## Three known copy defects

| Where | Says | Actually |
|---|---|---|
| `patch-cell-use` | placement costs 2 RAM | `PLACE_COST = 4` |
| `cascade-bank` | pays at four nodes | `cascadeRam` pays from three |
| `ram` tip | rotation or cast costs 1 | true, but silent on `PLACE_COST` |

Coverage is complete; three of the covering strings are wrong. **`teach-sim.ts` checks that a mechanic is covered, not that the copy is accurate.** That is the gap the tutorial gate's manual read exists to fill.

## See also

- [[teaching-waivers]] · [[standing-lessons]]
