---
title: Save and load
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[death-and-run-end]]", "[[title-and-start-screen]]", "[[meta-progression]]"]
---

# Save and load

> [!info] Source
> `game/save.ts`. `SLOT_COUNT = 3`.

## Three slots

Keys `kernel-panic-s<N>-meta-v2` and `kernel-panic-s<N>-run-v3`.

Each slot is a separate player. `MetaState` including `runCount`, `machineOpened` and `taught` is per slot, so a second slot is genuinely fresh and will be taught everything again.

Slots are **deletable from the login screen**. See [[title-and-start-screen]].

## Two objects

| Object | Holds | Lifetime |
|---|---|---|
| `MetaState` | `runCount`, `machineOpened`, `sound`, `music`, `taught`, `stats` | forever |
| `RunState` | credits, augments, tiers, RAM, pieces, bays, strain, day, screen | one run |

See [[meta-progression]], which is unwritten and should not be.

## There are no checkpoints

No mid-run save-scumming, no restore point, no continue. A run either finishes or ends. See [[death-and-run-end]].

## Refresh is a safe abort

> [!info] Transient screens are never resumed into
> Reloading mid-dive puts the player back at the day, not into a half-serialized duel. So closing the tab during a losing dive costs the ticket, never the run, and never corrupts the save.
>
> This is also the only "abandon" affordance in the game, and the ABANDON dialog copy exists to make it explicit rather than a discovered trick.

## The migration ladder

Real, and load-bearing, because saves survive across builds:

- Legacy `patchCells` integer becomes N cross masks.
- `ramPerTurn` NaN is repaired.
- Unknown augment ids are **dropped**, so removing an augment from the catalog does not brick an old save.
- Transient screens are never resumed into.

`run-sim.ts` exercises meta hydration across 40 full runs.

## Two things worth knowing

**localStorage is per port.** A save made against `bun run preview` is not the save made against `dist/server/server.js`. This has confused more than one playtest.

**There is no cloud save and no account.** Clearing site data destroys everything.

## See also

- [[technical-requirements]] · [[scoring-and-lifetime-stats]]
