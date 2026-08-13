---
title: Opponent AI
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[difficulty-dials]]", "[[route-cost-and-par]]", "[[traps-and-telegraphs]]"]
---

# Opponent AI

> [!info] Source
> `opponent.ts` (598 lines). Uses the same `routePlan` the player's board is measured by.

The intrusion is a scripted opponent, not a search. It runs the same Dijkstra you do, on its own board, and decides each turn whether to race or to interfere.

## Stance

`Stance = "race" | "deny" | "mixed"`, chosen by `assessRace`, which compares the two clocks **in turns** rather than in raw cost:

```
clock = routeCost / ramPerTurn
```

Comparing turns rather than cost is what makes the comparison fair across different RAM budgets. A machine with 11 RAM per turn and a route of 22 is two turns out; so is a player with 6 RAM and a route of 12.

**`assessRace` only runs at [[difficulty-dials|horizon]] 3.** Below that the machine has no concept of your clock and cannot decide to abandon its own race.

## Cut scoring

What a candidate twist on your board is worth:

```
cutScore = costGain * 2
         + (horizon >= 2 ? litLost * 3 : 0)
         + (horizon >= 3 ? repairCostOf * 2 : 0)
```

- **`costGain`** - how much it raises your [[route-cost-and-par|route cost]].
- **`litLost`** - how much of your **live** grid goes dark. Weighted highest, because tempo damage is felt immediately.
- **`repairCostOf`** - what it costs you to undo. At horizon 3 the machine deliberately targets elbows and tees, which cost 3 RAM to un-twist, over straights at 1. See [[rotation]].

`focus` then decides whether the cut lands on the best-scoring target or a random one of the top three.

## Replanning

`oppTurn.replans = 3` per turn, each requiring **strict progress**: the new plan must beat `lastReplanCost`. Without that requirement a machine can oscillate between two equal-cost plans and burn its whole turn achieving nothing.

`oppTurn.queue` holds committed rotations as absolute target rotations, not deltas, so a queue stays valid if something else moves the cell.

## Casting

- `abilityFreq` is the per-turn chance of a **non-forced** cast.
- The `dominant` mode is prioritized and guaranteed early, which is what makes the Analyze tell honest. See [[traps-and-telegraphs]].
- `oppKitFor` decides which modes are available at all, by job tier. See [[difficulty-dials]].
- At most one program per turn.

## The telegraph

`oppTurn.aim` holds the locked-in move for one tick before it lands, and `oppStep` advances the turn one visible move at a time. The player watches the machine play rather than seeing a diff.

## The tutorial machine

`tutorialConfig()` sets `horizon: 0`, `focus: 0.5`, `abilityFreq: 0`, `oppAttackModes: ["armHalt"]` and no defend modes. It races its own board, plants one kind of trap, and is RAM-throttled.

It is unwinnable by construction rather than by difficulty: touching the core seals every port. See [[the-tutorial]].

## Cost in simulation

The AI is the wall-clock cost of the balance harness. `sim.ts` carries `BEAT_MS = 255` as a blended proxy for its thinking time and reports `ai seconds` per day. That number is why `opts.arm === false` disables undo snapshotting for simulated duels. See [[simulation-harnesses]].

## See also

- [[difficulty-dials]] - the values fed in
- [[the-ten-day-arc]] - how they escalate
