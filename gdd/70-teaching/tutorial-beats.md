---
title: Tutorial beats
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[the-tutorial]]", "[[teaching-system]]", "[[the-board]]"]
---

# Tutorial beats

> [!info] Source
> `content/teaching.ts:TUTORIAL_BEATS`. Ten beats, ordered. The **first passing `test(ctx)` wins**.

| # | id | Teaches |
|---|---|---|
| 1 | `watch-it-move` | the opponent exists and moves |
| 2 | `holding-back` | it is not attacking yet |
| 3 | `no-longer-holding` | now it is |
| 4 | `first-rotation` | **rotate** |
| 5 | `chain-toward-core` | routing toward the goal |
| 6 | `scan-it` | **scan** |
| 7 | `purge-it` | **defend** |
| 8 | `purge-waiting` | purge needs a revealed trap |
| 9 | `attack-it` | **attack** |
| 10 | `whole-toolbox` | all three, one turn |

Beats are how the tutorial teaches, because coachmarks are gated off day 0 by `notBeforeDay: 1`. See [[teaching-system]].

## The bound that broke, and why it is documented

> [!warning] `first-rotation` tests `ownedNodes <= 3` and must stay in sync with `MAX_OPENING_BUILT`
> When the two drifted apart, **23.9% of opening dives never taught rotation at all.**
>
> The beat's trigger assumes the opening power lights at most 3 nodes. The board generator guarantees that via `MAX_OPENING_BUILT`. Change the generator bound without changing the beat and roughly a quarter of new players are never taught the game's only movement verb, silently, with no error anywhere.

See [[the-board]].

This is the single most instructive bug in the project's history: two correct-looking constants in different files, a failure that is invisible in any individual playthrough, and a percentage that only exists because someone simulated it.

## The ladder must never go silent

`teach-sim.ts` asserts the tutorial ladder is never silent in a reachable state. If the player can arrive somewhere with no beat willing to fire, the build fails.

## Line limit

`MAX_BEAT_LINE = 260` characters, against 160 for a coachmark. A beat has more room because it is the only thing on screen and the player is not mid-decision.

## See also

- [[the-tutorial]] · [[mechanic-coverage]]
