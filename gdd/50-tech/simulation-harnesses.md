---
title: Simulation harnesses
status: canon
source: code
owner: validation
updated: 2026-08-05
related: ["[[verification-gate]]", "[[determinism-and-seeds]]", "[[the-ten-day-arc]]"]
---

# Simulation harnesses

> [!info] Source
> `src/game/dev/sim.ts`, `run-sim.ts`, `teach-sim.ts`, plus `kitted-bot.ts` and `kitted-profile.ts`. Run with `bun` from `app/`; never imported by app code.

Three harnesses. Each answers a different question and each can fail a build.

## sim.ts - is the duel balanced?

`SEEDS = 200` per day. `PROXY_GREED = 0.95`. `BEAT_MS = 255` as an AI wall-clock proxy. Six modes cycled by seed.

Runs in order:

1. **`checkPlanHonesty(20)`** - every non-`approx` plan must light the goal at exactly its quoted cost. `exit(1)` on any liar.
2. **Tutorial check** - `tutorial player wins: X of 200 (must be 0)`.
3. **Kit-less pass**, days 1 to 9 plus finale. RAM `5 + floor((day-1)/2)`.
4. **Kitted pass**, same seeds, paired. Adds the delta against kit-less, cast counts and cells per win.
5. **Finale close player-turns histogram**, t1 to t5+, where **t1 must be 0**.
6. **Kitted ends tally**: won goal, won cap, lost goal, lost seal, lost cap.
7. **PD assertion** - every day's measured mean `pd` within `PD_TOLERANCE` (2.0) of `pdTarget`, else `exit(1)`.

Per-day output: win%, cap%, rounds mean and range, chip per win, par, rotations, over%; then measured pd against target, od, ram, approach in turns, rounds p10/p50/p90, `<=2r`%, and ai seconds.

### The canonical build

`kitted-profile.ts` fixes what a "good player" looks like so the kitted pass is reproducible:

- `NIGHT_SCHEDULE = [ram, attack, ram, scan, ram, defend, attack, ram, defend]`
- `MODE_PAIRS`: redirect+purge/jamAnchor, armSiphon+purge/siphonPlus, armHalt+lock/tripwire, cycled per seed from day 3
- `BOOST_SCHEDULE`: hotBoot day 2, longArms day 4, a pair day 6
- `cellsAtDay`: 0,0,1,1,2,2,3,3,3

It **throws at import** if a scheduled augment id no longer exists, so deleting an augment cannot silently degrade the profile into something weaker.

## run-sim.ts - does the run layer hold?

**40 full runs** driving the **real reducers** exactly as the UI does, asserting at every dispatch. `must()` names the dispatch count on failure.

Covers: meta hydration, the opener, the tutorial (asserts unwinnable), 10 days of pick-analyze-dive, drafts (no repeats, never offers owned, `requires` honoured, swap ejects the named boost, bays never exceeded), **pouch conservation** (a dive never mints pieces), night rest, darknet buy, bay buy, craft, the two-step night, the finale, and story scenes.

Also asserts the [[split-boards]] invariants: a `"goal"` verdict means the winner's goal is lit and the loser's is not, and **every live node is built**.

## teach-sim.ts - will the player understand?

Every `MECHANIC_INVENTORY` entry must resolve to a moment, beat, tip or written waiver, and premise-backed waivers must still hold. Plus unique `order`, per-surface limits, line lengths, the four `CORE_VERBS` in the opening dive, and reachability by an actual run walk.

See [[mechanic-coverage]].

## See also

- [[verification-gate]] · [[validation]] · [[difficulty-dials]]
