---
title: REPAIR.LOG
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[job-pay-and-billing]]", "[[neural-strain]]", "[[augment-drafts]]"]
---

# REPAIR.LOG

`report` · `windows/report.tsx`

The post-dive result, **read as a transaction**.

## The three lines

**CREDITED · BILLED · RECOVERED.** Money in, [[neural-strain|strain]] out, [[patch-pieces|pieces]] recovered.

That framing is the window's whole idea. A repair shop produces an invoice, not a victory screen, so the result of a dive is an accounting document. It is the same move [[ledger-log]] makes with lifetime stats.

## What else it carries

- The **verdict slab**, the obvious focal element.
- The **client line**: `winLine` or `lossLine` from the customer profile.
- The **strain trace** with sparklines, plus the dive log.
- The **3-card [[augment-drafts|augment draft]]**.

## `endReason`

A loss the machine won without ever touching your core needs explaining, and a 2.4 second toast cannot carry that line. So `endReason` is set at finish, **never cleared**, and this window reads it. See [[win-conditions]].

## Teaching

Three coachmarks live here, and their `order` values encode the reading sequence:

| Order | id | Teaches |
|---|---|---|
| 60 | `strain-chip` | why the win cost something |
| 61 | `augment-draft` | the draft and its cadence |
| 62 | `boost-swap` | ejecting an installed boost |

Only one callout renders at a time, so the ordering is what stops the result screen from teaching three things at once. See [[teaching-system]].

## Panel note

Already dense. The verdict is the obvious focal element, and the ECG strain trace is a natural `--r-warn` surface. See [[law-11-panel-queue]].

## See also

- [[job-pay-and-billing]] · [[route-cost-and-par]]
