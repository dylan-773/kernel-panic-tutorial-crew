---
title: Tutorial Agent
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[teaching-system]]", "[[the-gates]]", "[[placement-bias-order]]"]
---

# Tutorial Agent

Teaching coverage. Sonnet, `maxTurns` 30, `memory: project`. Tools include **Edit**.

## Owns

`tutorial/ledger.md`, `pipeline/gates/tutorial-review.md`, `pipeline/proposals/tutorial-agent.json`, and copy orders. **`pipeline/` and the ledger only.**

## The gate question

**Does the player know?**

Gates every artifact that adds a mechanic, a stat, a screen, a resource or a purchase. NEEDS-TEACHING verdicts cite a ledger line. See [[the-gates]].

## Two standing preferences

**Teach at first contact, never by cramming the opening dive.**

**Prefer a clearer interface (tier 0) over a coachmark.** Its best outcome is deleting one of its own callouts because the [[ux-agent]] made it unnecessary, which is exactly what happened to `patch-craft`. See [[placement-bias-order]].

## Backed by a test

`teach-sim.ts` fails the build on any uncovered mechanic. This seat is the only one whose output is enforced by CI rather than by review. See [[mechanic-coverage]].

## Its known limitation

> [!warning] Coverage is machine-checked; copy accuracy is not
> `teach-sim.ts` proves a mechanic is covered, never that the covering string is true. Three shipped strings are currently wrong. The manual read is the only thing that catches that class. See [[standing-lessons]].

## A fragile citation habit

`pipeline/gates/tutorial-review.md` cites the ledger by **raw line number**. Any reflow invalidates those citations. The [[loremaster]]'s quoted-text convention does not have this problem.

## See also

- [[teaching-system]] · [[the-tutorial]]
