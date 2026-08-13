---
title: Design change log
status: canon
source: lore
owner: orchestrator
updated: 2026-08-05
related: ["[[revision-history]]", "[[territory-and-claiming]]"]
---

# Design change log

Every entry is a design that was replaced, with the evidence that forced it. The v2 GDD carried nine of these as `REVISED IN PROTOTYPE` boxes; the tenth is the split-board rewrite.

This is the most reusable page in the vault. Each entry is a mistake already paid for.

## 1. Mandatory build stop, cut

> [!danger] REVISED IN PROTOTYPE
> The draft made kit configuration a required screen between the job board and the dive. It became a speed bump: players clicked through it unchanged. It is now an optional floating window ([[loadout-cfg]]) with its own dive button, so configuring is a choice and diving is never gated on it.

Random augment unlock also became a curated draft of three. See [[augment-drafts]].

## 2. Draw-bag placement, replaced by rotation

> [!danger] REVISED IN PROTOTYPE
> The draft dealt pieces from a bag and had the player place them. Placement made every board a fresh puzzle with no read-ahead. The shipped duel pre-deals a scrambled grid and gives the player exactly one verb on it: rotate. See [[rotation]].

## 3. Neural Capacity, cut

> [!danger] REVISED IN PROTOTYPE
> Two resources competing for the same decision. Neural Capacity was removed entirely and [[patch-pieces]] took the slot, because a consumable that changes the board reads more clearly than a second abstract meter. Surviving resources: [[neural-strain]], [[ram]], [[credits]], [[patch-pieces]].

## 4. Eight verbs and about twenty-four variants, replaced by three programs

> [!danger] REVISED IN PROTOTYPE
> The largest single change. The draft's ability catalog was unreadable at speed. The shipped kit is exactly three programs, always present, always 1 RAM, once per turn each: [[scan]], [[attack]], [[defend]]. Depth moved into modes and tiers rather than count. See [[the-kit]].

## 5. Immediate cascade RAM, replaced by banking

> [!danger] REVISED IN PROTOTYPE
> Paying cascade RAM inside the turn that earned it collapsed duels to about 1.5 rounds across a 200-seed sweep: one good chain ended the game. Cascade RAM now banks into the following turn. See [[cascades-and-surge]].

## 6. Tier-0 tutorial config, lost its first playtest

> [!danger] REVISED IN PROTOTYPE
> Teaching by a weakened opponent did not read as teaching, it read as a bad fight. The shipped tutorial boots programs OFFLINE and unlocks them by lesson beat, and makes unwinnability structural rather than statistical: touching the core slams every port. See [[the-tutorial]].

## 7. Unity, cut

> [!danger] REVISED IN PROTOTYPE
> Along with the purchased asset packs. The game ships as a browser app. See [[technology-stack]].

## 8. The agent pipeline stopped being a proposal

> [!danger] REVISED IN PROTOTYPE
> Every loop in the crew architecture was executed by hand at least once during the build before it was written down as a system. See [[the-dev-crew]].

## 9. Determinism became load-bearing

> [!danger] REVISED IN PROTOTYPE
> Seeded generation was originally a convenience. It became the thing that makes balance claims checkable at all: 200 seeds a day, paired kitted and kit-less passes, and a tutorial that must post zero wins. See [[determinism-and-seeds]].

## 10. Territory and claiming, cut (2026-08-04)

> [!danger] REVISED IN PROTOTYPE
> The shared board made defence mean holding ground, and holding ground is not interesting to play. Each side now owns a grid. Progress splits into two layers: `built` is permanent, `power` is cuttable. Defence now means anti-trap and anti-redirect rather than occupation.
>
> Two win conditions died with it: `SEVERED` and gridlock. Removing them also killed a bug class where an `Infinity` blindspot in the planner lost dives that were still winnable.

See [[split-boards]] for the current model and [[territory-and-claiming]] for the full record of what was removed.

## Still open

- [[meta-progression]] - the draft said unlocked abilities persist across runs while currency resets. v2 removed the mechanic and never replaced the statement, so no document currently says what carries between runs beyond story progress.
- [[palette-generalization-conflict]] - canon ruling 14 scoped multi-hue to one window and reserved generalization for the user; the UI spec generalized it anyway.
