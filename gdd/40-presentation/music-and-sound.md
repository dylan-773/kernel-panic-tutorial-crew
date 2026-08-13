---
title: Music and sound
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[player-options]]", "[[ux-agent]]", "[[law-7-motion]]"]
---

# Music and sound

> [!info] Source
> `game/audio.ts` (460 lines), `game/sfxr.ts`. Music beds at `/assets/sfx/music/<track>.mp3`.

## The engine

An **sfxr preset palette rendered to buffers on demand**, plus a small additive synth for stingers, plus a music manager for the generated beds.

Client-only, lazily created on the first user gesture so importing the module is SSR-safe.

### Three buses

| Bus | Level | Carries |
|---|---|---|
| `ui` | quiet | chrome: clicks, page flips, window sounds |
| `game` | present | the duel |
| `music` | 0.3 | the bed |

All three hang off a master at 0.8. Muting ramps the master with `setTargetAtTime` rather than cutting.

## The palette

Roughly a hundred named effects, all synthesized rather than sampled. A sample of the vocabulary shows how specific it gets: `cascadeEnd`, `claimTick`, `overParTick`, `pieceFuse`, `patchPlace`, `freeze`, `jam`, `deny`, `granted`, `heartbeat`, `alarm`, `darknetLinkUp`, `darknetLinkDown`, `darknetReveal`, `ledgerTick`, `ledgerSettle`, `inboxGenie`, `hueSwap`, `busLogArrival`, `andOpen`.

Note `overParTick`: going over [[route-cost-and-par|par]] has its own sound. The strain economy is audible before it is billed.

## Design intent

- **The cascade arpeggio scales with chain length.** A three-node light and a fifteen-node light are the same sound at different lengths, so the payoff is heard before it is read. See [[cascades-and-surge]].
- **The telegraph has a two-beat sting.** The wind-up is audible, which is what makes it answerable without staring at the board. See [[traps-and-telegraphs]].
- **Traps crack.** A sprung trap is a physical sound, not a UI sound, and it plays on the game bus.

## A trap that cost real time

> [!warning] sfxr envelope values are plain seconds, never normalized knobs
> Treating them as 0-to-1 knobs produced silence. The fix (2026-07-24, "Fix silent audio") also corrected gain staging and added the autoplay unlock. This is why `testBeep()` exists at all: it bypasses every bus and flag so the next silent-audio report can be diagnosed in one click.

## Music

Generated beds, fetched as mp3 and cached in an `AudioBuffer` map, crossfaded rather than cut. Safe to call repeatedly with the same track.

## Where sound lives in the crew

With the [[ux-agent]], not a separate audio seat. Sound is feel, and feel is one job: the agent that decides a press state floods inverse video also decides what it sounds like.

## See also

- [[player-options]] · [[art-direction]]
