---
title: LOCK
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[defend]]", "[[rotation]]", "[[cascades-and-surge]]"]
---

# LOCK

> [!info] Source
> `kit.ts:LOCK_ROUNDS`, `defendModeDesc`, `AUGMENTS.cfgLock`. Unlocked by [[clamp-driver]].

Freeze junctions for **2 rounds** (`LOCK_ROUNDS`). Nothing rotates or redirects them.

1, 2 or 3 junctions per cast by `DEFEND_WIDTH`.

State lives on the cell as `lockedThroughRound` and `lockedBy`.

## Whose lock stops whom

`canRotate` refuses only when `lockedBy` is the **other** side. Your own lock never blocks you. `redirectTargetLegal` applies the same test.

So a lock is a one-way clamp: it bolts down your line against their [[redirect]], or freezes a junction **they** need on their own board.

## The counter

> [!warning] A SURGE shatters every enemy lock on the board it happens on
> A cascade of 6 or more nodes clears them all. This exists so that the answer to being clamped is a play rather than "wait two rounds". See [[cascades-and-surge]].

## Interaction

[[jam-anchor]] grants a lock effect on your [[redirect]] without spending DEFEND.

## See also

- [[purge]] · [[ward]]
