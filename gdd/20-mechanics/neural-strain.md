---
title: Neural Strain
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[death-and-run-end]]", "[[route-cost-and-par]]", "[[the-night-shop]]"]
---

# Neural Strain

> [!info] Source
> `run-reducer.ts:START_STRAIN`, `PATCH_HEAL`, `DAY_REST_REGEN`; `duel-actions.ts:finishDuel`.

The run's health bar. It is the only thing that ends a run early.

```
START_STRAIN    = 100
DAY_REST_REGEN  = 10     free, at day close
PATCH_HEAL      = 12     per night patch bought
cap             = 100
```

Strain is shared across all three tickets of a day. It never rises during a dive.

## It is a bill, not attrition

Strain is charged **only on a win**, and every term is avoidable in principle:

```
chip = 2  * rotations past par
     + 4  * traps sprung (minus 1 with FIRST FAULT)
     + 1  * redirects taken
     + 2  * pressure rounds
     + 10 if the win came at the round cap
chip = min(45, chip)
```

A perfect dive bills exactly zero. Full derivation in [[route-cost-and-par]].

> [!warning] A loss bills nothing
> `finishDuel` sets `strainChip = 0` for a loss. The run is ending anyway, so there is nothing to price.

## The fiction

NF-3 neurofilament degradation. Strain is not injury, it is accumulated scarring from diving, and at zero the connection severs rather than the diver dying:

> NEURAL STRAIN: ZERO. CONNECTION SEVERED.

Dad's death is the same mechanic on a longer timescale. That the player's health bar and the father's cause of death are the same number is the game's central rhyme. See [[dad]] and [[ground-truth]].

## Restoring it

- **+10** free at day close (`resultNext`, when the day closes).
- **+12** per night patch, costing `45 + 5 * day` credits. See [[the-night-shop]].

Night patches are strain suppressants. The bible is explicit that they treat the symptom.

## Teaching

The `strain-chip` coachmark (order 60) fires on first sight of the [[repair-log]] result surface. A `strain` tip is a persistent hover explainer, because the number is reference the player wants repeatedly. See [[teaching-system]].

## See also

- [[death-and-run-end]] · [[economy]]
