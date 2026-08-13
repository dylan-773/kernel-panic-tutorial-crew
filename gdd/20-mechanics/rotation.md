---
title: Rotation
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[reach-and-placement]]", "[[route-cost-and-par]]", "[[ram]]"]
---

# Rotation

> [!info] Source
> `duel-power.ts:rotCostFor`, `repairCostOf`, `canRotate`; `types.ts` for arm masks.

The only movement verb. You twist a junction a quarter turn so its arms line up and signal flows further.

- **Cost:** 1 [[ram]] per quarter turn.
- **Counts against [[route-cost-and-par|par]]:** yes. Manual rotations increment `econ.rotations`. Program twists and patch placements do **not**.
- **Settles immediately:** the board recomputes after every rotation. See [[built-and-power]].

## Arm masks

Directions are `0 north, 1 east, 2 south, 3 west`, and a cell's arms are a 4-bit mask where `bit = 1 << dir`.

| Piece | Mask | Shape | Generator draw |
|---|---|---|---|
| `PIECE_I` | `0b0101` | straight | 40% |
| `PIECE_L` | `0b0011` | elbow | 45% |
| `PIECE_T` | `0b0111` | tee | 12% |
| `PIECE_X` | `0b1111` | cross | 3% |

Constants in `duel-types.ts`, distribution in `duel-setup.ts:drawMask`.

## Rotation is unidirectional

> [!warning] This is a design decision, not a missing feature
> `(rot + 1) % 4` everywhere, and `rotCostFor` only searches forward. There is no shortest-way-round. Do not "fix" it.

`rotCostFor(c, needed)` walks `k = 0..3` forward and returns the first `k` whose rotated arms cover the needed mask, or `Infinity`.

### The exchange rate this creates

`repairCostOf(c)` prices undoing one enemy twist:

| Piece | Cost to undo one twist |
|---|---|
| straight (I) | 1 RAM |
| elbow (L) | **3 RAM** |
| tee (T) | **3 RAM** |
| cross (X) | 0 RAM |

A straight returns to its own orientation in two quarter turns because it is symmetric, so one twist costs one to undo. An elbow or tee has four distinct orientations, so undoing a single forward twist means going three more forward.

**That asymmetry is the economy of the duel.** It is why reaching across to the enemy board is worth the RAM: one [[redirect]] at 1 RAM can cost them 3 to repair. It is also the reason there is no hold-the-goal phase. If undoing were cheap, interference would be noise and the game would collapse into two parallel solitaire puzzles.

The opponent's cut scorer weights targets by `repairCostOf` at [[difficulty-dials|horizon]] 3, so a smart machine specifically twists your elbows.

## Fused cells never rotate

A placed [[patch-pieces|patch piece]] is welded. `fused: true` means:
- `rotCostFor` returns 0 if it already fits and `Infinity` otherwise.
- `canRotate` refuses.
- `repairCostOf` returns 0.
- REDIRECT cannot touch it either.

Its orientation is final for everyone. A patch piece is therefore both a bridge and a permanent anchor the enemy cannot twist.

## What can stop you rotating

`canRotate(s, side, idx)` refuses only when:

1. The cell is not a junction (entry, goal and slag are not rotatable).
2. The cell is `fused`.
3. An enemy [[lock]] holds: `lockedThroughRound >= s.round` and `lockedBy` is the other side.
4. The cell is unbuilt and out of [[reach-and-placement|reach]].

Built ground you own is **always** rotatable. Note that a lock cast by your own side never blocks you.

## See also

- [[the-board]] - piece distribution and generation
- [[redirect]] - the enemy's version of this verb
- [[turn-structure]] - the one take-back per turn
