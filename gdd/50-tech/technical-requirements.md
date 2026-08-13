---
title: Technical requirements
status: canon
source: rulings
owner: orchestrator
updated: 2026-08-05
related: ["[[law-3-fluid-and-the-height-ceiling]]", "[[game-controls]]", "[[performance-budget]]"]
---

# Technical requirements

## Platform

**Desktop browser.** No download, no install, no account.

## Supported viewports

| Viewport | Ratio |
|---|---|
| 1366x768 | 16:9 |
| 2560x1080 | 21:9 |
| 1280x800 | laptop |

**All three render the same arrangement.**

> [!warning] 4:3 is explicitly not supported
> A narrow tier below 700px content inline-size may exist as a tiling fallback, but no supported viewport reaches it. See [[law-3-fluid-and-the-height-ceiling]].

The binding constraint is **height**: 1366x768 leaves roughly 700px of usable height after the taskbar, and every window must fit it.

## Input

**Mouse only.** No keyboard scheme, no gamepad. See [[game-controls]].

Touch is unaddressed. `touch-safe-tooltips` is a logged ui-spec, so it has been noticed but not designed.

## Audio

Web Audio, created lazily on the **first user gesture** for autoplay unlock. Importing the audio module is SSR-safe. Music beds are mp3 fetched from `/assets/sfx/music/`. See [[music-and-sound]].

## Storage

`localStorage`, three slots, keys `kernel-panic-s<N>-meta-v2` and `-run-v3`. No server, no cloud save, no account. Clearing site data destroys every run. See [[save-and-load]].

## Performance

Frame budget and the measurements behind it in [[performance-budget]].

## Open questions

- [ ] Is mobile or touch a target at all? The height ceiling and mouse-only input both currently say no.
- [ ] Minimum browser versions are undocumented. The code uses container queries (`cqi`), `color-mix` and `mix-blend-mode`, which sets a real floor.

## See also

- [[technology-stack]] · [[player-options]]
