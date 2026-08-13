---
title: Split boards
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[built-and-power]]", "[[territory-and-claiming]]", "[[the-duel]]"]
---

# Split boards

> [!info] Source
> `duel-types.ts:DuelState.boards`, `duel-power.ts`. Landed on branch `split-boards`, 2026-08-04.

Each side owns a grid. `DuelState.boards` is a `Record<Side, Board>` where `Side = "player" | "opp"`. Yours is `boards.player`, the intrusion's is `boards.opp`.

**The enemy is never on your board.** Only its traps and its redirects reach in. You defend against those, not against ground.

## Why this replaced the shared board

The old model had one grid that both sides flooded and claimed, and claimed ground was impassable to the other signal. That made defence mean occupation: hold territory, deny approaches. It did not play well. Holding ground is not an interesting decision, and it turned the back half of a duel into a stalemate about position rather than a race.

Splitting the boards keeps the race and rebuilds defence around interference. Full record in [[territory-and-claiming]].

## Board geometry

```
Board { w, h, cells, entry, goal, power }
```

- **Entry** is one cell, left edge, mid row. It is the signal source.
- **Goal** is three cells, right edge, mid row plus and minus one. Lighting any one ends the dive.
- The player's board faces east, the opponent's faces west.

> [!warning] The goal is three cells on purpose
> One redirect can never hard-block a single goal cell into unreachability. Three terminals means interference can slow the approach but cannot wall it.

The goal is also a **sink** in `computePower`: signal arrives and stops rather than conducting onward. Without that, one contact would light the entire goal column.

## Which board a verb touches

Fixed by the verb, never by the payload. This is the rule that keeps the split model from becoming a source of targeting bugs:

| Verb | Board |
|---|---|
| rotate | your own |
| place a [[patch-pieces|patch piece]] | your own |
| [[attack]] (any mode) | theirs |
| [[defend]] (any mode) | your own |

`targetBoardOf` in the reducer derives the board from the action kind. **No `DuelAction` carries a board tag.** A payload cannot lie about which grid it means because it is never asked.

## What `view` is, and is not

`DuelState.view: Side` is which board the viewport is showing. It is presentation only. No rule reads it. Casting ATTACK while looking at your own board still hits theirs.

## What died with territory

Two win conditions, both gone from `DuelEndKind`:

- **SEVERED** - being walled off. On a board only you occupy, this cannot happen to you.
- **Gridlock** - the mutual-stall outcome.

Removing them also deleted a bug class: a planner blindspot that reported `Infinity` used to end still-winnable dives in an instant loss. See [[win-conditions]].

`gridlockWin` is still carried in `run-reducer.ts` and persisted in `save.ts`, and a `gridlockChip` teaching waiver still describes it. That is vestigial. Noted in [[20-mechanics]].

## See also

- [[built-and-power]] - the two layers each board tracks
- [[the-board]] - how a board is generated and made fair
- [[reach-and-placement]] - what you may touch on your own grid
