---
title: Route cost and par
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[rotation]]", "[[neural-strain]]", "[[opponent-ai]]"]
---

# Route cost and par

> [!info] Source
> `duel-power.ts:routePlan`, `routeCost`; `kit.ts:PAR_RATE`, `PAR_FLAT`, `PAR_STRAIN_PER`; `duel-setup.ts`.

One function prices the entire game.

## Route cost

`routePlan(b)` is a Dijkstra over `(cell, entry-direction)` states. A node's cost is the quarter-turns needed to give it both the arm it is entered by and the arm it exits through. `routeCost(b)` is that plan's cost, or `Infinity` if no route exists.

This single metric is:
- the **board generator's fairness measure** (see [[the-board]]),
- **both planners**, yours implicitly and the machine's explicitly,
- the basis of **par**,
- the **[[the-round-cap|round-cap]] tiebreak**,
- and the **pressure** term in the strain bill.

### Two details that matter

**A bias against rewiring.** If a node already `built` needs turning, its cost gets `+1`. Re-rotating built ground rewires the chain feeding it and drops everything downstream dark. It stays legal, but the planner prefers fresh junctions.

**Self-crossing plans.** A route that crosses itself and demands two different orientations of one node is physically impossible. The search reroutes around the conflicted junction, up to 4 times. If it runs out, it returns the plan with `approx: true`.

> [!warning] `approx: true` does not mean "no route"
> It means the quoted cost is a lower bound and executing the queue verbatim will not conduct. A route **does** exist. Returning `null` there would read as "unreachable", and callers acting on that would be wrong. This distinction is what `sim.ts:checkPlanHonesty` guards.

## Par

Par is the rotation budget for a clean dive, fixed once at board generation:

```
par = ceil(routeCost(playerBoard) * PAR_RATE) + (cfg.parFlat ?? PAR_FLAT)

PAR_RATE = 1.0
PAR_FLAT = 2
PAR_STRAIN_PER = 2
```

Rotations past par chip [[neural-strain]] at 2 per rotation on a win. `cfg.parFlat` is overridden per day and tightens across the arc from 6 on day 1 down to 1 on day 9. See [[the-ten-day-arc]].

### What counts against par

Only **manual rotations** (`econ.rotations`). Program twists from [[redirect]] and [[patch-pieces|patch]] placements are free. Par measures your own routing efficiency, not what was done to you.

> [!danger] REVISED IN PROTOTYPE
> Par was rebased for [[split-boards]]. Route cost roughly doubled when the goal moved to the far edge, and at the old 1.25x rate nobody could ever exceed it: measured par was 26 against 17 actual rotations, so `over` was 0.0% on every day of the arc and strain billed nothing at all. A dive costs about one rotation per point of route, so par is now the route plus a working margin, not the route plus a quarter of itself.

## Pressure

`pressureRounds` increments at the end of each opponent turn when `routeCost(s.boards.opp) <= PRESSURE_RANGE` (4). It bills 2 strain each on a win.

Winning while the machine was one or two turns from its own goal should still cost something. This is the term that makes a narrow win read as narrow. It does not apply in the tutorial.

## The full strain bill

From `duel-actions.ts:finishDuel`, on a **win** only:

```
over  = max(0, econ.player.rotations - par)
chip  = 2  * over                                    PAR_STRAIN_PER
      + 4  * max(0, trapsFired - (firstFault ? 1 : 0))
      + 1  * redirectsTaken                          REDIRECT_STRAIN_PER
      + 2  * pressureRounds                          PRESSURE_STRAIN_PER
      + 10 if the win came at the round cap
chip  = min(45, chip)
```

A loss bills 0. The run is ending anyway.

**Every term is avoidable in principle.** Play a clean dive and the bill is exactly zero. That is what keeps strain an efficiency bill rather than attrition you cannot play out of.

## See also

- [[neural-strain]] - what the bill is paid in
- [[opponent-ai]] - the same metric, used against you
- [[simulation-harnesses]] - `pd` measured against `pdTarget` every day
