---
title: The board
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[split-boards]]", "[[route-cost-and-par]]", "[[determinism-and-seeds]]"]
---

# The board

> [!info] Source
> `duel-setup.ts:generateBoard`, `drawMask`, `mixSeed`; `duel-types.ts:DuelCell`.

Each side's grid is generated from the run seed, then rejection-sampled until it is fair.

## Cell kinds

`CellKind = "node" | "entry" | "goal" | "block"`

- **node** - a rotatable connector. The only kind `isJunction` accepts.
- **entry** - the signal source. One per board, left edge, mid row.
- **goal** - three cells, right edge. A sink: signal arrives and stops.
- **block** - slag. Impassable, and the only thing a [[patch-pieces|patch piece]] can fill.

> [!info] Why `isJunction` exists
> Every rule meaning "a connector" goes through the predicate rather than testing `kind === "node"` inline. There is one connector kind today. The predicate exists so that adding a second does not mean finding twenty-odd open-coded comparisons and silently missing three.

## Piece distribution

`drawMask` draws:

| Piece | Share |
|---|---|
| straight (I) | 40% |
| elbow (L) | 45% |
| tee (T) | 12% |
| cross (X) | 3% |

Elbows dominate, which is what makes [[rotation|unidirectional rotation]] bite: the most common piece costs 3 RAM to un-twist. Crosses are rare because they are free to repair and therefore dead weight for interference.

## Slag density

`cfg.slag`, defaulting to 0.18 and 0.12 in the tutorial. It climbs across the arc from 0.18 on day 1 to 0.27 in the finale. See [[the-ten-day-arc]].

Slag does two jobs: it constrains routes, and it is the only surface [[patch-pieces]] can be spent on. Rising slag is simultaneously rising difficulty and rising patch value.

## Generation constants

```
MAX_OPENING_BUILT      = 3      nodes the opening power may already light
GEN_REACH              = 2      reach assumed during generation checks
HEAD_START_COST        = 1.8    route cost one head-start junction is worth
HEAD_START_COMPENSATION= 0.6    how much of that the opponent board gives back
PD_FLOOR_RATE          = 0.8
SHORTCUT_FLOOR_RATE    = 0.65
```

`generateBoard` rejection-samples up to **160 attempts** toward `cfg.pdTarget`.

## The three fairness rejections

A candidate board is thrown away if:

1. **Its opening power already reaches the goal.** A board that is already solved is not a board.
2. **Its opening power lights more than `MAX_OPENING_BUILT` (3) nodes.** This bound is also load-bearing for teaching: the `first-rotation` tutorial beat tests `ownedNodes <= 3`. When the two drifted apart, **23.9% of opening dives never taught rotation at all**. See [[tutorial-beats]].
3. **(Player boards only) a single patch cross placed from opening reach collapses the route below `0.65 * pdTarget`.** One lucky piece must not trivialize the board.

## How the two boards are matched

The opponent's board is not generated to the same target as the player's. It is targeted at the player's **actual** measured cost, plus `round(headStart * 1.8 * 0.6)`.

So the invariant that `|pd - od| <= 2` falls out by construction rather than by tuning. `sim.ts` asserts measured `pd` stays within `PD_TOLERANCE` (2.0) of `pdTarget` on every day, and exits 1 if not.

## Par is set here

Once, at generation:

```
par = ceil(routeCost(playerBoard) * PAR_RATE) + (cfg.parFlat ?? PAR_FLAT)
```

See [[route-cost-and-par]].

## `oppOpens`

Finale only. `startOppTurn` runs before the player's first input, because the machine was already inside. See [[day-10-the-finale]].

## See also

- [[difficulty-dials]] - what changes per day
- [[determinism-and-seeds]] - why the same seed gives the same board
