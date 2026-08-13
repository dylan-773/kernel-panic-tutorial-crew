---
title: Clip queue
status: canon
source: user
owner: user
updated: 2026-08-05
related: ["[[marketing-plan]]", "[[cascades-and-surge]]"]
---

# Clip queue

> [!info] Source
> `marketing/clips/orders/*.json`, nine open orders. Fulfilled by the `clip-director` agent.

Short-form capture orders. Each is a structured brief, not a suggestion.

| Order | Pillar |
|---|---|
| `boot-cold-open` | the OS conceit |
| `desktop-is-the-game` | the OS conceit |
| `cascade-bank` | hook-loop |
| `chain-claim-lockout` | hook-loop |
| `telegraph-read` | hook-loop |
| `customer-of-the-day` | content |
| `tutorial-unwinnable` | story |
| `sound-from-nothing` | craft |
| `tuned-by-simulation` | craft |

## The shape of an order

`{ id, pillar, spoilerTier, priority, status, hook, capture{surface, setup, actions, duration, sound}, edit{aspect, notes}, captions }`

`spoilerTier` is the interesting field: it gates a clip against the [[reveal-schedule]]. A clip that shows a run-8 beat is a spoiler even though it is a real screenshot.

## One rule worth quoting

From the `cascade-bank` order, on capturing a chain of four or more:

> If the cascade comes in under 4, keep playing and capture the next one. **Do not fake it.**

The capture instructions also name a real setup detail: shoot day 1 or day 2 jobs, because "day 1 sits near an 82 percent win rate so you can play loosely and still get clean footage."

## See also

- [[marketing-plan]] · [[cascades-and-surge]]
