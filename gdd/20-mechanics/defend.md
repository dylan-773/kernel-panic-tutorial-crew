---
title: DEFEND
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[purge]]", "[[lock]]", "[[ward]]"]
---

# DEFEND

> [!info] Source
> `kit.ts:DEFEND_WIDTH`, `defendModeDesc`.

Acts on **your own** board. 1 RAM, once per turn.

Width by tier: 1, 2, 3 targets per cast. See [[program-tiers]].

## Modes

| Mode | Unlocked by | What it does |
|---|---|---|
| [[purge]] | default | Disarms revealed traps |
| [[lock]] | [[clamp-driver]] | Freezes junctions for 2 rounds |
| [[ward]] | [[ward-driver]] | Area denial against traps and redirects |

## What defence means now

> [!warning] Defence is not holding ground
> Under the old shared-board model, defending meant occupying territory to deny approaches. With [[split-boards]] the enemy is never on your board. Defence is entirely **anti-trap and anti-redirect**.
>
> This is the design intent behind the whole rewrite. See [[territory-and-claiming]].

So the three modes map cleanly onto the three things that can be done to you:

- a trap already planted, revealed by [[scan]] and removed by [[purge]];
- a junction about to be twisted, frozen by [[lock]];
- an area you cannot watch, sealed by [[ward]].

## See also

- [[the-kit]] · [[traps-and-telegraphs]]
