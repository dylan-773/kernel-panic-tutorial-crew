---
title: The ten-day arc
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[difficulty-dials]]", "[[game-progression]]", "[[arc-composer]]"]
---

# The ten-day arc

> [!info] Source
> `content/arc.ts:DAY_CONFIGS`, `finaleConfig`, `FINAL_DAY = 10`.

Nine working days of three tickets each, then day 10.

## The table as shipped

| Day | Grid | oppRam | greed | abilityFreq | pdTarget | minPd | headStart | parFlat | horizon | focus | slag | patchDrop | jobTiers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[day-1]] | 9x7 | 6 | 0.70 | 0.20 | 16 | - | 0 | 6 | 0 | 0.50 | 0.18 | 0.35 | 1,1,1 |
| [[day-2]] | 9x7 | 6 | 0.80 | 0.40 | 16 | - | 0 | 5 | 1 | 0.65 | 0.18 | 0.35 | 1,1,2 |
| [[day-3]] | 9x9 | 7 | 0.88 | 0.45 | 18 | - | 1 | 5 | 1 | 0.70 | 0.19 | 0.24 | 1,2,2 |
| [[day-4]] | 9x9 | 7 | 0.93 | 0.60 | 18 | - | 2 | 4 | 2 | 0.80 | 0.20 | 0.22 | 2,2,3 |
| [[day-5]] | 11x9 | 8 | 0.94 | 0.55 | 20 | 9 | 2 | 4 | 2 | 0.80 | 0.21 | 0.18 | 2,3,3 |
| [[day-6]] | 11x9 | 8 | 0.98 | 0.78 | 20 | 10 | 3 | 3 | 2 | 0.90 | 0.22 | 0.16 | 3,3,3 |
| [[day-7]] | 11x11 | 9 | 0.99 | 0.65 | 21 | 10 | 3 | 2 | 2 | 0.90 | 0.23 | 0.13 | 3,3,4 |
| [[day-8]] | 13x11 | 10 | 0.98 | 0.70 | 22 | 10 | 3 | 2 | 3 | 0.90 | 0.24 | 0.12 | 4,4,4 |
| [[day-9]] | 13x11 | 11 | 0.97 | 0.75 | 24 | 12 | 4 | 1 | 3 | 0.95 | 0.25 | 0.11 | 4,4,5 |
| [[day-10-the-finale]] | 15x11 | 11 | 1.00 | 0.90 | 29 | 18 | 1 | 2 | 3 | 1.00 | 0.27 | - | finale |

Field meanings in [[difficulty-dials]].

## What escalates, and how

Six curves move against the player at once:

| Curve | Day 1 | Day 9 |
|---|---|---|
| grid | 9x7 | 13x11 |
| opponent RAM | 6 | 11 |
| **horizon** (intelligence) | 0 | 3 |
| **focus** | 0.50 | 0.95 |
| par margin (`parFlat`) | 6 | 1 |
| slag | 0.18 | 0.25 |
| patch drops | 0.35 | 0.11 |
| job tiers | 1,1,1 | 4,4,5 |

Slag rises while patch drops fall, so board material gets scarcer exactly as it gets more necessary. The par margin tightens from a forgiving 6 to a punishing 1, so the same untidy dive that cost nothing on day 1 bills real [[neural-strain]] on day 9.

The counter-pressure is the compounding kit: nine night picks, up to 27 [[augment-drafts|drafts]], and RAM from 5 to 9.

## Target win rates

The **kitted** curve is what gates a deploy:

```
~84 / 93 / 67 / 75 / 56 / 72 / 63 / 52 / 52, finale ~35
```

The kit-less proxy is a **floor and nothing more** (`94/67/60/46/53/41/32/18/13`, finale 0 by construction under `oppOpens`). It never locks, wards or purges, so on split boards it is missing half the game.

Also watched per day: measured `pd` within 2.0 of `pdTarget`, median rounds 3 to 4, and `<=2r` under about 40%. See [[simulation-harnesses]].

## The tutorial is separate

`tutorialConfig()`: 13x7, oppRam 12, horizon 0, focus 0.5, `abilityFreq: 0`, halt traps only, slag 0.12. **Unwinnable by construction.** It must post **0 wins in 200 seeds** before any deploy. See [[the-tutorial]].

## Who owns this table

The [[arc-composer]], and only through the balance loop with before and after sim numbers. Iron rule 4.

## See also

- [[game-progression]] · [[economy]]
