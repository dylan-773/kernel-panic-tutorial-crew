---
title: The night shop
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[economy]]", "[[program-tiers]]", "[[night-sys]]"]
---

# The night shop

> [!info] Source
> `run-reducer.ts:chooseUpgrade`, `closeNight`, `buyPatch`, `buySlot`, `buyDarkPatch`, `craftPatch`; `NIGHT_PICKS`.

Day close. One free pick, plus anything you can afford.

## The pick

`NIGHT_PICKS = ["ram", "scan", "attack", "defend"]`

- **ram** - +1 RAM per turn, cap 9.
- **scan / attack / defend** - +1 [[program-tiers|tier]] on that program, cap 3.

One per night, free.

## The shop

| Purchase | Cost | Effect |
|---|---|---|
| Night patch | `45 + 5 * day` | +12 [[neural-strain]] |
| [[boost-bays|Boost bay]] | 150, then 300 | 4th and 5th bay |
| [[the-darknet|Dark pull]] | `25 + 5 * (day - 1)` | one blind [[patch-pieces|piece]] |
| Weld | free | two pieces become their union |

Also free: +10 strain, applied automatically at day close.

## The night is two-step and reversible

`chooseUpgrade` sets `nightPick` **without ending the night**. `closeNight` commits, and refuses without a pick.

So the shop rows stay spendable after you have chosen your upgrade, and you can change the pick while you shop. This matters because the pick and the purchases trade against each other: taking a RAM tier changes whether you can afford the bay.

`run-sim.ts` asserts both halves: `closeNight` refused without a pick, and choosing does not end the night.

## Fiction

Night Patch is a strain suppressant, and the bible is clear it treats the symptom. Buying your way through the arc on patches is exactly what [[dad]] did. See [[ground-truth]].

## Teaching

Two coachmarks, both on first sight of the upgrade surface: `day-upgrade` (order 70) and `night-shop` (71), the latter covering patches, dark pulls and bays together. See [[coachmarks]].

## See also

- [[night-sys]] - the window this happens in
- [[economy]]
