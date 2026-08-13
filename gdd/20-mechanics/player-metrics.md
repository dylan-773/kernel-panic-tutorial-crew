---
title: Player metrics
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[ram]]", "[[neural-strain]]", "[[route-cost-and-par]]"]
---

# Player metrics

Every number attached to the player, and where it lives.

## Per turn

| Metric | Range | Source |
|---|---|---|
| [[ram]] | 5 to 9 base, plus carry and banks | `ramPerTurn`, `carry`, `drainNext` |
| carry | 0 to 2 | `carryCap = 2` |
| [[reach-and-placement|reach]] | 2, or 4 with [[long-arms]] | `reachOf` |

## Per dive

| Metric | Meaning |
|---|---|
| `rotations` | manual twists, the [[route-cost-and-par|par]] meter |
| `par` | the budget, fixed at generation |
| `trapsFired` | enemy traps sprung on you |
| `redirectsTaken` | enemy twists landed on your board |
| `pressureRounds` | rounds the machine was within 4 of its goal |
| `attacksCast`, `scansCast`, `defendsCast` | cast counters; only `attacksCast` drives a rule |
| `strainChip` | the bill, computed at finish |

## Per run

| Metric | Range |
|---|---|
| [[neural-strain]] | 100 to 0 |
| [[credits]] | unbounded |
| day | 1 to 10 |
| program tiers | 1 to 3 each |
| [[boost-bays]] | 3 to 5 |
| pouch | 0 to 5 [[patch-pieces|pieces]] |

## Lifetime

`runCount`, `machineOpened`, `taught`, `stats`. See [[scoring-and-lifetime-stats]].

## Which are shown, and where

The dive HUD shows RAM, par, round and the [[traps-and-telegraphs|telegraph]]. [[repair-log]] shows the strain trace with sparklines and a dive log. [[ledger-log]] shows lifetime.

Three of these carry persistent hover tips rather than one-time coachmarks, because they are reference the player wants repeatedly: `par`, `strain`, `ram`. See [[teaching-tips]].

## See also

- [[player-skills]] · [[player-inventory]]
