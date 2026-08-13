---
title: The duel
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[split-boards]]", "[[the-kit]]", "[[win-conditions]]"]
---

# The duel

> [!info] Source
> `duel-types.ts`, `duel-setup.ts`, `duel-power.ts`, `duel-actions.ts`, `duel-commands.ts`, `opponent.ts`. Branch `split-boards`.

The duel is the combat system. Every dive into a customer's device is one duel against one intrusion. It is turn-based, deterministic from a seed, and it is a race rather than a fight: nobody has hit points.

## The one-paragraph version

You and the intrusion each get your own grid of scrambled pipe junctions. Your signal runs from an entry on the left edge toward a goal column on the right. Your only movement verb is [[rotation]]: twist a junction a quarter turn so its arms line up and the signal flows further. First side to light a goal cell wins. You also carry three programs ([[the-kit]]) that let you reach across and interfere with the other board, and they let the intrusion reach across and interfere with yours.

## What makes it a game rather than a puzzle

A solitaire pipe puzzle has one correct answer and no clock. Three things turn this into a duel:

1. **RAM is a per-turn budget.** Each rotation costs 1 [[ram]]. You cannot do everything you can see.
2. **The other side is also racing.** [[opponent-ai]] runs the same route metric you do, on its own board.
3. **You can reach across.** [[attack]] acts on their board, [[defend]] on yours. Interference is bidirectional and telegraphed one beat ahead.

## The two layers

The single most important structural idea, and the reason the rewrite happened:

- **`built`** is every node your signal has ever lit. Permanent.
- **`power`** is every node carrying signal from your entry right now. Cuttable.

Progress is reversible in throughput and never in construction. Full detail in [[built-and-power]].

## Glance order of a turn

1. Read the machine's telegraphed `aim` (see [[traps-and-telegraphs]]).
2. Spend [[ram]] on rotations, a program cast, or a [[patch-pieces]] placement.
3. Watch the board re-settle. Any first light pays a cascade into your next turn ([[cascades-and-surge]]).
4. End turn. The machine takes one visible step at a time.

Full sequencing in [[turn-structure]].

## How it ends

Three outcomes only, `DuelEndKind = "goal" | "cap" | "seal"`. See [[win-conditions]].

Winning is not free: rotations past [[route-cost-and-par]], sprung traps, redirects taken and rounds spent under pressure all bill [[neural-strain]] on the way out. A clean dive still bills exactly zero.

## Design intent

- **Touch-move.** Every rotation settles the board immediately. There is one take-back per turn and a cast spends it. The texture is commitment, not exploration.
- **Defence is not occupation.** With split boards, defending means anti-trap and anti-redirect. It is never holding ground, which is what the old model made it and which did not play well. See [[territory-and-claiming]].
- **The signature moment is the cascade.** [[reach-and-placement]] and the banked payoff both exist to serve it: hold a long chain behind one unturned junction, then flip it.

## See also

- [[difficulty-dials]] - how the same rules get harder across the arc
- [[the-ten-day-arc]] - what the player faces, day by day
- [[the-tutorial]] - how the four core verbs are taught
