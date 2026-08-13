---
title: Palette generalization conflict
status: unwritten
source: none
owner: user
updated: 2026-08-05
related: ["[[ruling-14-loadout-palette]]", "[[law-1-colour-is-roles]]", "[[kp-os]]"]
---

# Palette generalization conflict

> [!question] UNWRITTEN
> Canon reserved this question for you. The UI spec answered it anyway. Both are in the repo, and they disagree.

## The two positions

**[[ruling-14-loadout-palette]]** (2026-07-31, your directive) scoped the five-channel palette **narrowly to LOADOUT.CFG only**, quoted the v2 single-ink law as still governing "every other surface", and left this explicitly OPEN:

> whether color-as-diagnostic-state should become the general KP/OS law in place of single-ink-accent everywhere, or stay a LOADOUT.CFG exception. **Until the user says otherwise, the narrow reading governs every other surface.**

**[[law-1-colour-is-roles]]** (`ui-demos/RULINGS.md`, established by the same cycle) then generalized it universally:

> Every surface reads the same eight role tokens

and cites ruling 14 as its authority.

## Why this matters beyond bookkeeping

Ten KP/OS v3 panels were integrated on 2026-08-01 under the generalized reading. So the shipped game currently follows law 1, not ruling 14's narrow reading. Whichever way you settle it, one of those two documents needs correcting, and possibly some shipped surfaces.

## A second, smaller mismatch

The hexes do not match either. Ruling 14 lists `#ffab3d / #7bff5a / #ff3b30 / #35d6ff / #fff2d9`. The RULINGS `nerv` scheme uses `#ff9a1f / #8dff3a / #ff2a17 / #23d3ff / #ffe9c4`. Close, but not the same values, and neither document acknowledges the other's.

## What this note must decide

- [ ] Does colour-as-diagnostic-state become the **general** KP/OS law, or stay a LOADOUT.CFG exception?
- [ ] If general: ruling 14's narrow scope clause needs superseding by an explicit new ruling.
- [ ] If exception: the ten integrated v3 panels need auditing against the single-ink law.
- [ ] Which hex set is authoritative, ruling 14's or `nerv`'s?
- [ ] Does the answer differ for `nerv` versus `tokyo`, or do both stand or fall together?

## See also

- [[law-1-colour-is-roles]] · [[art-direction]] · [[design-change-log]]
