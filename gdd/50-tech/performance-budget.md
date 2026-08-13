---
title: Performance budget
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[law-7-motion]]", "[[law-6-the-tube]]", "[[law-10-verification]]"]
---

# Performance budget

Measured, not assumed. Every number here came off the reference build.

## The measurement that set the law

| Approach | p95 frame time |
|---|---|
| baseline | 9ms |
| animating `background` / `box-shadow` inside a filtered subtree | **50ms** |
| the identical effect via `opacity` cross-fade on a promoted layer | **9.3ms** |

The promoted version uses `will-change` plus a `mix-blend-mode: difference` plate to get the inverse flip.

**Animate compositor properties, not paint properties.** See [[law-7-motion]].

## Why paint is so expensive here

The whole stage sits under CRT glass layers. A paint-property animation inside a filtered subtree re-runs the filter over the affected area every frame. The cost is not the animation, it is the filter it drags along.

## The same fact killed CURVED

Barrel distortion via `feDisplacementMap` was built, measured and cut. Every repaint inside a displaced subtree re-ran the warp **over the whole stage**, which cost the feed roll, the REC blink, the terminal cursor and the clock's seconds.

And it read the same as flat. So the cost bought nothing. See [[law-6-the-tube]].

## The harness

Sample `requestAnimationFrame` deltas over **400+ frames**, report mean, p50, p95 and worst, per CRT mode. Driven from headless Chrome over CDP. See [[law-10-verification]].

## The AI's budget

Different problem, same discipline. `sim.ts` carries `BEAT_MS = 255` as a blended proxy for opponent thinking time and reports `ai seconds` per day, which is what makes a smarter [[difficulty-dials|horizon]] a cost as well as a difficulty change. See [[opponent-ai]].

## See also

- [[law-7-motion]] · [[technical-requirements]]
