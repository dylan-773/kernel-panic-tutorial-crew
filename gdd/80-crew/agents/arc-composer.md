---
title: Arc Composer
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-ten-day-arc]]", "[[difficulty-dials]]", "[[validation]]"]
---

# Arc Composer

The difficulty curve. Sonnet, `maxTurns` 15.

## Owns

`pipeline/proposals/arc-composer.json`. Proposes `DayConfig` deltas against win-rate targets.

Never touches `kernel-panic-site/`.

## The table it moves

`DAY_CONFIGS` in `content/arc.ts`. See [[the-ten-day-arc]] for values and [[difficulty-dials]] for what each field means.

## The rule

Deltas against targets, with before and after sim numbers from the latest [[validation]] report. Iron rule 4.

## The smallest seat by call count

12 calls in the [[token-budget]], against 240 for Validation. The seat that can most easily break the game touches it least, and only with measurements in hand.

## What it learned about its own dials

`greed` is finished as a difficulty dial because it **compounds with duel length**. `focus` replaced it precisely because it does not. That distinction is this seat's most useful piece of institutional knowledge. See [[difficulty-dials]].

## See also

- [[the-ten-day-arc]] · [[simulation-harnesses]]
