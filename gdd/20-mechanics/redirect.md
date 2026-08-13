---
title: REDIRECT
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[attack]]", "[[rotation]]", "[[jam-anchor]]"]
---

# REDIRECT

> [!info] Source
> `kit.ts:attackModeDesc`. ATTACK default mode, needs no augment.

Twist enemy or open junctions a quarter turn, **anywhere on the board, no reach limit**. Cuts power to everything downstream.

Targets per cast follow `ATTACK_WIDTH`: 1, 2 or 3.

## Why it is the economic core of the duel

A redirect costs the caster 1 RAM as part of a 1 RAM program cast. Undoing it costs the victim:

| Piece hit | Their repair cost |
|---|---|
| elbow or tee | **3 RAM** |
| straight | 1 RAM |
| cross | 0 RAM |

Elbows and tees are 57% of the board. That exchange rate is the reason reaching across is worth doing at all, and it is priced into [[neural-strain]]: `REDIRECT_STRAIN_PER = 1` bills you 1 strain per redirect that landed on you, because each one cost you roughly 3 RAM to undo. See [[rotation]].

## What stops it

- [[lock]] - `redirectTargetLegal` refuses a node locked by the other side.
- [[ward]] - REDIRECT cannot touch anything inside a warded radius.
- `fused` cells. A placed [[patch-pieces|patch piece]] is permanent for everyone.

## Risk

A REDIRECT settles the **enemy** board immediately. A badly chosen twist can complete their route and end the dive in their favour.

## Interaction

[[jam-anchor]] makes your REDIRECT also freeze the junction it twists, through the reply and into your next turn.

## See also

- [[attack]] · [[traps-and-telegraphs]]
