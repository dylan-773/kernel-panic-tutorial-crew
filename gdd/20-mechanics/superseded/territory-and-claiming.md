---
title: Territory and claiming
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[split-boards]]", "[[design-change-log]]", "[[win-conditions]]"]
---

# Territory and claiming (superseded)

> [!warning] This describes a model that no longer exists
> Removed 2026-08-04 on branch `split-boards`. It is recorded here because three documents still asserted it after the engine deleted it, and because the reasons it failed are worth keeping. For the current model see [[split-boards]].
>
> `main` still ships this. The deployed game and the documented game differ until `split-boards` lands.

## What it was

**One shared grid.** Both sides flooded it from opposite entries. Lighting a chain **claimed** it, and claimed territory was **impassable to the enemy signal**. Claims were permanent.

Consequences that followed:

- Defence meant **occupation**. You held ground to deny approaches.
- The board was a contested space, so position mattered as much as speed.
- Two extra loss conditions existed: **SEVERED** (walled off from the core with no route left) and **gridlock** (mutual stall).
- `MAX_OPENING_CLAIM` was the generation bound, now `MAX_OPENING_BUILT`.

## Why it went

**Holding ground is not an interesting decision.** Once you had a defensible shape, the correct play was to keep it, and keeping it is not a move. The back half of a duel stopped being a race and became a positional stalemate. The intended feel was a sprint with sabotage; what it produced was a slow squeeze.

There was also a defect class attached to it. The route planner could report `Infinity` for a route that actually existed (see the `approx` discussion in [[route-cost-and-par]]). Under SEVERED, a planner blindspot did not merely mislead the AI, it **ended a still-winnable dive in an instant loss**. Deleting the loss condition deleted the bug's landing site.

## What replaced each piece

| Old | New |
|---|---|
| one shared grid | two grids, `DuelState.boards[side]` |
| claiming, permanent and exclusive | `built`, permanent but non-exclusive: the enemy is never on your board |
| impassability as defence | anti-trap and anti-redirect as defence |
| SEVERED, gridlock | removed; only `goal`, `cap`, `seal` remain |
| holding ground | [[cascades-and-surge]] and interference tempo |

See [[built-and-power]] for the two-layer model that carries the load claiming used to.

## What still references the old model

As of 2026-08-05, and outside this vault:

- `lore/bible.md` technology rules: "Claimed territory is impassable to the enemy signal."
- `tutorial/ledger.md`: coverage rows for `flood`, and `MAX_OPENING_CLAIM`.
- `gdd/Kernel_Panic_GDD_v2.html`: the whole Duel section.
- `run-reducer.ts` and `save.ts`: `gridlockWin`, vestigial.
- `teaching.ts`: the `gridlockChip` waiver.

The vault's [[60-story]] notes were corrected during migration. The originals were not edited.

## See also

- [[design-change-log]] - entry 10
- [[split-boards]] - the current model
