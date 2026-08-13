---
title: Scoring and lifetime stats
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[ledger-log]]", "[[meta-progression]]", "[[save-and-load]]"]
---

# Scoring and lifetime stats

> [!info] Source
> `save.ts:MetaState.stats` (`LifetimeStats`). Window: [[ledger-log]].

There is no score. Nothing ranks the player and nothing is optimized for points.

What exists instead is an **accounting record**: `LifetimeStats` on `MetaState`, persisted per save slot, surviving every run.

## Presentation

[[ledger-log]] renders it as an accounting terminal:

- **THIS RUN** against **LIFETIME**.
- **CREDITS** as the hero number.
- **MOST LETHAL** customer dossier, the client whose device has ended the most runs.
- Print furniture: the window is styled as a ledger printout.

## Why stats and not score

The fiction does the work. A repair shop keeps books; it does not keep a high score. Framing the record as accounting makes the number diegetic, which is the same move as [[repair-log]] reading a dive result as a transaction.

MOST LETHAL is the one stat that behaves like a boss meter, and it is emergent rather than authored: whichever [[customers|customer]] the player keeps failing becomes their nemesis without the game ever designating one.

## See also

- [[ledger-log]] · [[death-and-run-end]]
