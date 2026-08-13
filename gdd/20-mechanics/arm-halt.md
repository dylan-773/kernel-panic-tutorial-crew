---
title: ARM - HALT
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[attack]]", "[[traps-and-telegraphs]]", "[[tripwire]]"]
---

# ARM: HALT

> [!info] Source
> `kit.ts:attackModeDesc`, `AUGMENTS.cfgArmHalt`. Unlocked by [[halt-driver]].

Plant a halt trap on open junctions on the enemy board. When their signal claims the node, **they lose a full turn**.

Targets per cast follow `ATTACK_WIDTH`: 1, 2 or 3.

## Firing

A trap fires the first time signal reaches its node, and is consumed. It never blocks: the cascade runs straight past it.

If the victim is the acting side, the turn is forfeit **now**, after the cascade lands. Otherwise `loseNextTurn` is set.

Player-facing copy:

> HALT TRAP. Your signal hit an armed node. The cascade lands, then your turn is forfeit.

## Why a full turn

It is the heaviest single tempo swing in the game, which is what makes the honest Analyze tell matter. A halt-dominant customer is a scan-first job, and misplaying that is the most expensive mistake available.

## Interaction

[[tripwire]] adds 3 RAM burned off the victim's next active turn on top of the forfeit.

## Counters

[[scan]] then [[purge]]; [[ward]] to prevent the landing; a BREAK-tier [[cascades-and-surge|cascade]] to cook one dead.

## See also

- [[arm-siphon]] - the other trap kind
