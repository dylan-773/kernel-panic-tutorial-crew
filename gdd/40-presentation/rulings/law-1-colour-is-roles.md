---
title: Law 1 - Colour is roles
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[palette-generalization-conflict]]", "[[ruling-14-loadout-palette]]"]
---

# Law 1 - Colour is ROLES, not hues

**Do not hand-pick colours per surface.** Every surface reads the same eight role tokens, and a scheme is a remap of those tokens and nothing else.

> If you find yourself writing a hex value inside a component rule, you are doing it wrong.

## The eight roles

| Token | Means | Takes |
|---|---|---|
| `--r-struct` | chrome and borders | panel frames, dividers, disabled outlines |
| `--r-note` | annotation: labels that NAME, never STATE | `// LABEL` prefixes, units, tick labels, eyebrows |
| `--r-line` | live data | meters, filled slots, tier segments, values |
| `--r-data` | hot values | hero numerals, the biggest numbers on the surface |
| `--r-ok` | NOMINAL | ready verdicts, the active option |
| `--r-warn` | RISK | **the alarm state only, nothing else, ever** |
| `--r-aux` | a different signal class | camera and video imagery |
| `--r-hazard` | structural red | hazard stripes, focal brackets, window edge, record lights |

## Reversibility

`:root` defaults **every** role onto the single accent, so a surface with no `data-scheme` renders exactly as v2 did. Only `data-scheme` pulls them apart.

**Keep that property.** It is what makes the system reversible, and it is also the reason the v2 hues could be restored to the picker without unpicking v3.

## The two schemes

`nerv` and `tokyo`, given as literal CSS blocks in the source spec. Copy the block from `loadout-eva/index.html`; **do not retype the hexes**. Each also carries `--r-ok-glow` and `--r-warn-glow`, a `color-mix` of their role at 45 to 60 percent.

## Two non-negotiables

**RISK never shares its colour.** `--r-warn` appears on exactly one thing per surface: the alarm. `--r-hazard` is the ambient red and is a duller, separate tone. A surface with no alarm state has no `--r-warn`.

**Colour is never the only channel.** An alarm must also flood inverse video **and move**. Ambient chrome must **never** move.

> [!info] The asymmetry is the mechanism
> Five static red shapes train the eye to stop sampling red. Motion is the one channel the chrome does not have, so motion is what an alarm gets.

## The unresolved scope question

> [!warning] This law generalized something canon reserved for the user
> [[ruling-14-loadout-palette]] scoped the multi-hue palette to LOADOUT.CFG only and left generalization explicitly OPEN. This law says "every surface reads the same eight role tokens", citing that ruling as its authority.
>
> Ten panels shipped under the generalized reading on 2026-08-01. See [[palette-generalization-conflict]].

## See also

- [[law-7-motion]] · [[art-direction]]
