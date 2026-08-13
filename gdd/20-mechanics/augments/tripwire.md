---
title: TRIPWIRE
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[arm-halt]]", "[[halt-driver]]", "[[augments]]"]
---

# TRIPWIRE

**Boost** · `tripwire` · requires [[halt-driver]]

> Your halt traps also burn 3 RAM off the victim's next active turn.

The forfeited turn plus a drain on the turn after it. This is the `drain` field on the trap record. See [[traps-and-telegraphs]].

Gated by `{ kind: "augment", id: "cfgArmHalt" }`.
