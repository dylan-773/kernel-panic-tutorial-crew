---
title: ARM - SIPHON
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[attack]]", "[[ram]]", "[[deep-siphon]]"]
---

# ARM: SIPHON

> [!info] Source
> `kit.ts:attackModeDesc`, `SIPHON_STEAL`, `AUGMENTS.cfgArmSiphon`. Unlocked by [[siphon-driver]].

Plant a siphon trap on open junctions on the enemy board. When it fires, RAM **drains from their next turn into yours**.

| ATTACK tier | RAM stolen |
|---|---|
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

`SIPHON_STEAL` scales with the caster's ATTACK tier, so tiering ATTACK buys bite as well as width.

## Why it reads differently from HALT

A halt is a tempo hit. A siphon is a **resource swing**: it does not just cost them a turn, it funds yours. Against a machine that is ahead on clock, a siphon converts its lead into your RAM.

The shipped augment description is explicit that the steal is bigger "when you are the one springing it".

## Mechanics

Fires on first light, is consumed, never blocks. The drain lands via `drainNext` on the victim and as a gain on the caster. See [[traps-and-telegraphs]] and [[turn-structure]].

## Interaction

[[deep-siphon]] adds 1 extra RAM per steal. [[echo-tap]] pays you 2 RAM whenever any of your traps fires.

## See also

- [[arm-halt]] - the other trap kind
