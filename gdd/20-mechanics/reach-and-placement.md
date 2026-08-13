---
title: Reach and placement
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[rotation]]", "[[built-and-power]]", "[[patch-pieces]]"]
---

# Reach and placement

> [!info] Source
> `duel-power.ts:reachOf`, `inReach`, `canPlace`, `withinReachWalk`, `isFrontier`; `kit.ts:BASE_REACH`.

Reach is how far ahead of your built ground you are allowed to work.

## The number

```
BASE_REACH = 2          (kit.ts)
reachOf() = 2, or 4 with LONG ARMS
```

`reachOf(s, side)` returns `BASE_REACH + 2` when the player owns [[long-arms]], otherwise `BASE_REACH`. The opponent always has base reach.

## Why 2 and not 1

Depth 1 is the classic frontier: you can only touch what directly abuts your live edge. At depth 2 you can **line up a chain before lighting it**.

That is the entire setup move for [[cascades-and-surge]]. Hold a long chain aligned behind one unturned junction for two or three turns, then flip that junction and light all of it at once. Reach 2 exists to make that possible; [[long-arms]] at reach 4 exists to make it bigger.

## The walk

`withinReachWalk` breadth-firsts outward from the target cell for `reach` steps and returns true if it touches the entry or any **built** junction. It walks **only through unbuilt junctions**, so you cannot tunnel toward built ground through slag or around obstacles.

Two consequences worth stating:

1. Reach measures from `built`, not from `power`. An enemy cut that darkens your chain does not shrink your reach. See [[built-and-power]].
2. Reach is only ever consulted for **unbuilt** cells. `inReach` returns false immediately for anything already built, because `canRotate` short-circuits built ground to always-allowed.

## Placement uses the same walk

`canPlace(b, idx, reach)` is `withinReachWalk` with one different precondition: the target must be `kind === "block"`, that is, slag.

So a [[patch-pieces|patch piece]] fills a slag cell that is within reach of built ground. Same distance, same walk, different target kind.

Placement rules:
- **4 RAM** (`PLACE_COST`, `patch-cells.ts`).
- **One per turn** (`econ.placedThisTurn`).
- Does **not** count against [[route-cost-and-par|par]].
- The placed cell becomes `fused` forever. See [[rotation]].

## `isFrontier`

A separate, narrower predicate: unbuilt junctions orthogonally adjacent to built ground or the entry. Used for display and for generation constraints, not for legality. Reach is the legality rule.

## See also

- [[the-board]] - slag density per day
- [[long-arms]] - the reach boost
- [[splice-refund]] - placement that refunds its own RAM
