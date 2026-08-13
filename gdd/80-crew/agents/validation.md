---
title: Validation
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[simulation-harnesses]]", "[[verification-gate]]"]
---

# Validation

Runs the harnesses. **Haiku**, `maxTurns` 15. Tools: Bash, Read, Write.

The only agent with **no memory and no skills**.

## Owns

`pipeline/validation/report.md`, overwritten each run.

## What it does

Runs `typecheck` plus the sims, and reports distributions against targets with a **PASS or FAIL verdict**. See [[simulation-harnesses]] and [[verification-gate]].

## Why it is deliberately the dumbest seat

It measures; it does not interpret. Memory would let it form opinions across runs, and an opinionated measurement is not a measurement.

240 calls at ~700 tokens: the highest call count and the cheapest model. Model follows constraint, not prestige. See [[token-budget]].

## Its one absolute

`tutorial player wins: 0 of 200`. Anything else fails the build.

## See also

- [[verification-gate]] · [[arc-composer]] · [[ability-agent]]
