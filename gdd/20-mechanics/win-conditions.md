---
title: Win conditions
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-round-cap]]", "[[split-boards]]", "[[territory-and-claiming]]"]
---

# Win conditions

> [!info] Source
> `duel-types.ts:DuelEndKind`, `duel-actions.ts:finishDuel`.

Three outcomes. That is the complete list.

```ts
type DuelEndKind = "goal" | "cap" | "seal";
```

## goal

A side's **live** signal touches any of its three goal cells. `goalLive(b)` asks whether any goal index is currently in `b.power`.

Note "live", not "built". A goal contact that gets cut before the settle completes does not count, because power is recomputed wholesale on every change. See [[built-and-power]].

In the tutorial this is inverted: the player reaching the goal triggers an `opp` win with kind `seal`. See [[the-tutorial]].

## cap

The [[the-round-cap|round cap]] at 25 rounds. Tiebreak on [[route-cost-and-par|route cost]]: `playerCloser = pd <= od`. Ties go to the player.

A cap win is a **messy win**. It costs 10 extra [[neural-strain]] and pays half the ticket, or 75% with [[overtime-clause]].

## seal

Tutorial only. The scripted close: the lesson completes plus one round, or `round >= 7`, whichever comes first.

## What was removed

> [!warning] SEVERED and gridlock no longer exist
> Both are gone from `DuelEndKind`. On a board only you occupy, being walled off is not a thing that can happen to you, so SEVERED had no meaning left. Gridlock went with it.
>
> This also deleted a bug class. A planner blindspot that reported `Infinity` for a route that actually existed used to end still-winnable dives in an instant loss. With no loss condition reading the planner's failure, that defect has nowhere to land.

Vestigial remains: `gridlockWin` is still carried through `RunAction.duelFinished`, still persisted on `lastResult` in `save.ts`, and a `gridlockChip` teaching waiver still describes it. Both sims hardcode it to `false`.

## `endReason`

A player-facing sentence, set at finish and **never cleared**.

It exists because the result overlay has to explain a loss the machine won without ever touching your core, and a 2.4 second toast cannot carry that line. So the reason survives on state and the overlay reads it. See [[repair-log]].

## The strain bill

Only a win is billed. A loss chips 0, because the run is ending anyway. Formula in [[route-cost-and-par]].

## See also

- [[death-and-run-end]] - what happens when strain reaches zero
- [[job-pay-and-billing]] - what each outcome pays
