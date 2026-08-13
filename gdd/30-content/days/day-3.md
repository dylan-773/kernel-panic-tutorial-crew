---
title: Day 3
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-ten-day-arc]]", "[[day-2]]", "[[day-4]]"]
---

# Day 3

> DAY 3. Word is getting around. The tickets are getting stranger.

| | |
|---|---|
| Grid | **9x9** |
| Opponent RAM | 7 |
| horizon / focus | 1 / 0.70 |
| pdTarget | 18 |
| headStart | **1** |
| parFlat | 5 |
| slag / patchDrop | 0.19 / **0.24** |
| Job tiers | 1, 2, 2 |
| Target kitted win rate | ~67% |

## The first difficulty wall

Three things change together: the grid grows, `headStart` arrives, and the patch drop rate falls by a third.

**headStart 1** means the intrusion arrives with one junction already aligned along its route. The board generator compensates the opponent's target cost by `round(headStart * 1.8 * 0.6)`, so this is a real head start rather than a cosmetic one.

Target win rate drops 26 points from day 2, the sharpest fall in the arc. Day 3 is where a player who has been coasting notices.

The sim's canonical build begins cycling attack and defend mode pairs from day 3 (`MODE_PAIRS`), which is roughly when a real player has their first config [[augments|augment]].

## See also

- [[day-4]] · [[the-board]]
