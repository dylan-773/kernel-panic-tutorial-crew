---
title: Patch pieces
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-pouch]]", "[[solder-bay]]", "[[reach-and-placement]]"]
---

# Patch pieces

> [!info] Source
> `patch-cells.ts:PLACE_COST`, `CRAFT_COST`, `PATCH_ROLL_WEIGHTS`, `armUnionCraft`, `darkPatchCost`.

Single-use shaped fills. A piece is a **4-bit arm mask with its orientation baked in**: it is never rotatable, in hand or on the board.

```
PLACE_COST            = 4 RAM     (one per turn)
CRAFT_COST            = 0 credits
PATCH_POUCH_MAX       = 5
PATCH_DROP_TIER_BONUS = 0.05 per tier above 1
PATCH_ROLL_WEIGHTS    = I 40 / L 45 / T 12 / X 3
darkPatchCost(day)    = 25 + 5 * (day - 1)
```

> [!danger] REVISED IN PROTOTYPE
> Patch pieces took the slot vacated when Neural Capacity was cut. A consumable that changes the board reads more clearly than a second abstract meter.
>
> `PLACE_COST` was raised from 2 to 4 for [[split-boards]]: on a board only you occupy, a cheap bridge trivialized routing.

## What placing one does

Fills a **slag** cell within [[reach-and-placement|reach]] of built ground. The cell becomes `fused`:

- nothing rotates it, for anyone, ever;
- [[redirect]] cannot touch it;
- `repairCostOf` returns 0.

So a piece is both a bridge across slag and a permanent anchor the enemy cannot twist. Placements do not count against [[route-cost-and-par|par]].

## Getting them

1. **Job drops.** Chance per cleared ticket is `DAY_CONFIGS[day].patchDrop + 0.05 * (tier - 1)`. Drop rates fall across the arc, from 0.35 on day 1 to 0.11 on day 9, while slag rises. Scarcity increases exactly as need does.
2. **[[the-darknet|Dark pulls]].** Blind, priced by day.
3. **[[clean-run]].** A zero-strain win banks one.
4. **Crafting.** See below.

## Crafting: the weld

`armUnionCraft(a, b)` is a bitwise **union** of two masks, legal only when the result is **strictly bigger than both inputs**.

So an I welded to a perpendicular L makes a T. An I welded to a parallel I is illegal, because the union equals an input. The shop copy states the rule directly:

> PICK A PARTNER. THE WELD MUST OUTGROW BOTH.

Crafting is free in credits and costs two pieces to make one. It converts quantity into shape. See [[solder-bay]], where illegal partners are rendered physically dead rather than merely rejected.

## Drift

The `patch-cell-use` coachmark still says placing costs **2 RAM**. `PLACE_COST` is 4. Recorded in [[20-mechanics]].

## See also

- [[the-pouch]] · [[splice-refund]]
