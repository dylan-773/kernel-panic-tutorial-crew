---
title: Law 8 - The cuts discipline
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[law-3-fluid-and-the-height-ceiling]]"]
---

# Law 8 - The cuts discipline

When a surface exceeds its height budget, cut **in this order**, and record what was cut and why in its `NOTES.md`:

1. **Decorative imagery that cannot survive its size.** Cut it outright rather than shrinking it into noise. See [[law-5-imagery]].
2. **Prose that is taught elsewhere.** Reduce a paragraph to a chip plus its pointer sentence when another surface owns the explanation.
3. **Always-visible descriptions** move to hover, focus or tap popups, **but only if** the control carries a persistent marker that it holds more, such as a dotted underline. **A bare name with a hidden popup is a dead end.**
4. **Box treatment** on the lowest-priority data, keeping the data.
5. **Paging or tabs**, in the narrow tier only.

## The two absolutes

**Never shrink type below its floor.**

**Never add a scrollbar.** No internal scrollbars, ever: reflow, page, or tab.

## The structural lesson

> **A row you do not share is a row you pay for in full.**

Placing a short zone beside a tall one costs nothing. Giving it its own row cost the reference build **112px**, which is a sixth of the entire height budget for one under-filled strip.

This is usually the first thing to check when a panel is over budget, and it is cheaper than any of the five cuts.

## Why an ordered list rather than judgment

Because under pressure the tempting cut is always the wrong one: shrink the type, or add a scrollbar. Both are forbidden, so the list has to say what to do instead, in an order that spends the cheapest thing first.

## See also

- [[law-3-fluid-and-the-height-ceiling]] · [[law-2-hierarchy]]
