---
title: Home
status: canon
source: none
owner: orchestrator
updated: 2026-08-05
related: ["[[table-of-contents]]", "[[vault-conventions]]", "[[revision-history]]"]
---

# KERNEL PANIC

A turn-based cyberpunk roguelike about inheriting your father's computer repair business and the machine in the back room he never let you touch.

Playable prototype: [kernel-panic.higgsfield.app](https://kernel-panic.higgsfield.app)
Build `0.7.0`, dated 2026-07-29 (`app/src/game/version.ts`).

> [!warning] The duel changed
> The design docs that predate this vault describe a shared board with territory and claiming. That model is gone. The current engine gives each side its own grid. Start at [[split-boards]], and see [[territory-and-claiming]] for what was removed and why.

## Start here

| If you want | Read |
|---|---|
| The 60-second version | [[elevator-pitch]] |
| What the game is trying to be | [[design-pillars]] |
| How a session actually goes | [[core-loop]] then [[game-flowchart]] |
| The combat system | [[the-duel]] |
| The story, spoilers included | [[ground-truth]] |
| What the player is taught, and when | [[teaching-system]] |
| How the interface works | [[kp-os]] |
| Who builds this | [[the-dev-crew]] |

## The ten areas

- **[[10-design]]** - pitch, goals, pillars, loop, flowchart, progression.
- **[[20-mechanics]]** - the duel, the kit, augments, economy, metrics, difficulty.
- **[[30-content]]** - the ten days, twelve customers, journal entries, cutscenes, world.
- **[[40-presentation]]** - KP/OS, the windows, controls, options, art, audio, the UI rulings.
- **[[50-tech]]** - stack, requirements, save and load, determinism, the harnesses.
- **[[60-story]]** - ground truth, characters, the reveal schedule, canon rulings, voice.
- **[[70-teaching]]** - the teaching system, the tutorial, coverage, waivers.
- **[[80-crew]]** - the nine agents, the pipeline, the gates, the plays.
- **[[90-business]]** - marketing, monetization.

## How to read a note

Every note declares what it is in frontmatter. The field that matters most is `status`:

| status | meaning |
|---|---|
| `canon` | Matches shipped code or settled canon. Trust it. |
| `derived` | Read out of the code but never written down before. Trust it, but it was inferred. |
| `draft` | A proposal. Needs your review before it counts. |
| `unwritten` | No decision exists. The note holds the open questions, not the answer. |

Full rules in [[vault-conventions]].

## Open questions

Notes carrying `status: unwritten` are the live edges of the design. Currently:

- [[monetization]] - nothing decided.
- [[palette-generalization-conflict]] - canon ruling 14 reserved this for you; the UI spec answered it anyway.
- [[meta-progression]] - v2 removed the old carry-between-runs mechanic and never replaced the statement.

## What this vault is not

It does not contain the code. `kernel-panic-site/` is a separate nested repo and is deliberately outside this vault. It also does not contain `pipeline/`, which is per-cycle scratch that gets cleared between production runs. Durable findings from the pipeline are lifted into notes here; the dated verdicts stay where they are.
