---
title: Mechanics
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[home]]", "[[the-duel]]", "[[economy]]"]
---

# Mechanics

Everything the player does, read out of the engine rather than out of the old design doc.

> [!warning] This area was rewritten on 2026-08-05
> The duel was rebuilt on branch `split-boards`. Notes here describe that engine. Anything you remember about territory, claiming, SEVERED or gridlock is [[territory-and-claiming]] now.

## The duel

The combat system. One dive is one duel.

| Note | What it covers |
|---|---|
| [[the-duel]] | The overview. Read this first. |
| [[split-boards]] | Two grids, one per side. The central structural fact. |
| [[built-and-power]] | Permanent construction versus cuttable throughput. |
| [[the-board]] | Cells, junctions, piece distribution, generation and fairness. |
| [[rotation]] | The only movement verb, and why it only turns one way. |
| [[reach-and-placement]] | What you are allowed to touch. |
| [[route-cost-and-par]] | The Dijkstra metric that prices everything. |
| [[cascades-and-surge]] | The signature payoff, and the three surge tiers. |
| [[traps-and-telegraphs]] | Halt, siphon, and the one-beat tell. |
| [[win-conditions]] | Goal, cap, seal. |
| [[the-round-cap]] | The 25-round tiebreak. |
| [[turn-structure]] | Turn order, the command gate, the one undo. |
| [[opponent-ai]] | Stances, cut scoring, replanning. |
| [[difficulty-dials]] | `horizon`, `focus`, `greed`, and which are load-bearing. |

## The kit

Three programs, always present, 1 RAM each, once per turn each. Depth lives in modes and tiers, not in count.

[[the-kit]] · [[scan]] · [[attack]] · [[defend]] · [[program-tiers]]

Modes: [[redirect]] · [[arm-halt]] · [[arm-siphon]] · [[purge]] · [[lock]] · [[ward]]

## Augments

Eighteen. Four configs unlock modes, fourteen boosts modify rules.

[[augments]] · [[augment-drafts]] · [[boost-bays]]

## The player

[[player-character]] · [[player-skills]] · [[player-metrics]] · [[player-inventory]] · [[death-and-run-end]]

Resources: [[ram]] · [[neural-strain]] · [[credits]] · [[patch-pieces]] · [[the-pouch]]

## Economy

[[economy]] · [[job-pay-and-billing]] · [[the-night-shop]] · [[the-darknet]] · [[scoring-and-lifetime-stats]] · [[meta-progression]]

## Known drift

Three places where shipped copy disagrees with shipped rules. Recorded, not patched, because this vault does not edit the game.

| Where | Says | Actually |
|---|---|---|
| `teaching.ts` coachmark `patch-cell-use` | placing a piece costs 2 RAM | `PLACE_COST = 4` (`patch-cells.ts`) |
| `teaching.ts` coachmark `cascade-bank` | pays from four nodes | `cascadeRam` pays from three (`kit.ts`) |
| `run-reducer.ts`, `save.ts` | `gridlockWin` is carried and persisted | `DuelEndKind` has no gridlock case; both sims hardcode `false` |
| `kit.ts:142` (`scanDesc`), `kit.ts:221` ([[long-arms]]) | "within N of **your territory**" | there is no territory. It means built ground. Also in the comments at `kit.ts:16` and `kit.ts:51` |

That last one is **player-facing copy in two places**: the SCAN description and the LONG ARMS augment card, both rendered in [[manual-txt]] and [[loadout-cfg]]. It is the deleted model's vocabulary still on screen. The accurate word is "built ground" or "your line". See [[built-and-power]].
