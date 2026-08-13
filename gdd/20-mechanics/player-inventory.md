---
title: Player inventory
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-pouch]]", "[[boost-bays]]", "[[loadout-cfg]]"]
---

# Player inventory

Three containers, all capped, all emptied at run end.

## The pouch

Up to 5 [[patch-pieces]], held as shaped 4-bit masks. Shape matters as much as count, because a piece cannot be rotated to fit. See [[the-pouch]].

Managed in [[solder-bay]], where two pieces can be welded into their union.

## Boost bays

3 to 5 slots, holding boost [[augments]]. Configs do not occupy bays. At full bays a draft pick becomes a swap. See [[boost-bays]].

## The kit

Not really an inventory: three programs that are always present, each with a tier and a selected mode. Configured in [[loadout-cfg]]. See [[player-skills]].

## What there is not

No consumables beyond patch pieces, no equipment slots, no weapons, no crafting materials other than pieces welding into pieces, and no stash. Nothing carries between runs. See [[meta-progression]].

## Why so small

Everything the player owns has to be readable **during a turn**, on one screen, under a hard 700px height ceiling. See [[law-3-fluid-and-the-height-ceiling]]. An inventory that needs scrolling would break the interface law before it broke the design.

## See also

- [[solder-bay]] · [[loadout-cfg]]
