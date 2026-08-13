---
title: Cutscenes and scenes
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[reveal-schedule]]", "[[shopfront-exe]]", "[[narrative-director]]"]
---

# Cutscenes and scenes

> [!info] Source
> `content/story.ts`, 924 lines. Scenes are **functions**, not a table.

```ts
StoryBeat { speaker: "sister"|"father"|"system"|"companion",
            name?, portrait?, still?, lines: string[] }
Scene     { id, beats }
```

## The scene functions

| Function | Scene id | When |
|---|---|---|
| `runOpenerScene(runCount)` | `run-open-<n>` | start of every run |
| `runEndScene(runCount)` | `run-end-<n>` | when a run ends |
| `dayOpenScene(day)` | per day | each morning |
| `tutorialIntroScene()` | `tutorial-intro` | run 1 only |
| `tutorialOutroScene()` | `tutorial-outro` | run 1 only |
| `finaleWinScene()` | `finale-win` | on opening the machine |

Plus `DAY_LINES`, nine morning one-liners. See the individual day notes, [[day-1]] onward.

## Four speakers

- **sister** - [[rhea]], `sister.png`
- **father** - [[dad]], `father.png`, fragments only
- **system** - the terminal voice, short caps declaratives
- **companion** - [[patch]], **finale only**

> [!warning] The companion speaker may not appear before the finale
> Before it, no content may confirm the occupant speaks at all. See [[reveal-schedule]], prohibition 5.

## Stills

`still-locked.png`, `still-bench.png`, `still-counter.png`, `still-open.png`. Four states of the same shop, and the sequence locked to open is the whole arc in four images.

## Bespoke, then fallback

- Openers: bespoke runs 1 to 6, then a three-scene cycle (coffee, "so does my theory", the dream).
- Enders: bespoke runs 1 to 8, carrying sectors 1 to 7 on runs 2 to 8. Runs 9+ alternate "SECTOR SCAN: NO NEW DATA" echoing sector 1 on odd runs and sector 4 on even runs.

`run-sim.ts` asserts openers and enders exist for run numbers **1 through 12**, so the fallbacks are covered by test rather than by hope.

## Where they play

All of them in the flow window, [[shopfront-exe]], which changes its own title per screen. There is no separate cutscene mode and no full-screen takeover: a scene is a window with text in it, on the same desktop as everything else.

## Owned by

The [[narrative-director]] writes them; the [[loremaster]] gates them against [[reveal-schedule]].

## See also

- [[dad-log-archive]] - the other delivery channel
