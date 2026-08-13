---
title: Standing lessons
status: canon
source: lore
owner: tutorial-agent
updated: 2026-08-05
related: ["[[70-teaching]]", "[[the-gates]]", "[[teaching-system]]"]
---

# Standing lessons

Craft rules extracted from thirteen dated cycle retrospectives in `tutorial/ledger.md`. The retrospectives stay there; the lessons belong here, because they are reusable and their dates are not.

## On verification

**Verify against ground truth, not against the proposal text.** A proposal describing what a change will do is not evidence the change did it. Read the shipped file.

**Verify after integration, not at proposal time.** The gate that matters is the one run against what actually landed.

**Verify claims that say nothing changed.** "Unchanged" is a claim like any other and is wrong about as often.

## On scope

**A gate's scope is the artifacts named in the brief**, not everything the reviewer notices. Out-of-scope findings get noted once, not blocked on.

**Redesigning an existing window is pure UI.** No loremaster gate, no tutorial gate, no detour into game code. Those gates are for new fiction or new things a player must understand. See [[the-gates]].

## On copy

**Vague to specific raises the stakes.** Replacing a general line with a concrete one usually improves it and occasionally invents canon. Check which.

**Copy drift is invisible to coverage tests.** `teach-sim.ts` proves a mechanic is covered, never that the covering string is true. Three shipped strings are currently wrong. See [[mechanic-coverage]].

## On the teaching system itself

**A moment that never appears is usually losing an `order` tie**, not broken. See [[teaching-system]].

**Constants that two files both depend on will drift.** `first-rotation` versus `MAX_OPENING_BUILT` cost 23.9% of opening dives their rotation lesson. See [[tutorial-beats]].

**Prefer a clearer interface over a coachmark, always.** The `patch-craft` retirement is the model: fix the surface, delete the callout. See [[placement-bias-order]].

**A new visual footprint is a ui-spec, not a teaching decision.** File it to the [[ux-agent]].

## On process

**Append, do not renumber.** Rulings and laws are cited by number from other files. See [[canon-rulings]].

## See also

- [[70-teaching]] · [[the-gates]]
