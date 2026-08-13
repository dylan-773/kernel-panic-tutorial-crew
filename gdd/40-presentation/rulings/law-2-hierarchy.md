---
title: Law 2 - Hierarchy
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[hud-and-ui-design]]"]
---

# Law 2 - Hierarchy

**State the glance order, then build the type scale to enforce it.**

Every surface declares in its `NOTES.md` what the eye hits 1st, 2nd, 3rd, and what is deliberately ambient. That declaration comes **before** the build, not after.

## One focal element per surface, at extreme scale

The reference build uses three hero numerals at ~83px against 19px body: **2.2x** larger than the next biggest thing.

> A surface whose largest element is 1.3x the second largest has no hierarchy.

Annotation clusters at 9 to 11px fill the negative space around the focal element.

Nothing ambient may compete. **Demote it** (unboxed, `--r-note`, smaller) rather than merely moving it.

## The sentence that governs the whole system

> **Maximalism is NOT permission to add. It is extreme contrast between what matters and what does not.**

A dense surface earns its density by having one thing that is unmistakably the point. Density without hierarchy is noise, and the KP/OS look would collapse into it immediately without this law.

## Why it is written down

Because the failure mode is invisible from inside. Every element on a panel feels important to whoever is building it, and the result is five things at 1.3x each. Declaring the order first makes the decision before the attachment forms.

## See also

- [[law-3-fluid-and-the-height-ceiling]] · [[law-8-the-cuts-discipline]]
