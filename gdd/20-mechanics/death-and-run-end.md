---
title: Death, lives and run end
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[neural-strain]]", "[[save-and-load]]", "[[reveal-schedule]]"]
---

# Death, lives and run end

> [!info] Source
> `run-reducer.ts` (`runEnd` screen), `save.ts:MetaState`; `story.ts:runEndScene`.

## There are no lives

Deliberately. There is no life counter, no continues, no revives, and no mid-run checkpoint. A run either reaches day 10 or it ends.

## There is no death either

The player never dies. [[neural-strain]] reaching zero severs the connection:

> NEURAL STRAIN: ZERO. CONNECTION SEVERED.

You wake up at the bench. The shop is still there, [[rhea]] is still at the counter, and you start again tomorrow.

## What ends a run

Exactly one thing: **strain reaching 0**, checked after a dive resolves. The flow goes `duelFinished` to `runEnd` rather than to `result`.

Losing a single dive does **not** end the run by itself. A loss bills 0 strain. It costs you the ticket's pay and the day's progress, not the run.

## What survives

`MetaState` persists across runs:

| Field | Meaning |
|---|---|
| `runCount` | how many attempts have been made |
| `machineOpened` | whether the finale has ever been won |
| `taught` | mechanics already explained, so nothing is re-taught |
| `stats` | [[scoring-and-lifetime-stats|lifetime totals]] |
| `sound`, `music` | preferences |

Everything else lives on `RunState` and dies with the run: credits, augments, tiers, RAM, pieces, strain.

## Losing is the story

This is the design's central move. `runCount` drives the [[reveal-schedule]]: each failed run advances [[rhea]]'s erosion and surfaces another fragment of the father. The v2 GDD states it plainly:

> Losing is how the player learns who their father was.

So there is no failure state in the narrative sense. A lost run is a chapter. See [[story-overview]] and [[dad-log-archive]].

## Abandoning

Refreshing mid-dive is a **safe abort**, not a loss. Transient screens are never resumed into. See [[save-and-load]].

## See also

- [[game-progression]] · [[the-ten-day-arc]]
