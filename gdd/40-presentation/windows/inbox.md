---
title: INBOX
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[customers]]", "[[traps-and-telegraphs]]", "[[law-11-panel-queue]]"]
---

# INBOX

`inbox` · `windows/inbox.tsx`

The job board and the CUSTOMER.REC card. Fronts the day loop and launches the dive.

## What it shows

- **Three tickets**, takeable in any order.
- Per ticket: the [[customers|customer]], the device, the **threat pips** (job tier 1 to 5), and the **dominant-routine tell**.
- A **head-start RISK warning** where `headStart` is non-zero.
- The DIVE button.

Two widths, `INBOX_W_LIST` and `INBOX_W_CARD`, because the collapsed list and the expanded customer record are genuinely different surfaces rather than one surface with a detail pane.

## The tell is the whole point

The dominant-mode line is **honest**, always, and the machine is guaranteed to use that mode early. `MODE_TELL` carries the six lines. See [[traps-and-telegraphs]].

That honesty is what makes ticket order a real decision: a `redirect` job and an `armHalt` job want different kits, and the player can see which is which before committing [[ram]] or [[neural-strain|strain]].

## Teaching

`analyze-readout` (order **20**, the earliest coachmark in the game) fires here on first sight, teaching `analyzeTell` and `threatTier` together. It is first because everything downstream depends on the player believing the diagnostic. See [[coachmarks]].

## The design problem it carries

> [!warning] Two focal candidates
> The customer card and the DIVE button both want to be the one big thing. [[law-2-hierarchy]] requires the glance order be decided **before** the panel is built, and this is the surface where that decision is hardest.

## See also

- [[customers]] · [[core-loop]] · [[difficulty-dials]]
