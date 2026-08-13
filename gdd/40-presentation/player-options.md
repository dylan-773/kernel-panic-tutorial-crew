---
title: Player options
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[music-and-sound]]", "[[kp-os]]", "[[save-and-load]]"]
---

# Player options

A short list, deliberately. Everything here is either accessibility or taste.

## Audio

| Option | Stored | Default |
|---|---|---|
| Sound | `MetaState.sound` | on |
| Music | `MetaState.music` | on |

Both persist per save slot. Music crossfades to silence rather than cutting (`setTargetAtTime` over 0.3s). See [[music-and-sound]].

There is also a **TEST SOUND** diagnostic: a two-tone beep wired straight to the audio destination, bypassing every bus and the mute flag, plus an `audioDebug()` readout of context state, sample rate and master gain. If the beep is silent, the problem is outside the page: tab mute, per-site sound setting, or output device.

## Appearance

| Option | Values |
|---|---|
| Hue | LAVENDER, MAGENTA, PHOSPHOR |
| Scheme | NERV, TOKYO NIGHT |
| CRT | FLAT, OFF |

Hues are the v2 single-phosphor system, restored to the picker on 2026-08-01 after the v3 integration. Schemes are the v3 role-token remap. See [[law-1-colour-is-roles]].

**CRT OFF removes every glass layer outright** rather than fading them, and the surface must still read as a finished flat-ink print. None of a surface's richness may live in the CRT layer. See [[law-6-the-tube]].

## Accessibility

**Reduced motion** is honoured from the OS setting rather than an in-game toggle: choreography collapses to the settled state in one frame, with sound unaffected.

## What is not offered

No difficulty setting. The arc is the difficulty curve, and every balance claim is measured against it. See [[the-ten-day-arc]].

No text size control, because type floors are already fixed at the readable minimum and there is no room to grow inside the height ceiling. That is a real limitation of [[law-3-fluid-and-the-height-ceiling]].

## See also

- [[game-controls]] · [[title-and-start-screen]]
