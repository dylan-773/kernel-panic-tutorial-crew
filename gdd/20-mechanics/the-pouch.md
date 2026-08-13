---
title: The pouch
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[patch-pieces]]", "[[player-inventory]]", "[[solder-bay]]"]
---

# The pouch

> [!info] Source
> `patch-cells.ts:PATCH_POUCH_MAX`; `duel-types.ts:DuelKit.patchPouch`, `DuelState.patchPouch`.

Where [[patch-pieces]] are carried. `PATCH_POUCH_MAX = 5`.

The pouch is a list of 4-bit arm masks, not a count. Which shapes you hold matters as much as how many, because a piece cannot be rotated to fit.

## Conservation

`run-sim.ts` asserts across 40 full runs that **a dive never mints pieces**: the pouch after a dive equals leftovers plus banked drops exactly, the cap is respected, and every mask is a legal shape.

That invariant exists because the pouch crosses the duel and run reducers in both directions, which is precisely where a resource leak would hide.

## Interaction with drafting

`{ kind: "pouch" }` is the requirement gate on [[splice-refund]]: the pouch must hold at least one piece **at roll time**. It is the only non-augment requirement in the catalog. See [[augments]].

## See also

- [[player-inventory]] · [[solder-bay]] · [[the-darknet]]
