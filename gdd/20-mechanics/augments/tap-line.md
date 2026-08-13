---
title: TAP LINE
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[scan]]", "[[opponent-ai]]", "[[augments]]"]
---

# TAP LINE

**Boost** · `tapLine`

> SCAN also traces the intrusion's planned route to the core, visible for 2 rounds.

Stored as `DuelState.routeTrace: { round, cells }`, cleared each round.

The only pure-information boost. It shows you the machine's `routePlan`, which is what lets you aim a [[redirect]] at the junction that costs it most rather than guessing. Pairs with [[difficulty-dials|horizon]] 3 opponents, which are the ones whose plans are worth reading.

One of only two augments the v2 GDD and the shipped catalog agree on.
