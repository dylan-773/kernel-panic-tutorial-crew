---
title: Verification gate
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[simulation-harnesses]]", "[[the-ten-day-arc]]", "[[the-plays]]"]
---

# Verification gate

**Nothing deploys unless all four are green.** Iron rule 5.

```bash
cd /Users/lyd0n/Development/kernel-panic/kernel-panic-site/app

bun run typecheck
bun run src/game/dev/sim.ts        # tutorial MUST print 0/200
bun run src/game/dev/run-sim.ts    # run-layer invariants
bun run src/game/dev/teach-sim.ts  # every mechanic taught or waived
```

> [!warning] `cd` first, always
> Working-directory drift resolves a broken global toolchain. Run every command from `app/`.

## What each proves

| Command | Proves |
|---|---|
| `typecheck` | the content modules match their schemas. This is the schema enforcer for every hand-integrated proposal |
| `sim.ts` | the duel is balanced, the planner is honest, and the tutorial is unwinnable |
| `run-sim.ts` | the run layer's invariants hold across 40 full runs |
| `teach-sim.ts` | every mechanic is taught or explicitly waived |

## The curve to gate

Gate the **KITTED** curve:

```
~84 / 93 / 67 / 75 / 56 / 72 / 63 / 52 / 52, finale ~35
```

The kit-less proxy is a **floor and nothing more** (`94/67/60/46/53/41/32/18/13`, finale 0 by construction under `oppOpens`). It never locks, wards or purges, and on [[split-boards]] defence is half the game.

Also per day: measured `pd` within 2.0 of `pdTarget`, median rounds 3 to 4, `<=2r` under about 40%.

## The absolute

**Tutorial: 0 wins in 200 seeds.** Not a target, a gate. See [[the-tutorial]].

## Deploy

Orchestrator only, on explicit user OK. Commit in `kernel-panic-site/`, push to main, then `deploy_website`, then verify live markers.

> [!warning] Live-site checks need `curl --compressed` and about 20s of CDN settle
> Grep all JS chunks for marker strings.

## The UI has its own gate

Panels are verified separately, by measurement rather than by eye. See [[law-10-verification]].

## See also

- [[simulation-harnesses]] · [[the-plays]] · [[validation]]
