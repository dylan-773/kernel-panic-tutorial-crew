---
title: Cascades and surge
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[built-and-power]]", "[[ram]]", "[[reach-and-placement]]"]
---

# Cascades and surge

> [!info] Source
> `kit.ts:cascadeRam`, `surgeTierOf`; `duel-actions.ts:settleBoard`.

The signature moment. Hold a long chain aligned behind one unturned junction, then flip that junction and light all of it at once.

## The payoff curve

`cascadeRam(lit)` where `lit` is the number of nodes lit for the **first** time in one settle:

| Nodes lit | RAM banked |
|---|---|
| 0 to 2 | 0 |
| 3 to 5 | 1 |
| 6 to 9 | 2 |
| 10 to 14 | 3 |
| 15 or more | 4 |

Steep on purpose. From `kit.ts`:

> A two-node light is not an achievement and pays nothing; a ten-node light means you deliberately held a long chain behind one unturned junction for two or three turns and then flipped it, which is the combo the fast win is supposed to be made of.

## Two rules that keep it honest

**1. Only first lights count.** `settlePower` pays on `built.length`, and `built` only collects cells whose `built` flag was false. Cutting and re-lighting your own chain pays zero. See [[built-and-power]].

**2. The RAM banks into the next turn.** `s.econ[owner].drainNext -= bonus`. Negative `drainNext` is a gain.

> [!danger] REVISED IN PROTOTYPE
> Paying cascade RAM immediately collapsed duels to about 1.5 rounds across a 200-seed sweep. One good chain simply ended the game, because the reward funded the follow-up that finished it inside the same turn. Banked, the same reward is pure tempo on the very next cycle and the duel keeps its shape.

## Surge tiers

`surgeTierOf(lit)` grades what a light does beyond RAM:

| Tier | Threshold | Effect |
|---|---|---|
| `none` | 0 to 2 | nothing |
| `spark` | 3 or more | RAM only |
| `surge` | 6 or more | **shatters every enemy lock on this board** |
| `break` | 10 or more | surge, **plus** cooks one armed enemy trap on this board dead |

### SURGE shatters clamps

A cascade is a power surge, so it blows the clamps on the board it happened on. Every cell whose `lockedBy` is the other side has its lock cleared.

This is the designed counter to a [[lock]]-heavy opponent. Without it, the answer to being clamped would be "wait two rounds", which is not a play. With it, the answer is "light something big", which is.

### BREAK arcs across

At ten or more, the overload also finds one armed trap on the owner's **own** board and destroys it before the signal ever walks into it. Their cast, wasted.

> [!warning] It clears a trap on your grid, not on theirs
> `settleBoard` searches `b`, which is `s.boards[owner]`. The trap destroyed is one the enemy planted on you. Reading this as "you blow up their trap on their board" gets the targeting backwards.

## Why reach 2 exists

The setup move is only possible because you can rotate up to 2 steps beyond built ground without lighting anything. [[reach-and-placement]] and this note are two halves of one mechanic. [[long-arms]] at reach 4 exists to make the held chain longer.

## Effects are side-tagged

`emit` fires `cascade` or `cascadeOpp`, `surgeBreak` or `surgeBreakOpp`. This was a bug fix: an untagged `cascade` rendered the machine lighting half its own board as a green win banner on the player's screen.

## See also

- [[traps-and-telegraphs]] - what a cascade can spring on the way through
- [[the-board]] - piece mix, which sets how buildable a long chain is
- [[teaching-system]] - the `cascade-bank` coachmark, and its copy drift
