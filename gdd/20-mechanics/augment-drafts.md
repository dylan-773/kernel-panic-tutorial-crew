---
title: Augment drafts
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[augments]]", "[[boost-bays]]", "[[credits]]"]
---

# Augment drafts

> [!info] Source
> `run-reducer.ts:rollDraft`, `pickAugment`; `SALVAGE_PAY = 25`.

One draft per **cleared ticket**. Three tickets a day, so a clean day banks three picks.

## The roll

`rollDraft(run)` offers **three** cards, deterministic per `(runSeed, day, activeJob)`.

- Weighted: config 3, boost 1 (`AugmentDef.weight` defaults).
- `requires` gates honoured.
- Never offers something already owned.
- **Slot 0 is always a config while any config is unowned.**

That last rule is the progression guarantee. Modes are the interesting axis, so the game makes sure you are reliably offered one until you have all four drivers.

> [!danger] REVISED IN PROTOTYPE
> The draft replaced a random unlock. A random grant cannot be planned around; a curated three can. The mandatory build stop was cut at the same time, so configuring became optional and diving never waits on it.

## Picking

- A **config** is simply added. It unlocks a mode without switching to it.
- A **boost** occupies a [[boost-bays|bay]]. At full bays the pick becomes a **swap**: you name the installed boost to eject.

## When the pool runs dry

`SALVAGE_PAY = 25` credits instead of a card.

The pool is 18 augments against roughly 27 cleared tickets, so this starts happening around day 6 and is the normal state for days 7 to 9. See the cadence problem in [[augments]].

## Teaching

Three coachmarks cover this surface: `augment-draft` (order 61) teaches the draft and the cadence, `boost-swap` (62) teaches ejection. Both fire on the [[repair-log]] surface. See [[coachmarks]].

## See also

- [[repair-log]] - where drafts are presented
