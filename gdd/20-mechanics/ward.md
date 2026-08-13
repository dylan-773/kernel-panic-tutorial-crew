---
title: WARD
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[defend]]", "[[traps-and-telegraphs]]", "[[redirect]]"]
---

# WARD

> [!info] Source
> `kit.ts:WARD_RADIUS`, `WARD_ROUNDS`, `defendModeDesc`, `AUGMENTS.cfgWard`. Unlocked by [[ward-driver]].

Ward a junction and everything within a Manhattan radius of it for **2 rounds** (`WARD_ROUNDS`).

| DEFEND tier | Radius |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

Inside the bubble:
- **no new traps can land**, and
- **[[redirect]] cannot touch anything**.

State lives on the cell as `wardThroughRound` and `wardBy`. The shipped augment copy notes the effect holds "for the full duration on both sides".

## Prevention rather than cure

Ward is the only defensive mode that acts before the threat exists. [[purge]] needs a trap already planted and already revealed by [[scan]]; ward makes the planting illegal.

At tier 3 a radius of 3 covers a large share of an approach corridor, which is what makes it the answer to a wide-casting tier 5 opponent that can plant faster than you can purge.

## As an opponent routine

The `ward`-dominant Analyze tell: "Diagnostic flags warding fields. Whole approaches will refuse your traps and shrug off your redirects." Against it, plan to route around rather than through.

## See also

- [[purge]] · [[lock]]
