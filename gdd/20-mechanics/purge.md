---
title: PURGE
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[defend]]", "[[scan]]", "[[sweep-credit]]"]
---

# PURGE

> [!info] Source
> `kit.ts:defendModeDesc`. DEFEND default mode, needs no augment.

Disarm revealed traps on your own board. 1, 2 or 3 per cast by `DEFEND_WIDTH`.

Shipped copy:

> Disarm one revealed trap. Scan first; you cannot defuse what you cannot see.

## The prerequisite

Purge only sees **revealed** traps. [[scan]] is the other half of the counter. Two programs, two turns of RAM, to answer one enemy cast is a deliberately steep exchange, and it is why [[ward]] (prevention) and a BREAK [[cascades-and-surge|cascade]] (destruction) are worth having as alternatives.

## Interaction

[[sweep-credit]] refunds 1 RAM per trap defused, up to 3 per cast, which turns a wide purge against a trap-heavy board from a cost into close to free.

## As an opponent routine

A `purge`-dominant customer is flagged by the Analyze tell as "self-cleaning routines. Traps you plant will not stick around." Against it, your own [[arm-halt]] and [[arm-siphon]] casts are low value and [[redirect]] is the better attack.

## See also

- [[lock]] · [[ward]]
