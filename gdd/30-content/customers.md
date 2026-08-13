---
title: Customers
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[intrusions]]", "[[encounter-generator]]", "[[inbox]]"]
---

# Customers

> [!info] Source
> `content/customers.ts:CUSTOMERS`, twelve `CustomerProfile` entries; `lore/bible.md` roster.

Twelve regulars. Every job is an intrusion in a machine somebody loves.

```ts
{ id, name, device, portrait, quotes: [string, string],
  winLine, lossLine, tiers: number[], dominant: OppMode }
```

| Customer | Device | Tiers | Dominant |
|---|---|---|---|
| [[juno-vex]] | Hexlight arcade handheld | 1, 2 | [[arm-siphon\|armSiphon]] |
| [[sable-okonkwo]] | Kestrel courier drone | 1, 2 | [[redirect]] |
| [[aldous-wick]] | Meridian ledger terminal | 1, 2, 3 | [[arm-halt\|armHalt]] |
| [[wren-tallis]] | studio master ledger | 1, 2 | [[ward]] |
| [[bram-hollander]] | Copperline register hub | 2, 3 | [[lock]] |
| [[dex-marlowe]] | Nocta cram deck | 2, 3 | [[redirect]] |
| [[june-aksoy]] | Halcyon clinic gateway | 3, 4 | [[ward]] |
| [[ines-calloway]] | Ferrox lifter exosuit | 3, 4 | [[arm-halt\|armHalt]] |
| [[emeric-snow]] | Ivora chess cabinet | 4, 5 | [[purge]] |
| [[vera-stanek]] | Apothek dosage safe | 4, 5 | [[arm-siphon\|armSiphon]] |
| [[casimir-bell]] | Ledgerstone pawn vault | 4, 5 | [[lock]] |
| [[noor-behzadi]] | Polyverb synth brain | 4, 5 | [[purge]] |

All six modes appear twice across the roster, and tier bands overlap so any given day can draw a plausible three.

## The "One Wow"

Each profile is supposed to carry exactly one memorable thing. Not a backstory: a **device plus a complaint plus a routine** that makes the dive feel specific. "A ghost second player keeps setting records" is a wow. "Arcade kid with a broken handheld" is not.

Owned by the [[encounter-generator]].

## Dominant is a promise

`dominant` is the mode the Analyze diagnostic reports, and the machine is guaranteed to use it early. **The tell is always honest.** That is what makes reading the [[inbox|ticket]] a real decision. See [[traps-and-telegraphs]].

## Copy rules

- Customers are **fond of their machines**. The intrusion is a betrayal, not an inconvenience.
- `winLine`: relief, with personality.
- `lossLine`: **one cold sentence** in the shop's ledger voice.

See [[voice-and-copy-laws]].

## Appearance canon

Only where art has needed it. Ruled for [[juno-vex]], [[sable-okonkwo]], [[aldous-wick]], [[wren-tallis]] and [[bram-hollander]]; [[dex-marlowe]]'s is established by shipped card art.

> [!warning] An unlisted customer has no likeness yet. Invent nothing without a ruling.

Twelve customers share six portrait assets (`/assets/px/portraits/cust-01..06.png`).

## MOST LETHAL

[[ledger-log]] tracks whichever customer's device has ended the most runs. It is the closest thing the game has to a nemesis, and it is emergent rather than authored. See [[scoring-and-lifetime-stats]].

## See also

- [[the-finale-encounter]] · [[inbox]]
