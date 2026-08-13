---
title: SOLDER.BAY
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[patch-pieces]]", "[[the-pouch]]", "[[game-controls]]"]
---

# SOLDER.BAY

`solder` · `windows/solder.tsx`

The patch-piece bench. Crafting lives here and nowhere else.

## What it does

- A **rack of held [[patch-pieces|pieces]]**, up to 5.
- **Drag-to-weld** union crafting.
- **Illegal partners are physically dead and disabled.**

## The rule it has to teach without words

`armUnionCraft(a, b)` is a bitwise union, legal only when the result is **strictly bigger than both inputs**. An I welded to a perpendicular L makes a T; an I welded to a parallel I is illegal.

The shop copy states it directly:

> PICK A PARTNER. THE WELD MUST OUTGROW BOTH.

## Why illegal partners are dead rather than refusing

> [!info] This is tier 0 teaching
> A drag that is accepted and then rejected teaches by failure. A partner that visibly cannot be dragged onto teaches the rule before the attempt.
>
> The [[placement-bias-order|placement bias order]] puts "make the UI say it" above every kind of callout, and this window is the clearest example in the game. The `patch-craft` coachmark was **retired on 2026-07-29** because the interface had made it redundant.

See [[teaching-system]].

## Panel note

Interaction-heavy, so the **motion budget matters most here**. Drag feedback is continuous, and [[law-7-motion]] restricts animation to compositor properties. See [[law-11-panel-queue]].

## See also

- [[patch-pieces]] · [[the-darknet]] · [[the-night-shop]]
