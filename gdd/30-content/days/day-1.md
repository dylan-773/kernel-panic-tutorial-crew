---
title: Day 1
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-ten-day-arc]]", "[[the-tutorial]]", "[[day-2]]"]
---

# Day 1

> DAY 1. The shop is yours. Three tickets on the spike.

| | |
|---|---|
| Grid | 9x7 |
| Opponent RAM | 6 |
| horizon / focus | **0** / 0.50 |
| pdTarget | 16 |
| headStart | 0 |
| parFlat | **6** |
| slag / patchDrop | 0.18 / **0.35** |
| Job tiers | 1, 1, 1 |
| Target kitted win rate | ~84% |

## What day 1 is for

The gentlest configuration in the game. **horizon 0** means the machine does no cut scoring at all: it simply races its own board and never reaches across to interfere. The player meets the race before they meet the duel.

`parFlat` at 6 is the most forgiving margin of the arc, so a clumsy first day bills almost no [[neural-strain]].

The highest patch drop rate (0.35) against the lowest slag (0.18), so the player accumulates [[patch-pieces|pieces]] before they need them.

## Teaching

On run 1 the opening dive happens **before** day 1: `opener` to `tutIntro` to [[the-tutorial|tutorial]] to `tutOutro` to `dayOpen`. Every coachmark carries `notBeforeDay: 1`, so day 0 takes none by construction.

## See also

- [[day-2]] · [[the-ten-day-arc]]
