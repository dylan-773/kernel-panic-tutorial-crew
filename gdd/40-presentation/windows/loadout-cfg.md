---
title: LOADOUT.CFG
status: canon
source: code
owner: ux-agent
updated: 2026-08-05
related: ["[[the-kit]]", "[[ui-rulings]]", "[[ruling-14-loadout-palette]]"]
---

# LOADOUT.CFG

`loadout` · `windows/loadout.tsx` · demo `ui-demos/loadout-eva/`

The kit. **The v3 reference implementation**, and the panel every other surface is built against.

## What it shows

- **Program tiers** with live RANGE and WIDTH numbers.
- **Attack and defend mode buttons**, locked until the matching config [[augments|augment]] is drafted.
- **[[boost-bays|Boost bays]]**.
- **The [[the-pouch|pouch]]**.

See [[the-kit]] and [[player-skills]].

## Optional, always

> [!danger] REVISED IN PROTOTYPE
> Configuring was a **mandatory build stop** between the job board and the dive. Players clicked through it unchanged, so it was a speed bump rather than a decision. It is now a floating window with **its own DIVE button**, so configuring is a choice and diving never waits on it.

## Why this window is the reference

It is the densest surface in the game that is not the dive: three programs, six modes, five bays, five pouch slots and their live numbers, all at once, in both a sparse day-1 state and a full day-9 state.

It landed at **638 to 727px** across every viewport and run state, down from about **1316px**. Meeting the ceiling here proved the ceiling was meetable anywhere. See [[law-3-fluid-and-the-height-ceiling]].

Its glance order uses three hero numerals at ~83px against 19px body, the 2.2x ratio that [[law-2-hierarchy]] now requires of every surface.

## Its status

**Still `awaiting` final approval.** The system it established is settled and is what other panels build to; the panel itself has not been signed off. See [[ui-rulings]].

## The palette question starts here

[[ruling-14-loadout-palette]] granted this window a five-channel state-coded palette and reserved generalization for the user. [[law-1-colour-is-roles]] generalized it anyway. See [[palette-generalization-conflict]].

## See also

- [[law-9-build-recipe]] · [[augments]]
