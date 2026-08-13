---
title: LONG ARMS
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[reach-and-placement]]", "[[cascades-and-surge]]", "[[augments]]"]
---

# LONG ARMS

**Boost** · `longArms`

> Rotate open junctions up to 4 steps from your territory instead of 2, and place patch pieces just as far. Bigger setups, bigger cascades.

`reachOf` returns `BASE_REACH + 2` when owned. Applies to both rotation and [[patch-pieces|patch]] placement, since `canPlace` uses the same reach walk.

The cascade-scaling boost. Reach 2 lets you hold a chain; reach 4 lets you hold a much longer one, which moves you up the `cascadeRam` curve. See [[reach-and-placement]].
