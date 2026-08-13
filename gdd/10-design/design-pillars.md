---
title: Design pillars
status: derived
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[elevator-pitch]]", "[[kp-os]]", "[[determinism-and-seeds]]"]
---

# Design pillars

> [!info] status: derived
> These were never written down as a list. They are read back out of the decisions the project actually defends: what it refuses to do, and what it rebuilt rather than compromise.

## 1. The interface is the game

Not a frame around it. KP/OS boots, you log in to one of three slots, you drag windows. Every screen is a window; the dive is the only full-screen surface. There is no menu layer, no HUD floating over a world, and no scene the interface sits in front of.

**What it costs:** a hard 700px height ceiling, no internal scrollbars ever, and a cut discipline for when a panel does not fit. See [[law-3-fluid-and-the-height-ceiling]] and [[law-8-the-cuts-discipline]].

## 2. Legible over deep

Three programs, six modes, eighteen augments, four verbs. The catalog is small enough to hold in your head during a turn.

**What it costs:** the entire eight-verb ability system was deleted. See [[design-change-log]], entry 4.

## 3. Every threat is answerable

A telegraphed action the player cannot respond to during the wind-up is an animation, not a telegraph. The Analyze tell is honest. Modes counter each other rather than laddering. Every term in the strain bill is avoidable in principle.

**What it costs:** the machine must show its aim one beat early even when that makes it weaker. See [[traps-and-telegraphs]].

## 4. Claims are measured, not asserted

Every balance statement comes from 200 seeds a day through a deterministic harness. The tutorial must post **0 wins in 200 seeds**. Teaching coverage is a build-failing test.

**What it costs:** a duel that cannot be unbounded, which is why [[the-round-cap]] exists at all. See [[verification-gate]].

## The pillar that was tested and failed

**Defence as position.** The shared-board model made defending mean holding ground, and it was rebuilt from scratch rather than tuned. See [[territory-and-claiming]].

## See also

- [[game-goals]] · [[ui-rulings]]
