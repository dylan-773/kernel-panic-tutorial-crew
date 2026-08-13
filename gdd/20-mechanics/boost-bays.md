---
title: Boost bays
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[augments]]", "[[the-night-shop]]", "[[player-inventory]]"]
---

# Boost bays

> [!info] Source
> `run-reducer.ts:BOOST_SLOTS_BASE`, `BOOST_SLOTS_MAX`, `BOOST_SLOT_COSTS`.

```
BOOST_SLOTS_BASE = 3
BOOST_SLOTS_MAX  = 5
BOOST_SLOT_COSTS = [150, 300]
```

Bays hold **boosts only**. Configs are exempt from the cap, so unlocking all four modes never costs you a bay.

You start a run with 3 bays and can buy the 4th for 150 credits and the 5th for 300, at the [[the-night-shop|night shop]].

## The swap

At full bays, a boost draft pick becomes a swap: you name the installed boost to eject. The ejected augment is gone, not banked.

This is the run's main build-identity decision. With 14 boosts and 3 to 5 bays, most of the catalog is permanently unseen in any given run, which is what makes two runs feel different.

## Cost pressure

150 then 300 credits sits directly against [[the-night-shop|night patches]] at `45 + 5 * day` and [[the-darknet|dark pulls]] at `25 + 5 * (day - 1)`. Buying the 5th bay on day 5 is roughly six night patches of [[neural-strain]] forgone.

That is the intended tension: bays are power that compounds, strain is survival now.

## See also

- [[augments]] · [[augment-drafts]] · [[economy]]
