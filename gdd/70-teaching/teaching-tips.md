---
title: Teaching tips
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[coachmarks]]", "[[placement-bias-order]]", "[[manual-txt]]"]
---

# Teaching tips

> [!info] Source
> `content/teaching.ts:TEACH_TIPS`. Seven.

Persistent hover explainers. **A tip is reference you want again.**

| id | Explains |
|---|---|
| `par` | the rotation budget |
| `strain` | the run's health bar |
| `ram` | the per-turn budget |
| `manualRef` | that [[manual-txt]] exists |
| `threatTier` | job tier 1 to 5 |
| `boostSlots` | [[boost-bays]] |
| `modeLocked` | why a mode button is unavailable |

## The split rule

> **A tip is reference you want again, a coachmark is a rule you need once.**

Three things get **both**: [[route-cost-and-par|par]], [[neural-strain|strain]] and threat tier. Each has a rule to learn once and a number to look up repeatedly. That is not redundancy, it is the two halves of a mechanic being taught by the two mechanisms that suit them.

## `modeLocked` is doing tier-0 work

A locked mode button explains its own unavailability on hover. Without it, a player who has not drafted [[clamp-driver]] sees a dead button and learns nothing.

It is a tip rather than a coachmark because the answer changes: which mode is locked depends on which [[augments|configs]] you own, so there is no single moment at which the rule is learned once and for all.

## `ram` carries a known gap

The tip states that a rotation or a cast costs 1, which is correct, and **says nothing about `PLACE_COST`**, which is 4. Placement is the most expensive action in a turn and the persistent explainer for the resource does not mention it. See [[mechanic-coverage]].

## See also

- [[coachmarks]] · [[manual-txt]]
