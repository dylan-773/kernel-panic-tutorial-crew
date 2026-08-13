---
title: Built and power
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[split-boards]]", "[[cascades-and-surge]]", "[[reach-and-placement]]"]
---

# Built and power

> [!info] Source
> `duel-types.ts:DuelCell.built` and `Board.power`; `duel-power.ts:computePower`, `settlePower`.

Two layers per board. Keeping them apart is the whole design.

| Layer | Where | Meaning | Permanent? |
|---|---|---|---|
| `built` | `DuelCell.built` | Ever lit by this board's owner | **Yes** |
| `power` | `Board.power[]` | Carrying signal from `entry` right now | **No** |

**Progress is reversible in throughput and never in construction.**

## What each one governs

`built` governs:
- **[[reach-and-placement|Reach]].** The reach walk starts from built ground, not from live ground.
- **[[cascades-and-surge|Cascade payment]].** Only first lights pay. Re-lighting a repaired chain pays zero.
- **Rotation rights.** `canRotate` returns true unconditionally for a built node you own. Built ground is always yours to rewire.

`power` governs:
- **Winning.** `goalLive` asks whether any goal cell is currently powered.
- **Trap springing.** A trap fires the first time signal reaches its node.
- **What the display shows as alive.**

## Why reach walks from built and not from live

Directly from the source comment in `duel-power.ts:inReach`:

> Walking from BUILT rather than from LIVE is deliberate: an enemy cut takes your power but must never take back your frontier, or a single redirect deep in the chain would strand everything you had set up ahead of it.

This is the load-bearing consequence of the split. One enemy [[redirect]] upstream turns everything behind it dark, which is real damage to your tempo. But it does not un-make the frontier you built, so it cannot retroactively make your forward setup illegal to touch.

Without this rule, a single well-placed redirect would be a soft board reset. With it, a redirect costs you throughput and about 3 RAM to undo, which is a price rather than a catastrophe.

## `computePower` versus `settlePower`

- `computePower(b)` is the **pure read**. Safe to call from planners and from the renderer. A breadth-first flood from `entry` through joined arms.
- `settlePower(b)` is the same walk plus the two effects that must happen exactly once per change: marking cells `built` on first light, and springing traps.

`settlePower` runs after **every** rotation. That immediacy is the texture of the game: you twist one junction and the board answers.

It returns a `SettleResult` carrying `power`, `built` (the newly lit, in light order), `trapsFired`, and `reachedGoal`.

## `litWave`

Each newly built cell records `litWave`, its ordinal within that settle. It drives the staggered cascade animation, so a ten-node light visibly rolls outward rather than snapping on. No rule reads it.

## A performance note that is load-bearing

`computePower` uses a head pointer rather than `Array.shift()`. `shift()` is O(n) on a JS array, which made the flood O(cells squared). It runs on every rotation **and** inside the opponent's per-candidate cut-scoring loop, so it is genuinely hot.

## See also

- [[the-board]] - what the cells are
- [[traps-and-telegraphs]] - what springs on first light
- [[turn-structure]] - why undo does not un-spring a trap
