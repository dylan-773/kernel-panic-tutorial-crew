---
title: Law 7 - Motion
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[law-1-colour-is-roles]]", "[[law-6-the-tube]]"]
---

# Law 7 - Motion, and the performance law that governs it

- **`steps()` timing only.** No eased curves.
- **Reduced motion collapses to the final state in one frame**, with sound unaffected.
- **Load choreography:** stagger meters, count up hero numerals, type descriptions, slot in chips. Scope typewriters **per element** so interacting with one does not restart the others.

## Motion is reserved

> [!warning] Ambient chrome never animates
> Animation means **something is happening or something is wrong**.

This is the other half of [[law-1-colour-is-roles]]'s alarm rule. Static red shapes train the eye to stop sampling red; motion is the one channel the chrome does not have, and it only works because it is never spent on decoration.

## Animate compositor properties, not paint properties

Measured on the reference build:

| Approach | p95 frame time |
|---|---|
| animating `background` / `box-shadow` inside a filtered subtree | **50ms** |
| the identical effect via an `opacity` cross-fade on a promoted layer | **9.3ms** |
| baseline | 9ms |

The promoted-layer version uses `will-change` plus a `mix-blend-mode: difference` plate to get the inverse flip.

Prefer `opacity` and `transform`.

> **Measure; do not assume.** The frame harness is in [[law-10-verification]].

## Why this law has teeth

It killed CURVED. See [[law-6-the-tube]]. A visual idea that measured badly was cut rather than optimized, because the cost was structural rather than incidental.

## See also

- [[performance-budget]] · [[music-and-sound]]
