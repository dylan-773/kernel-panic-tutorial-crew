---
title: Player character
status: canon
source: lore
owner: orchestrator
updated: 2026-08-05
related: ["[[the-player]]", "[[player-skills]]", "[[player-metrics]]"]
---

# Player character

The son. Unnamed, never pictured, never speaks in the third person.

Full character sheet in [[the-player]]. This note is the mechanical side of the same person.

## What the player is, mechanically

| Aspect | Expressed as |
|---|---|
| Health | [[neural-strain]], 100 down to 0 |
| Action economy | [[ram]], 5 to 9 per turn |
| Skills | [[player-skills]] - three programs, tiers, modes |
| Inventory | [[player-inventory]] - pieces, pouch, bays |
| Money | [[credits]] |
| Progress | the day, 1 to 10 |

There is no level, no XP, no class and no stat block. Every axis of power is either a program tier, an augment, or a resource.

## What the player does

Exactly four verbs, and the [[the-tutorial|opening dive]] teaches all four and nothing else:

1. **rotate** - [[rotation]]
2. **scan** - [[scan]]
3. **defend** - [[defend]]
4. **attack** - [[attack]]

`teach-sim.ts` enforces this: `CORE_VERBS = ["rotate", "scan", "defend", "attack"]` must all be taught in the opening dive or the build fails.

## Point of view

The player is always at the bench, in the shop, in the chair. The dive is something they do at a desk. That framing is why the entire interface is an operating system rather than a world: [[kp-os]] is not a menu over the game, it is the game's diegetic surface.

## See also

- [[the-player]] - who he is
- [[game-controls]] - what he does with a mouse
