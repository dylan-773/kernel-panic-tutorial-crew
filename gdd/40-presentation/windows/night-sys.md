---
title: NIGHT.SYS
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-night-shop]]", "[[shopfront-exe]]", "[[darknet-lnk]]"]
---

# NIGHT.SYS

The `upgrade` screen of [[shopfront-exe]] · `windows/night.tsx`

Day close. The night pick and the shop.

## What it carries

- One free pick from `NIGHT_PICKS`: **+1 RAM** or **+1 [[program-tiers|tier]]** on one program.
- The shop: night patch, [[boost-bays|boost bay]], [[the-darknet|dark pull]], weld.
- The automatic **+10 [[neural-strain|strain]]** for closing the day.

Full economics in [[the-night-shop]].

## Two-step and reversible

`chooseUpgrade` sets the pick **without ending the night**; `closeNight` commits and refuses without a pick.

> [!info] Why the interface has to work this way
> The pick and the purchases trade against each other. Taking a RAM tier changes whether you can afford the bay. If choosing ended the night, the player would be committing to the expensive half of the decision before seeing the cheap half.
>
> `run-sim.ts` asserts both halves: `closeNight` refused without a pick, and choosing does not end the night.

## Teaching

Two coachmarks fire here on first sight:

| Order | id | Teaches |
|---|---|---|
| 70 | `day-upgrade` | the free pick |
| 71 | `night-shop` | `nightPatch`, `darkWebBuy`, `slotBuy` together |

Three purchases under one callout is unusual. It is allowed because they are one decision: what to do with tonight's credits. See [[coachmarks]].

## Panel note

Small surface, and a candidate for **proving the system at low density**. Most of the v3 laws are about managing too much; this panel tests whether they survive having little. See [[law-11-panel-queue]].

## See also

- [[the-night-shop]] · [[economy]]
