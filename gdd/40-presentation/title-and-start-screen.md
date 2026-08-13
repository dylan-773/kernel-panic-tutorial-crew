---
title: Title and start screen
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[kp-os]]", "[[save-and-load]]", "[[game-flowchart]]"]
---

# Title and start screen

> [!info] Source
> `components/os/boot.tsx`, `login.tsx`; `game/version.ts`.

There is no title screen. There is a **boot sequence**.

## BIOS boot

The machine posts. Boot lines scroll. This is the game's first statement of its own thesis: before you are a player you are someone switching on a terminal.

Boot line 1 ships **name-free**, per a loremaster gate. [[ruling-08-names]] applies even here.

## The build stamp

`VERSION_LABEL` from `version.ts` is shown on the title surface: `0.7.0 (2026-07-29)`.

> [!info] Why the date is on screen
> From the source comment: playtest notes are written against whatever was live that day, and a screenshot of a fixed bug is indistinguishable from a screenshot of a stale build. The date is there so a report can be matched to a build without digging through git.

`BUILD_DATE` bumps on every deploy; `APP_VERSION` when mechanics change.

## Login

Three save slots. Each is a separate save; each can be **deleted** from the login screen.

Slots are the game's only profile system. `MetaState` including `runCount`, `machineOpened` and `taught` is per slot, so a second slot is a genuinely fresh player who will be taught everything again. See [[save-and-load]].

## Then the desktop

Login leads to the KP/OS desktop, and on a fresh save the shopfront window auto-opens. See [[kp-os]] and [[game-flowchart]].

## See also

- [[player-options]] · [[technical-requirements]]
