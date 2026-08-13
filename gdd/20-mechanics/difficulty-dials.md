---
title: Difficulty dials
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[opponent-ai]]", "[[the-ten-day-arc]]", "[[arc-composer]]"]
---

# Difficulty dials

> [!info] Source
> `duel-types.ts:DuelConfig`; `content/arc.ts:DayConfig`, `DAY_CONFIGS`, `oppKitFor`.

Three knobs govern how hard the machine is. Only two of them are load-bearing.

## horizon (0 to 3) - the intelligence dial

How deep the machine looks before reaching across. This is the dial the game did not have for a long time: every earlier lever scaled RAM, cast width or mistake rate, never what the opponent **understood**.

| horizon | Behaviour |
|---|---|
| 0 | No cut scoring at all. It just races its own board. |
| 1 | Scores a twist by how much it raises your route cost. This was the whole old AI. |
| 2 | Also scores by how much of your **live** grid it puts in the dark. |
| 3 | Also weights by what the twist costs you to undo, and will abandon its own race to deny yours when your clock is shorter. |

Horizon 3 is where the machine starts playing the [[rotation|repair-cost]] economy against you deliberately, targeting elbows and tees over straights.

## focus (0 to 1) - per turn

Chance that a cut lands on the best target rather than a random one of the top three.

```ts
const sloppy = roll(s) >= s.cfg.focus;   // opponent.ts
```

**Deliberately per-turn.** Unlike `greed` it does not compound with duel length, so it reads the same at three rounds and at nine. `focus` is what replaced `greed`'s real job.

## greed (0 to 1) - per rotation, retired as a dial

Chance per **rotation** that the opponent does not fumble.

> [!warning] Finished as a difficulty dial. Kept only for movement texture, and pinned high.
> It compounds with duel length. `greed^oppRam` means the same 0.94 that reads as "occasionally sloppy" over a two-round duel is a 2% chance of a clean turn over a nine-round one. The difficulty it expressed depended on how long the fight ran, which is not a property you can tune against.

Shipped values sit between 0.70 and 0.99 and reach 1.0 in the finale. Treat it as flavour.

## The rest of DayConfig

```ts
interface DayConfig {
  grid: [number, number];
  oppRam: number;
  greed: number;
  abilityFreq: number;   // 0..1 chance per turn of a non-forced cast
  pdTarget: number;      // route cost the generator aims BOTH boards at
  minPd?: number;        // floor on the player's opening route cost
  headStart: number;     // junctions the intrusion arrives pre-aligned along
  parFlat: number;       // flat term of the par margin
  horizon: number;
  focus: number;
  slag: number;
  patchDrop: number;
  jobTiers: [number, number, number];
}
```

`minPd` exists because the old guarantee was only "more than one turn of RAM", and boosts, [[cascades-and-surge|cascade banking]] and a [[patch-pieces|patch]] shortcut can beat that. It is the floor that stops an opening burst closing a board outright.

Values per day in [[the-ten-day-arc]].

## Two tier vocabularies

> [!warning] These are different numbers that look the same
> **Program tiers** run 1 to 3 (`Tier`). They govern width and range. See [[program-tiers]].
> **Job, customer and day difficulty tiers** run 1 to 5. They govern pay and opponent kit.
>
> `oppKitFor(tier, dominant, seed)` is the mapping between them.

### oppKitFor

Starts from the customer's `dominant` mode, then broadens:

| Job tier | Kit |
|---|---|
| 1 | dominant only |
| 2 | + 1 random attack mode |
| 3 | + 1 random defend mode |
| 4 | + 1 more of each |
| 5 | **all three attack and all three defend** |

Cast width follows separately: `oppTier = tier <= 2 ? 1 : tier <= 4 ? 2 : 3`, feeding `ATTACK_WIDTH` and `DEFEND_WIDTH`.

So a tier 5 job is not simply "more damage". It is an opponent with the full vocabulary casting three targets wide.

## Who owns these

The [[arc-composer]] proposes DayConfig deltas against win-rate targets, and only with before and after sim numbers. Iron rule 4: curve changes enter through the balance loop. See [[the-plays]].

## See also

- [[opponent-ai]] - what consumes these values
- [[simulation-harnesses]] - how a change is measured
