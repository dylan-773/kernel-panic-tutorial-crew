---
title: Game controls
status: derived
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[kp-os]]", "[[turn-structure]]", "[[technical-requirements]]"]
---

# Game controls

> [!info] status: derived
> No controls documentation existed. This is read out of the components.

**Mouse-driven throughout.** There is no keyboard control scheme, no gamepad support, and no documented shortcut set.

## Desktop

| Action | Input |
|---|---|
| Open a window | click a desktop icon |
| Move a window | drag its title bar |
| Focus a window | click it |
| Close a window | the pixel X, the only button in the title bar |
| Switch window | taskbar |

## In a dive

| Action | Input |
|---|---|
| Rotate a junction | click it |
| Place a [[patch-pieces\|patch piece]] | drag from the pouch onto a slag cell |
| Cast a program | click SCAN, ATTACK or DEFEND, then click target cells |
| Change mode | in [[loadout-cfg]] before the dive |
| Undo | the undo button, once per turn, labelled with what it will reverse |
| End turn | the end turn button |
| Abandon | refresh, which is a safe abort |

Targeting is click-to-select, and `badTargetCount` and `illegalTarget` are refusal reasons the command gate returns, so partial target selection is a real state. See [[turn-structure]].

## In the solder bay

Drag one [[patch-pieces|piece]] onto another to weld. Illegal partners are rendered **physically dead and disabled** rather than accepting the drag and rejecting it. See [[solder-bay]].

## Accessibility

- **Reduced motion** is honoured: choreography collapses to the settled state in one frame, sound unaffected. See [[law-7-motion]].
- Colour is never the only channel for risk. See [[law-1-colour-is-roles]].
- **No keyboard path exists.** A player who cannot use a mouse cannot play.

## Open questions

- [ ] Is a keyboard scheme wanted? Every action is discrete and grid-based, so it is tractable.
- [ ] Touch is unaddressed. `touch-safe-tooltips` is a logged ui-spec in the teaching ledger, so it has been noticed but not designed. See [[technical-requirements]].

## See also

- [[player-options]] · [[hud-and-ui-design]]
