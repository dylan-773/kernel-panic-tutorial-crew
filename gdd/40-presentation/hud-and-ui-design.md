---
title: HUD and UI design
status: canon
source: rulings
owner: orchestrator
updated: 2026-08-05
related: ["[[kp-os]]", "[[law-2-hierarchy]]", "[[dive-exe]]"]
---

# HUD and UI design

There is no HUD in the usual sense. There is a desktop of windows, and one full-screen surface with instrumentation around the board.

## The method: glance order first

> [!info] The rule that produces everything else
> **Every surface declares, before it is built, what the eye hits 1st, 2nd, 3rd, and what is deliberately ambient.** Then the type scale is built to enforce that order.
>
> One focal element per surface, at extreme scale. The reference build uses ~83px hero numerals against 19px body: **2.2x** the next biggest thing. A surface whose largest element is 1.3x the second largest has no hierarchy.

See [[law-2-hierarchy]].

## The vocabulary

Consistent across every window (see [[law-4-chrome-vocabulary]]):

- Solid-ink title bar, void pixel text, a pixel X as the only button.
- Boxed `// LABEL _` data rows.
- VT323 body at 19 to 21px, Silkscreen labels at 9 to 11px.
- **No border-radius on UI chrome, ever.**
- Hairline borders with heavy corner brackets, **scoped to focal panels only**.
- Hazard-stripe dividers marking zone boundaries.
- Corner-tick reticles marking the active option.
- **Equal-footprint empty states**: an empty slot occupies exactly the room a filled one does.

## In-dive instrumentation

[[dive-exe]] shows RAM, par, round, the YOU / INTRUSION turn pair, the threat banner, and the machine's telegraphed aim. It is full-screen and does not follow the window rules.

The telegraph is the single most important element on the surface: it is what makes every threat answerable. See [[traps-and-telegraphs]] and [[design-pillars]].

## Risk is never colour alone

`--r-warn` appears on exactly one thing per surface, the alarm. And colour is never the only channel: an alarm must **also** flood inverse video and **move**.

Ambient chrome must never move. That asymmetry is the mechanism: static red shapes train the eye to stop sampling red, so motion is the one channel the chrome does not have. See [[law-1-colour-is-roles]] and [[law-7-motion]].

## Density discipline

No internal scrollbars, ever. When a surface exceeds its budget it cuts in a fixed order rather than shrinking or scrolling. See [[law-8-the-cuts-discipline]].

## See also

- [[player-metrics]] - the numbers being displayed
- [[teaching-system]] - tier 0 is "make the UI say it"
