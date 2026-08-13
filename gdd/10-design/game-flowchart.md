---
title: Game flowchart
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[core-loop]]", "[[save-and-load]]", "[[title-and-start-screen]]"]
---

# Game flowchart

> [!info] Source
> `save.ts:RunScreen`, `run-reducer.ts` transitions.

## Boot to run

```mermaid
flowchart TB
  BIOS[BIOS boot] --> LOGIN[Login: 3 save slots]
  LOGIN --> DESK[KP/OS desktop]
  DESK --> OPEN[opener]
  OPEN -->|run 1 only| TI[tutIntro]
  TI --> TUT[tutorial dive]
  TUT --> TO[tutOutro]
  TO --> DO[dayOpen]
  OPEN -->|run 2+| DO
```

## The day

```mermaid
flowchart TB
  DO[dayOpen] --> DAY[day: three tickets]
  DAY -->|pickJob| AN[analyze]
  AN -->|startDuel| DU[duel]
  DU -->|duelFinished| CHK{strain > 0?}
  CHK -->|no| RE[runEnd]
  CHK -->|yes| RES[result: pay, strain, draft]
  RES -->|pickAugment, resultNext| BACK{3 tickets done?}
  BACK -->|no| DAY
  BACK -->|yes| UP[upgrade: night pick + shop]
  UP -->|closeNight| NEXT{day < 10?}
  NEXT -->|yes| DO
  NEXT -->|no| FP[finalePre]
  FP --> FD[finale dive]
  FD -->|win| FW[finaleWin]
  FD -->|lose| RE
```

## Screens

`opener` · `tutIntro` · `tutorial` · `tutOutro` · `dayOpen` · `day` · `analyze` · `duel` · `result` · `upgrade` · `finalePre` · `runEnd` · `finaleWin`

Plus `build`, which is **vestigial**: nothing routes to it any more. It is the cut mandatory build stop. See [[design-change-log]].

## Two things the diagram does not show

**Refresh is a safe abort.** Transient screens are never resumed into. Reloading mid-dive puts you back at the day, not into a corrupted duel. See [[save-and-load]].

**The night is two-step.** `chooseUpgrade` sets the pick without ending the night; `closeNight` commits and refuses without a pick. So the shop stays open while you reconsider. See [[the-night-shop]].

## See also

- [[core-loop]] · [[kp-os]]
