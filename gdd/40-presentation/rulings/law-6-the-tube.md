---
title: Law 6 - The tube
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[player-options]]", "[[law-7-motion]]"]
---

# Law 6 - The tube

The CRT is **a set of glass layers over the stage**, not a filter on the UI.

## Six layers

1. Phosphor scanlines - a bright line and a dark gap, not a faint tint
2. A vertical aperture grille
3. Ink-tinted bloom
4. A specular reflection
5. An elliptical falloff
6. A bezel lip

Rendered by `Glass()` as `g-scan`, `g-mask`, `g-bloom`, `g-spec`, `g-vig`, `g-bezel`.

## Two modes

**FLAT** (default) and **OFF**.

OFF **removes every layer outright** rather than fading them, and the surface must still read as a finished flat-ink print.

> [!info] None of a surface's richness may live in the CRT layer
> This is the real content of the law. The glass is allowed to be atmosphere and nothing else. If a panel only looks designed with the tube on, the panel is not designed.

## CURVED is dead. Do not rebuild it.

> [!warning] Built, measured and cut
> Real barrel distortion via `feDisplacementMap` **read the same as flat**, bowed the taskbar, and cost the feed roll, the REC blink, the terminal cursor and the clock's seconds.
>
> The cause: every repaint inside a displaced subtree re-runs the warp over the whole stage. So the price was not the curve, it was every animation on the page.
>
> The maps and wiring are in git if anyone revisits it.

This is the clearest case in the project of the [[law-7-motion|performance law]] deciding a visual question.

## See also

- [[law-7-motion]] · [[player-options]]
