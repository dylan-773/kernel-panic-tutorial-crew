---
title: Law 11 - Panel queue
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[40-presentation]]"]
---

# Law 11 - Panel queue

The worklist. [[loadout-cfg]] (`loadout-eva`) is the reference; the rest are independent.

| Panel | Shipped component | The hard part |
|---|---|---|
| [[inbox]] | `windows/inbox.tsx` | Fronts the day loop; owns the CUSTOMER.REC card and the DIVE button. **Two focal candidates**, so the glance order needs deciding first. |
| [[repair-log]] | `windows/report.tsx` | Already dense. The verdict is the obvious focal element; the ECG strain trace is a natural `--r-warn` surface. |
| [[solder-bay]] | `windows/solder.tsx` | Drag-to-craft, interaction-heavy, so the **motion budget matters most here**. |
| [[dad-log-window]] | `windows/dadlog.tsx` | Long documents, so **paging discipline** is the constraint. |
| [[darknet-lnk]] | `windows/darknet.tsx` | Deliberately the odd one out **via stepped-notch chrome, not colour**. Keep that. |
| [[manual-txt]] | `windows/manual.tsx` | Tabbed reference; the **18-card AUGMENTS page** is the hard case. |
| [[night-sys]] | `windows/night.tsx` | Small surface; a candidate for proving the system at **low density**. |
| [[ledger-log]] | `windows/ledger.tsx` | Small, table-shaped. |
| [[dive-exe]] | full-screen duel | **LAST.** Full-screen, real-time, and the machine's two-beat telegraph must stay readable. **It does not follow the window rules.** |

> [!warning] This list goes stale
> Ten v3 panels were integrated on 2026-08-01. The queue above is the spec's own copy and has not been reconciled since. Check `ui-demos/manifest.json` for live status; it is durable and is never cleared between cycles.

## Two notes worth keeping even after the queue empties

**INBOX has two focal candidates.** A surface where the customer card and the dive button both want to be the one big thing is precisely the case [[law-2-hierarchy]] exists for.

**DIVE.EXE is exempt.** It is full-screen and its own thing, and the telegraph readability constraint outranks the panel system. Doing it last is deliberate.

## See also

- [[ui-rulings]] · [[law-9-build-recipe]]
