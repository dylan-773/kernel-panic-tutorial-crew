---
title: SCAN
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-kit]]", "[[traps-and-telegraphs]]", "[[purge]]"]
---

# SCAN

> [!info] Source
> `kit.ts:SCAN_RANGE`, `scanDesc`.

Information. 1 RAM, once per turn, acts on your own board.

Exposes every armed node within range of your territory, **permanently**.

| Tier | Range |
|---|---|
| 1 | 3 |
| 2 | 6 |
| 3 | whole board |

Shipped copy at tier 3: "Expose every armed node on the entire board, permanently. Always 1 RAM."

## Why it matters

[[purge]] can only disarm what is **revealed**. Scan is the prerequisite half of the trap counter, which is why every trap-flavoured [[traps-and-telegraphs|Analyze tell]] ends with "Scan early."

Against a `redirect`-dominant opponent, scan is close to worthless. Against `armHalt` or `armSiphon` it is the difference between a clean dive and a strain bill. That asymmetry is what makes the honest pre-dive tell a real decision rather than flavour text.

## Interaction

[[tap-line]] adds route intelligence on top: SCAN also traces the intrusion's planned route for 2 rounds.

## See also

- [[the-kit]] · [[program-tiers]]
