---
title: DIVE.EXE
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-duel]]", "[[traps-and-telegraphs]]", "[[ruling-11-opponent-identity-tag]]"]
---

# DIVE.EXE

Full-screen · `components/game/duel.tsx`

The duel. The only surface in the game that is not a window.

## What it shows

- The board, at up to 15x11 cells. See [[the-board]].
- **YOU | INTRUSION** turn pair.
- [[ram]], [[route-cost-and-par|par]], round.
- The **threat banner**: "INTRUSION n ROTATIONS FROM THE CORE".
- The machine's **telegraphed aim**, highlighted one tick before it lands.
- The [[the-pouch|pouch]], the three programs, undo, end turn.

## The telegraph is the most important element on the surface

Everything else is state; the telegraph is the one thing that is **about to happen**. It is what makes threats answerable, which is a design pillar rather than a nicety. See [[traps-and-telegraphs]] and [[design-pillars]].

## INTRUSION, always

The opponent is labelled INTRUSION everywhere, on every dive, **including the winning finale dive**. The name [[patch]] is revealed in the scene afterwards, never in the dive's own UI.

That is a deliberate canon decision, not an oversight. See [[ruling-11-opponent-identity-tag]].

## It does not follow the window rules

> [!warning] Exempt from the panel system, and scheduled last
> Full-screen, real-time, and the two-beat telegraph must stay readable. The height ceiling, the 700px breakpoint and the tiling logic all assume a window; none of them apply.
>
> [[law-11-panel-queue]] puts it last for exactly this reason.

## Legibility set the finale board size

The finale is 15x11 and not 17x13 because 17x13 was measured as the worst legibility moment in the game, at 42px per cell. The board is as large as the surface can carry. See [[day-10-the-finale]].

## Teaching

Three coachmarks fire here: `par-budget` (order 40, on going over par), `cascade-bank` (50, on a banked cascade), and `patch-cell-use` (80, while holding pieces). All are **conditional** rather than first-sight, so they arrive at the moment the thing happens. See [[coachmarks]].

## See also

- [[the-duel]] · [[turn-structure]] · [[the-tutorial]]
