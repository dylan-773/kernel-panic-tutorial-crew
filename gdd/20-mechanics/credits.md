---
title: Credits
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[job-pay-and-billing]]", "[[the-night-shop]]", "[[economy]]"]
---

# Credits

> [!info] Source
> `content/arc.ts:jobPay`; `run-reducer.ts:jobPayFor`, `SALVAGE_PAY`.

The run currency. Earned by clearing tickets, spent at night.

## Earning

```
jobPay(tier) = 40 + 25 * tier
```

| Job tier | Pay |
|---|---|
| 1 | 65 |
| 2 | 90 |
| 3 | 115 |
| 4 | 140 |
| 5 | 165 |

Modifiers:
- **Cap win**: 50%, or 75% with [[overtime-clause]].
- **Salvage**: 25 credits (`SALVAGE_PAY`) when the [[augment-drafts|draft pool]] is dry.
- **[[clean-run]]**: 15 credits on a trap-free cap win.

Total credited per ticket is `ticketPay + salvage + cleanRunBonus`.

## Spending

| Purchase | Cost |
|---|---|
| Night patch, +12 [[neural-strain|strain]] | `45 + 5 * day` |
| [[boost-bays|Boost bay]] 4 then 5 | 150, then 300 |
| [[the-darknet|Dark pull]] | `25 + 5 * (day - 1)`, less 15% with [[darknet-rate]] |
| [[patch-pieces|Craft a weld]] | free (`CRAFT_COST = 0`) |

## The shape of the decision

Credits convert into exactly three things: survival now (patches), power that compounds (bays), or board material (pulls). There is no saving for later, because credits do not survive the run. See [[meta-progression]].

## Fiction

Credits are also the debt story. The shop is behind, the bills are real, and the [[entry-bills|drawer of Meridian final notices]] is what the money is actually for. The economy screen and the story are the same subject. See [[the-shop]].

## See also

- [[economy]] · [[scoring-and-lifetime-stats]]
