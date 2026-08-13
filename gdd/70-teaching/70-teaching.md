---
title: Teaching
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[teaching-system]]", "[[the-tutorial]]", "[[tutorial-agent]]"]
---

# Teaching

How the player learns the game. Owned by the [[tutorial-agent]], enforced by a build-failing test.

- [[teaching-system]] - the model, and the one rule
- [[placement-bias-order]] - the five tiers, and why tier 0 wins
- [[the-tutorial]] - the unwinnable opening dive
- [[tutorial-beats]] - the ten scripted beats
- [[coachmarks]] - the nine one-time callouts
- [[teaching-tips]] - the seven persistent explainers
- [[mechanic-coverage]] - the inventory, and what "covered" means
- [[teaching-waivers]] - what is deliberately not taught, and why
- [[standing-lessons]] - craft rules extracted from the cycle log

## The charter, in one line

**Every player-facing mechanic has a teaching moment or a written waiver, and `teach-sim.ts` fails the build if that is not true.**

## What is not migrated

`tutorial/ledger.md` is 872 lines, roughly 61% of it dated process log: open work, three closed-work sections, flagged items and thirteen cycle retrospectives. That log stays where it is.

What was durable came here: the charter, the placement law, the coverage model, the waiver rationales, and the ~12 standing lessons that were buried inside the retrospectives. See [[standing-lessons]].

## See also

- [[the-gates]] - the tutorial gate
- [[verification-gate]] - where `teach-sim.ts` sits
