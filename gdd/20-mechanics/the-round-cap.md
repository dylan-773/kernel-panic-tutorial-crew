---
title: The round cap
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[win-conditions]]", "[[route-cost-and-par]]", "[[overtime-clause]]"]
---

# The round cap

> [!info] Source
> `duel-types.ts:ROUND_CAP`; `duel-actions.ts`.

```
ROUND_CAP = 25
```

One round is one player turn followed by one opponent turn. At `round > 25` the dive ends with `winKind: "cap"`.

## The tiebreak

Whoever is closer to their own goal, measured in [[route-cost-and-par|route cost]]:

```
playerCloser = pd <= od
```

Ties go to the player. `pd` is the player's remaining route cost, `od` the opponent's.

Using route cost rather than nodes lit is deliberate. Nodes lit rewards sprawl; route cost rewards being nearly finished, which is what "closer" should mean in a race.

## Why a cap exists at all

Two boards, two racers, and interference in both directions can produce a duel that goes nowhere: each side undoing the other's progress at roughly the rate it is made. The cap guarantees termination.

It also guarantees the **simulation** terminates, which matters more than it sounds. Every balance claim in this project comes from 200 seeds a day through `sim.ts`. An unbounded duel makes the harness unbounded. See [[simulation-harnesses]].

## A cap win is a bad win

Deliberately. It is the game's "you did the job, badly, and late":

| Cost | Value |
|---|---|
| Extra [[neural-strain]] | +10 |
| Ticket pay | 50% |
| Ticket pay with [[overtime-clause]] | 75% |

The fiction is billing: the client eats the hours past the deadline. [[ruling-10-overtime-billing]] is the canon decision that makes the augment coherent rather than an arbitrary number tweak.

## Measured behaviour

`sim.ts` reports `cap%` per day alongside win rate, and tallies `kitted ends` across won-goal, won-cap, lost-goal, lost-seal, lost-cap. Watch also the `<=2r` figure, the share of duels resolving in two rounds or fewer, which should stay under about 40%. Median rounds should sit at 3 to 4.

A rising cap share means the interference economy has overtaken the racing economy, which historically has meant [[difficulty-dials|horizon]] or `abilityFreq` went up without a matching answer in the player's kit.

## See also

- [[difficulty-dials]] - the knobs that move cap share
- [[clean-run]] - the augment that pays a consolation on a trap-free cap loss
