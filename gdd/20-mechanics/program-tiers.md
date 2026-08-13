---
title: Program tiers
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-kit]]", "[[the-night-shop]]", "[[difficulty-dials]]"]
---

# Program tiers

> [!info] Source
> `kit.ts:SCAN_RANGE`, `ATTACK_WIDTH`, `DEFEND_WIDTH`, `WARD_RADIUS`, `SIPHON_STEAL`.

`Tier = 1 | 2 | 3`. Each program tiers independently. Tiers are bought one per night at day close, capped at 3. See [[the-night-shop]].

| Value | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| `SCAN_RANGE` | 3 | 6 | 99 (whole board) |
| `ATTACK_WIDTH` | 1 | 2 | 3 |
| `DEFEND_WIDTH` | 1 | 2 | 3 |
| `WARD_RADIUS` | 1 | 2 | 3 |
| `SIPHON_STEAL` | 2 | 3 | 4 |

Width is targets per cast: nodes redirected, traps planted, traps cleared, locks placed.

Note `SIPHON_STEAL` scales with the **ATTACK** tier, so width buys bite as well as breadth.

> [!warning] Two tier vocabularies
> These are program tiers, 1 to 3. Job, customer and day difficulty tiers run 1 to 5 and are a different scale entirely. `oppKitFor` maps between them. See [[difficulty-dials]].

## See also

- [[the-kit]] - what tiers apply to
