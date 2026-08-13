---
title: Coachmarks
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[teaching-system]]", "[[teaching-tips]]", "[[placement-bias-order]]"]
---

# Coachmarks

> [!info] Source
> `content/teaching.ts:TEACHING`.

One-time callouts. **A coachmark is a rule you need once.**

| Order | id | Surface | Fires on | Teaches |
|---|---|---|---|---|
| 20 | `analyze-readout` | [[inbox\|analyze]] | firstSight | `analyzeTell`, `threatTier` |
| 40 | `par-budget` | [[dive-exe\|duel]] | **overPar** | `par` |
| 50 | `cascade-bank` | duel | **cascadeBanked** | `cascade` |
| 60 | `strain-chip` | [[repair-log\|result]] | firstSight | `strainChip` |
| 61 | `augment-draft` | result | **draftOffered** | `augmentDraft`, `augmentCadence` |
| 62 | `boost-swap` | result | **swapOffered** | `boostSwap` |
| 70 | `day-upgrade` | [[night-sys\|upgrade]] | firstSight | `dayUpgrade` |
| 71 | `night-shop` | upgrade | firstSight | `nightPatch`, `darkWebBuy`, `slotBuy` |
| 80 | `patch-cell-use` | duel | **holdingCells** | patch placement |

All carry `notBeforeDay: 1`, so none can fire in the opening dive.

## Order is precedence, and it is total

Lower shows first, and **only one callout renders at a time**. `teach-sim.ts` requires uniqueness, so there is never a tie.

Read down the table and it is a reading order for the whole game: understand the diagnostic (20) before the duel's economy (40, 50), before the bill (60), before progression (61, 62), before the shop (70, 71).

## Conditional beats first-sight

Six of the nine fire on a **condition** rather than on seeing a screen: over par, a banked cascade, holding pieces, a draft offered, a swap offered.

> [!info] This is the "just in time, never front-loaded" rule
> `par-budget` fires the first time you **exceed** par, which is the first moment par means anything. Explaining it on the first dive, before it has cost anything, is front-loading.

## Retired

`patch-craft` was **retired 2026-07-29**: [[solder-bay]] was rebuilt so illegal weld partners are physically dead, which made the callout redundant. Tier 0 beat tier 2. See [[placement-bias-order]].

`solder-bay-intro` was proposed and **rejected** for the same reason.

## Limits

`MAX_COACH_LINE = 160` chars. `MAX_FIRST_SIGHT_PER_SURFACE = 2`, `MAX_MOMENTS_PER_SURFACE = 4`. The result surface sits at exactly 3 moments and 1 first-sight, and upgrade at 2 first-sight, which is the cap.

## See also

- [[teaching-tips]] · [[mechanic-coverage]]
