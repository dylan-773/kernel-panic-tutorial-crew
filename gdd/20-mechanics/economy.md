---
title: Economy
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[credits]]", "[[the-night-shop]]", "[[neural-strain]]"]
---

# Economy

> [!info] Source
> `run-reducer.ts`, `content/arc.ts:jobPay`, `patch-cells.ts`.

Three currencies, on three different clocks.

| Currency | Scope | Refills | Spends on |
|---|---|---|---|
| [[ram]] | one turn | every turn | rotations, casts, placements |
| [[credits]] | one run | per cleared ticket | patches, bays, dark pulls |
| [[neural-strain]] | one run | +10 nightly, +12 per patch | nothing; it is spent **on you** |

Nothing crosses between runs. See [[meta-progression]].

## The daily cycle

1. Three tickets on the board, any order. Each pays `40 + 25 * tier`.
2. Each cleared ticket rolls an [[augment-drafts|augment draft]], or 25 salvage if the pool is dry.
3. Each cleared ticket may drop a [[patch-pieces|piece]].
4. Each win bills [[neural-strain]] for how untidily it was won.
5. At day close: +10 strain free, one upgrade pick, and the shop.

## The core tension

Credits buy exactly three things, and they are on different time horizons:

- **Night patches** - survival now. `45 + 5 * day`, rising as your margin shrinks.
- **[[boost-bays|Boost bays]]** - power that compounds. 150 then 300, front-loaded cost for back-loaded value.
- **[[the-darknet|Dark pulls]]** - board material. `25 + 5 * (day - 1)`, blind.

Buying the fifth bay on day 5 costs roughly six night patches of strain forgone. There is no correct answer, which is the point.

## Pressures that escalate together

Across the arc: slag rises (0.18 to 0.27), patch drops fall (0.35 to 0.11), `parFlat` tightens (6 to 1), and night patch cost climbs. Every curve moves against the player at once, and the counter-pressure is the compounding kit. See [[the-ten-day-arc]].

## See also

- [[job-pay-and-billing]] · [[scoring-and-lifetime-stats]]
