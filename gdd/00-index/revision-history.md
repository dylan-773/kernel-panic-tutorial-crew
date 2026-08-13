---
title: Revision history
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[design-change-log]]", "[[home]]"]
---

# Revision history

> [!info] Source
> `git log` in both repos, plus `app/src/game/version.ts`. The build stamp is `APP_VERSION` / `BUILD_DATE`, shown on the title screen so a playtest screenshot can be matched to a build.

## Document lineage

| Version | Date | Form | Note |
|---|---|---|---|
| Final draft | 2026-07-23 | PDF | Pre-prototype. A different game: Unity, real-time then turn-based node placement, eight ability verbs, Neural Capacity, six agents. |
| v2 | 2026-07-25 | PDF + HTML | Rewritten after the prototype shipped. Every section describes what was built and measured. Nine `REVISED IN PROTOTYPE` boxes record what changed and why. |
| Vault | 2026-08-05 | Obsidian | This. Atomized to one idea per note, expanded to full GDD coverage, and corrected to the split-board duel. |

The v2 PDF is a stale render of the v2 HTML: its token table is missing the Tutorial Agent row and totals about 1,218,600 instead of 1,330,600. Renders are archived outside the repo; markdown here is authoritative.

## Build history

Current build **0.7.0**, dated 2026-07-29. `APP_VERSION` bumps when mechanics change, `BUILD_DATE` on every deploy.

| Date | Build | What landed |
|---|---|---|
| 2026-07-18 | - | Dive-system prototype: four signal-routing puzzles, hub, brand assets. |
| 2026-07-24 | - | Rebuilt as the final-GDD game: turn-based race-to-core duel, ten-day run, KP/OS desktop. |
| 2026-07-24 | - | v2 duel: flood-claim board, Dijkstra AI, floating windows. |
| 2026-07-24 | - | v3: telegraphed attacks, DAD.LOG, login with three save slots. |
| 2026-07-24 | - | v4: sfxr synthesis engine, layered mix, generated music beds. See [[music-and-sound]]. |
| 2026-07-24 | - | v5 kit rework: SCAN / ATTACK / DEFEND, augment drafts, cascade RAM, reach 2. The three-program kit dates from here. |
| 2026-07-24 | - | Scripted tutorial with staged program unlocks. |
| 2026-07-26 | - | Par and strain rotation budget, patch cell economy, four new augments. |
| 2026-07-26 | - | Teaching pass: silent coverage gaps fixed, redundant coachmarks retired. |
| 2026-07-28 | 0.6.0 | Deep balance: shaped welded patch pieces, boost bays, darknet, the kitted sim. |
| 2026-07-29 | 0.7.0 | KP/OS v2 single-phosphor shell. |
| 2026-08-01 | 0.7.0 | Ten approved KP/OS v3 instrument panels integrated, then four regressions fixed, then the v2 hues restored to the theme picker. |
| 2026-08-04 | 0.7.0 | `split-boards`: the duel engine rewritten. See [[split-boards]]. |

## Where the current work sits

The checked-out branch is `split-boards`, one commit ahead of `main`, with uncommitted changes across eleven files and two untracked new modules (`duel-clone.ts`, `duel-commands.ts`).

This means the deployed game and the documented game differ. This vault documents the branch, because that is the design going forward. [[territory-and-claiming]] records what `main` still ships.

## See also

- [[design-change-log]] - the nine prototype revisions with the evidence behind each
- [[verification-gate]] - what must pass before any of this deploys
