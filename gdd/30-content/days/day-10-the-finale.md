---
title: Day 10 - the finale
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-finale-encounter]]", "[[the-machine]]", "[[the-ten-day-arc]]"]
---

# Day 10 - the finale

> [!info] Source
> `content/arc.ts:finaleConfig`, `FINAL_DAY = 10`. Screen: `finalePre` then the dive.

No job board. The back room settles up.

| | |
|---|---|
| Grid | **15x11** |
| Opponent RAM | 11 |
| greed / focus | **1.00** / **1.00** |
| abilityFreq | **0.90** |
| pdTarget | **29** |
| minPd | **18** |
| headStart | 1 |
| parFlat | 2 |
| horizon | 3 |
| slag | **0.27** |
| Opponent kit | **all 3 attack, all 3 defend**, `oppTier: 3` |
| dominant | redirect |
| **`oppOpens`** | **true** |
| Target kitted win rate | ~35% |

## No fumbles

`greed` and `focus` both sit at 1.00. The machine never misfires and every cut lands on the best target. Combined with horizon 3 and the full mode vocabulary, this is the only opponent in the game with no weakness to exploit.

## `oppOpens`

**The machine takes the first turn.** `startOppTurn` runs before the player's first input.

The fiction is exact: it was already inside. This is the only dive in the game where the player is answering rather than opening, and it is why the kit-less proxy posts a 0% win rate here by construction.

## Why 15x11 and not larger

A source comment records that 17x13 was tested and was the worst legibility moment in the game at 42px per cell. The finale board is as large as the interface can carry. See [[law-3-fluid-and-the-height-ceiling]].

## Mechanically it is an ordinary duel

Same three programs, same rules, no special mechanic and no phases. **That is the point.** The final exam is the thing you have been practising, run at full difficulty, and the seal opens on "A FAIR WIN, NO ASSISTS".

See [[the-finale-encounter]] and [[the-machine]].

## What a win unlocks

`machineOpened` on `MetaState`, permanently. `finaleWinScene()` plays and [[entry-patch|PATCH]] becomes readable. A win on **any** run delivers the full truth regardless of `runCount`. See [[reveal-schedule]].

## See also

- [[day-9]] · [[backroom-lck]]
