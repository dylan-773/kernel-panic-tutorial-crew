---
title: MANUAL.TXT
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[teaching-tips]]", "[[augments]]", "[[the-kit]]"]
---

# MANUAL.TXT

`manual` · `windows/manual.tsx`

The reference. Five tabs, page-flip navigation: **DIVE · KIT · PATCHES · AUGMENTS · BAYS**.

## Generated, not written

Every page is **generated from the live `kit.ts` descriptions**. `attackModeDesc`, `defendModeDesc` and `scanDesc` are functions of tier, and the augment cards read `AugmentDef.desc`.

> [!info] This is why the manual cannot go stale
> A manual maintained by hand drifts from the game within one balance pass. A manual that reads the same constants the reducers read cannot.
>
> `teach-sim.ts` enforces the other half: two teaching waivers (`augmentEffects`, `modeEffects`) are backed by a `waiverPremise` asserting that every augment and every mode still ships its own desc. If a desc is ever removed, the waiver expires and the build fails.

## Its role in teaching

The manual is the **tier 3** answer in the [[placement-bias-order]]: reference the player can go and get, as opposed to a coachmark that comes to them.

A `manualRef` tip exists to point at it. The rule for the split: **a tip is reference you want again, a coachmark is a rule you need once**. See [[teaching-tips]].

## Panel note

The **18-card AUGMENTS page is the hard case**: eighteen cards with names and descriptions, inside a 700px ceiling, with no scrollbar allowed. Paging is the only available answer. See [[law-8-the-cuts-discipline]] and [[law-11-panel-queue]].

## See also

- [[augments]] · [[the-kit]] · [[mechanic-coverage]]
