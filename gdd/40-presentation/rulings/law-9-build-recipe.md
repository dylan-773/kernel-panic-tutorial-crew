---
title: Law 9 - Build recipe for a panel
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[the-plays]]", "[[ux-agent]]"]
---

# Law 9 - Build recipe for a panel

Panels are independent and can be built in parallel. For one panel:

1. **Read the reference.** `loadout-eva/index.html` and its `NOTES.md`. Copy the role token block, the glass layers, the rig and the load-choreography helpers **verbatim**. Do not re-derive them.
2. **Read the shipped component** in `app/src/components/os/windows/` for **structure and state flow only**. Its look is the thing being replaced.
3. **Import real numbers and copy** from `app/src/game/`. Transcribe constants rather than inventing them, **so the study cannot drift from the game**.
4. **Write the glance order FIRST**, then build the type scale to enforce it. See [[law-2-hierarchy]].
5. **Build at least two run states**, one full and one sparse. See [[law-4-chrome-vocabulary]].
6. **Build to the 700px height target and measure it.** See [[law-3-fluid-and-the-height-ceiling]].
7. **Standalone page** at `ui-demos/<id>/index.html`, linking `../_shared/kp.css` and `../_shared/system.css`, art under `<id>/art/`, everything else inlined. **Vanilla JS, no framework.**
8. **Register** in `ui-demos/manifest.json` at `"status": "awaiting"` with the variation rows (SCHEME, CRT, VIEWPORT, RUN STATE, plus whatever the surface needs), and write `<id>/NOTES.md`: what it is, what it decides, what it cuts, what it still owes.

## Two standing prohibitions

- **Game copy carries no em or en dashes.** See [[voice-and-copy-laws]].
- **Never write to `kernel-panic-site/`.** Only the Orchestrator integrates. See [[the-plays]].

## Why step 3 exists

A demo that invents its own numbers is a picture of a game rather than a study of this one. Transcribing from `src/game/` means a study that contradicts the build is a visible bug rather than an invisible drift.

## See also

- [[law-10-verification]] · [[ux-agent]]
