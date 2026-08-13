---
title: KP/OS
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[design-pillars]]", "[[title-and-start-screen]]"]
---

# KP/OS

> [!info] Source
> `components/os/shop-os.tsx` (provider and desktop), `wm.tsx`, `desk.tsx`, `boot.tsx`, `login.tsx`, `icons.tsx`, `kp-ui.tsx`.

The shop terminal's retro pixel desktop. **The game does not have an interface. The interface is the game.**

## Why this is a design pillar and not a skin

There is no menu layer over a world, no HUD floating above a scene, and no world. The player is a technician at a bench, looking at a terminal. Everything they do, they do through windows on that terminal, which is exactly what the fiction says they would be doing.

That decision buys enormous economy: no environment art, no camera, no character rig. It costs a hard height budget and a permanent ban on scrollbars. See [[design-pillars]].

## The shell

- **BIOS boot** into **login**, three deletable save slots, one save per slot.
- **Desktop** with icons, draggable windows, taskbar clock showing the in-game day.
- **The dive** is the only full-screen surface. See [[dive-exe]].
- **Refresh is a safe abort**, never a loss. See [[save-and-load]].

## The window manager

`WIN_DEFS` in `shop-os.tsx` declares nine windows. `wm.tsx` handles dragging, focus and z-order.

Windows are genuinely tiled and genuinely movable, which is why the 700px height ceiling exists: a window that fills the desk cannot be tiled, and untileable windows are what made window management feel rough. See [[law-3-fluid-and-the-height-ceiling]].

## Themes

`THEMES` offers three hues (LAVENDER, MAGENTA, PHOSPHOR) and two schemes (NERV, TOKYO NIGHT). Hues are the v2 single-phosphor system; schemes are the v3 role-token remap. Both ship. See [[player-options]] and [[law-1-colour-is-roles]].

## The glass

`Glass()` renders six CRT layers over the stage: `g-scan`, `g-mask`, `g-bloom`, `g-spec`, `g-vig`, `g-bezel`. Flat, never curved. See [[law-6-the-tube]].

## The strain alarm

`STRAIN_ALARM_AT = 35`. Below that the desktop itself arms an alarm state. The operating system reacts to the player's body, which is the clearest single expression of the whole conceit.

## kp-ui.tsx

The shared instrument-panel primitives, not a window: `Ticks`, `Nodes`, `Stripe`, `Ruler`, `Hero`, `DataRows`, `PipRow`, `DiamondRow`, `Chip`, `SegMeter`, `HatchBar`, `Btn`, `PhotoCell`, `PX_ICONS`, `PxIcon`, `KpMark`, `KpLockup`.

## See also

- [[hud-and-ui-design]] · [[ui-rulings]]
