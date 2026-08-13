---
title: Job pay and billing
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[credits]]", "[[the-round-cap]]", "[[overtime-clause]]"]
---

# Job pay and billing

> [!info] Source
> `content/arc.ts:jobPay`; `run-reducer.ts:jobPayFor`.

```
jobPay(tier)          = 40 + 25 * tier
jobPayFor(run, capWin) = jobPay * (capWin ? (overtimeClause ? 0.75 : 0.5) : 1)
```

| Tier | Full | Cap win | Cap win with [[overtime-clause]] |
|---|---|---|---|
| 1 | 65 | 32 | 48 |
| 2 | 90 | 45 | 67 |
| 3 | 115 | 57 | 86 |
| 4 | 140 | 70 | 105 |
| 5 | 165 | 82 | 123 |

Plus, where they apply: 25 salvage when the draft pool is dry, and 15 from [[clean-run]] on a trap-free cap win.

## Why a cap win pays half

The job took longer than the deadline. The client does not pay for the overrun. It is the same fact as the +10 strain: a [[the-round-cap|cap]] win is the game telling you it went badly without taking the win away.

[[overtime-clause]] changes the contract term, not the outcome. [[ruling-10-overtime-billing]] is the canon decision that makes this an in-world clause rather than a number.

## Presentation

[[repair-log]] reads the result as a **transaction**: CREDITED, BILLED, RECOVERED. Money in, strain out, pieces recovered. The window is an accounting document, which is what a repair shop would actually produce.

## See also

- [[economy]] · [[the-ten-day-arc]]
