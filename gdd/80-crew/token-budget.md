---
title: Token budget
status: canon
source: lore
owner: orchestrator
updated: 2026-08-05
related: ["[[the-dev-crew]]", "[[game-goals]]"]
---

# Token budget

What the crew cost to build the prototype, as estimated in the v2 GDD.

| Seat | Model | Calls | Tokens per call | Total |
|---|---|---|---|---|
| [[orchestrator]] | Fable 5 | ~60 turns | ~8,000 | ~480,000 |
| [[encounter-generator]] | Sonnet 5 | 60 | 2,700 | 162,000 |
| [[ability-agent]] | Sonnet 5 | 40 | 2,000 | 80,000 |
| [[narrative-director]] | Sonnet 5 | 50 | 1,200 | 60,000 |
| [[loremaster]] | Sonnet 5 | 100 | 1,150 | 115,000 |
| [[tutorial-agent]] | Sonnet 5 | 70 | 1,600 | 112,000 |
| [[arc-composer]] | Sonnet 5 | 12 | 1,300 | 15,600 |
| [[ux-agent]] | Sonnet 5 | 60 | 1,500 | 90,000 |
| [[validation]] | Haiku 4.5 | 240 | 700 | 168,000 |
| [[art-lead]] | Haiku 4.5 | 120 | 400 | 48,000 |
| **Total** | | | | **~1,330,600** |

## What the shape says

**The Orchestrator is 36% of the budget on 3% of the calls.** Integration is the expensive seat because it holds the most context: it reads proposals, writes code, and runs the gate.

**Validation is 240 calls at 700 tokens.** The cheapest possible seat doing the most repetitive work, on Haiku. That is the routing principle: model follows constraint, not prestige.

**Arc Composer is 12 calls.** The seat that moves the difficulty curve touches it rarely, and only with sim numbers in hand. Iron rule 4 is visible in the call count.

## A caveat on the number

The v2 **PDF** renders this table without the Tutorial Agent row and totals about 1,218,600. The HTML is correct at ~1,330,600. See [[revision-history]].

## Constraints this sat inside

- One person.
- **Generation credits are capped.** Higgsfield `nano_banana_pro` at 2 credits per image.
- Context windows are fixed, which is why agents own one file each.
- **Validation loops must terminate**, which is why [[the-round-cap]] exists.

## See also

- [[the-dev-crew]] · [[game-goals]]
