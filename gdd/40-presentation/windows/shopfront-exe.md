---
title: SHOPFRONT.EXE
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[cutscenes-and-scenes]]", "[[night-sys]]", "[[backroom-lck]]"]
---

# SHOPFRONT.EXE

`flow` · inline in `shop-os.tsx` plus `windows/night.tsx`

**The flow window.** The only window whose title changes with its contents, via `windowTitle()`.

## What it fronts

| Screen | Title |
|---|---|
| `opener`, `runEnd`, `finaleWin` | SHOPFRONT.EXE |
| `tutIntro`, `tutOutro` | the tutorial framing |
| `dayOpen` | MORNING.LOG |
| `upgrade` | NIGHT.SYS - see [[night-sys]] |
| `finalePre` | BACKROOM.LCK - see [[backroom-lck]] |

## Why one window and not five

Because they are the same object at different times of day: the story surface. A separate window per story state would put five icons on the desktop for one thing that is never open twice at once.

Retitling instead is also characterful. An operating system whose windows rename themselves as the day progresses is doing the fiction's work.

## What plays here

Every scene: openers, enders, day opens, the tutorial framing, the finale win. There is **no separate cutscene mode and no full-screen takeover**. A scene is a window with text in it, on the same desktop as everything else. See [[cutscenes-and-scenes]].

Speakers render with portraits (`sister.png`, `father.png`, `companion.png`) and stills (`still-locked`, `still-bench`, `still-counter`, `still-open`).

## On a fresh save

Auto-opens. It is the only window that opens itself, because on run 1 it is the only one with anything to say.

## See also

- [[kp-os]] · [[rhea]] · [[reveal-schedule]]
