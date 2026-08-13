---
title: Meta progression
status: unwritten
source: none
owner: user
updated: 2026-08-05
related: ["[[death-and-run-end]]", "[[reveal-schedule]]", "[[design-change-log]]"]
---

# Meta progression

> [!question] UNWRITTEN
> No document currently states what carries between runs beyond story progress. The final draft said "unlocked abilities persist across runs; currency, RAM and Neural Capacity reset". v2 removed that mechanic and **never replaced the statement**, so the design has a hole where a policy should be.

## What is actually true today

`MetaState` persists (`save.ts`):

| Field | Carries |
|---|---|
| `runCount` | yes - drives the [[reveal-schedule]] |
| `machineOpened` | yes - unlocks the [[entry-patch|PATCH]] journal entry |
| `taught` | yes - a mechanic explained in run 3 stays explained in run 4 |
| `stats` | yes - [[scoring-and-lifetime-stats]] |
| `sound`, `music` | yes - preferences |

Everything on `RunState` dies: credits, augments, program tiers, RAM per turn, patch pieces, boost bays, strain.

So mechanically the answer is currently **"nothing carries except knowledge and story"**. That is a coherent roguelike position. It has simply never been written down as a decision, which means nobody can tell whether it is the design or an omission.

## What this note must decide

- [ ] Is "nothing carries" the intended final answer, or a gap left by the v2 cut?
- [ ] If something should carry, what: a permanent augment unlock pool, a starting-RAM floor, retained [[patch-pieces|pieces]], a credit carryover?
- [ ] Does the answer change after `machineOpened` is true, when the story is complete and only the game remains?
- [ ] How does any carry interact with the [[augments|augment pool exhausting on day 6]]? A permanent unlock pool would make that worse, not better.
- [ ] Does the [[the-tutorial|tutorial]] still run on run 2 and beyond? (Currently no: run 1 goes `opener` to `tutIntro`, later runs go straight to `dayOpen`.)

## What argues against adding carry

The story already **is** the meta progression. `runCount` gates the reveals, and [[death-and-run-end|losing is how the player learns who their father was]]. Adding mechanical carry would give the player a second reason to lose on purpose, competing with the first.

## See also

- [[design-change-log]] - listed under Still open
