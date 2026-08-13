---
title: Law 3 - Fluid and the height ceiling
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[technical-requirements]]", "[[law-8-the-cuts-discipline]]"]
---

# Law 3 - Fluid: container units, one breakpoint, a hard height ceiling

## `cqi`, never `vw`

Every `clamp()` resolves against the window's own `container-type: inline-size`, so a tiled window scales to **its tile**.

A `vw` ramp gives two differently sized windows the same type scale, and is always wrong here.

Three mechanics worth knowing:

- Wrap content in a container element and style a **child**. An element cannot answer its own container query.
- **`cqi` in a custom property resolves at the USE SITE.** A body-size token lands smaller inside a nested container than outside it. This is desirable, since narrow columns get the smaller step, but know it is happening.
- Type floors hold regardless: VT323 body 19 to 21px, Silkscreen labels 9 to 11px. **Never clamp below them to win space.**

## One binary breakpoint at 700px

Of content inline-size. Above it, the full arrangement. Below, a **genuinely different compact arrangement**, not the same layout shrunk.

## The height ceiling

> [!warning] ~700px target, 820px absolute
> A window must fit the shortest desk it claims to support: a 1366x768 screen, which leaves roughly 700px of usable height after the taskbar.

The reference build lands 638 to 727 across every viewport and run state, **down from about 1316** for the window it replaces.

> [!info] This is the whole point of the cycle
> A window that fills the desk cannot be tiled, and untileable windows are what made window management feel rough. The ceiling is not a rendering constraint, it is what makes [[kp-os]] behave like an operating system instead of a stack of full-screen pages.

## Supported viewports

16:9 1366x768, 21:9 2560x1080, and 1280x800 laptop. **All three render the same arrangement.**

**4:3 is not supported.** A narrow tier below 700px may exist as a tiling fallback, but no supported viewport reaches it.

## See also

- [[technical-requirements]] · [[law-8-the-cuts-discipline]]
