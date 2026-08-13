---
title: Orchestrator
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-dev-crew]]", "[[the-plays]]", "[[verification-gate]]"]
---

# Orchestrator

**The main session.** Model: Fable 5.

## The only seat that writes code

`kernel-panic-site/` is its exclusive territory. Every other agent proposes structured JSON; the Orchestrator integrates by hand, and `bun run typecheck` is the schema enforcer.

## What it owns

- Integration of every proposal.
- The [[verification-gate]], all four harnesses.
- Deploy, on explicit user OK only.
- This vault.

## Why by hand

A proposal is a suggestion in a schema. Integration is a judgment about whether it fits the game, whether it contradicts something shipped, and whether it is worth the complexity. That judgment is the job, and automating it away would leave a pipeline that produces content nobody chose.

## Cost

36% of the token budget on 3% of the calls: it holds the most context of any seat. See [[token-budget]].

## See also

- [[the-plays]] · [[the-pipeline]]
