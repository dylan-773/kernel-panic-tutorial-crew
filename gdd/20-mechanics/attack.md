---
title: ATTACK
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[redirect]]", "[[arm-halt]]", "[[arm-siphon]]"]
---

# ATTACK

> [!info] Source
> `kit.ts:ATTACK_WIDTH`, `attackModeDesc`.

The only program that reaches the **enemy** board. 1 RAM, once per turn.

Width by tier: 1, 2, 3 targets per cast. See [[program-tiers]].

## Modes

| Mode | Unlocked by | What it does |
|---|---|---|
| [[redirect]] | default | Twists their junctions, no reach limit |
| [[arm-halt]] | [[halt-driver]] | Plants turn-forfeit traps |
| [[arm-siphon]] | [[siphon-driver]] | Plants RAM-stealing traps |

REDIRECT is the default and needs no augment. The other two are config unlocks.

## Targeting

ATTACK always resolves against `boards[otherSide]`. The action carries no board tag; `targetBoardOf` derives it from the verb. See [[split-boards]].

> [!warning] A REDIRECT settles the enemy board
> Which means a badly chosen twist can **complete their route and hand them the dive**. The verb is not risk-free.

## Economy

- `econ.attacksCast` counts casts this dive, which is what [[cheap-shot]] reads to make the first one free.
- Program twists do not count against [[route-cost-and-par|par]].
- `lastPlayerHitRound` records when you last landed an arm, redirect or lock.

## See also

- [[the-kit]] · [[traps-and-telegraphs]]
