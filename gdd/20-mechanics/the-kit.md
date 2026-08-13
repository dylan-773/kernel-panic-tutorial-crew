---
title: The kit
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[program-tiers]]", "[[augments]]", "[[player-skills]]"]
---

# The kit

> [!info] Source
> `content/kit.ts`. `PROGRAM_COST = 1`.

Every diver, and every intrusion, carries exactly three programs.

| Program | Acts on | Modes |
|---|---|---|
| [[scan]] | your own board | none (tier only) |
| [[attack]] | **their** board | [[redirect]], [[arm-halt]], [[arm-siphon]] |
| [[defend]] | your own board | [[purge]], [[lock]], [[ward]] |

Rules that never change:

- **Always three.** Programs never unlock and are never consumed.
- **1 RAM each.**
- **Once per turn each**, tracked by `econ.used`. A full turn can cast all three.
- They **upgrade** (tier, at day close) and **reconfigure** (mode, from [[augments]]).
- Program twists do not count against [[route-cost-and-par|par]].

> [!danger] REVISED IN PROTOTYPE
> The largest single change from the final draft. Eight ability verbs and about twenty-four variants became three programs. The catalog was unreadable at speed: players could not hold it in their heads mid-duel, so they defaulted to one or two verbs and ignored the rest. Depth moved into modes and tiers rather than count.

## The counter triangle

Modes answer each other rather than laddering:

- [[redirect]] cuts routes, and is stopped by [[lock]] and [[ward]].
- [[arm-halt]] and [[arm-siphon]] plant mines, and are answered by [[scan]] then [[purge]], or prevented by [[ward]].
- [[lock]] freezes, and is shattered by a SURGE-tier [[cascades-and-surge|cascade]].

Every telegraphed threat has a counter castable during the wind-up. That is a design law, not a coincidence. See [[traps-and-telegraphs]].

## The machine draws from the same table

`oppKitFor` builds the intrusion's kit from the same six modes, widening by job tier. There is no enemy-only ability. See [[difficulty-dials]].

## See also

- [[program-tiers]] - what a tier buys
- [[the-night-shop]] - where tiers are bought
