---
title: The plays
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-pipeline]]", "[[the-gates]]", "[[verification-gate]]"]
---

# The plays

User-invoked commands. Each is a skill under `.claude/skills/`.

| Play | Does |
|---|---|
| `/kp-produce` | the full production cycle |
| `/kp-balance` | curve plus catalog |
| `/kp-story` | a story pass |
| `/kp-tutorial` | teaching audit and repair |
| `/kp-ui` | a UX pass, **ending at a reviewable demo** |
| `/kp-ui integrate the approved UI demos` | lands approved demos |
| `/kp-art` | fulfils open art orders |
| `/kp-canonize` | rebuilds canon from what shipped |

Plus a workflow, `/kp-balance-loop`: validate, then propose, **no integration**.

## The six iron rules

1. **Only the Orchestrator touches `kernel-panic-site/`.** Agents propose JSON; integration is by hand; `typecheck` enforces the schema.
2. **UI is reviewed before it integrates.** See below.
3. The **Loremaster gates** every outward-facing artifact.
4. The **Tutorial Agent gates** every artifact adding something the player must understand.
5. Ability and curve changes enter **only through the balance loop**, with before and after sim numbers.
6. **Nothing deploys unless [[verification-gate|the gate]] is green.** Deploy only on explicit user OK.
7. Game copy never contains em or en dashes.

## Review before integration

> [!info] A `/kp-ui` cycle ends at something the user can look at
> A demo under `ui-demos/<id>/`, registered in `ui-demos/manifest.json` at `status: awaiting`, reviewed at `http://localhost:4180/kernel-panic-ui` via `bun ui-demos/_review/serve.ts`.
>
> Only `approved` demos are eligible for integration, and integrating flips them to `complete`.

The manifest is **durable**: unlike `pipeline/`, it is never cleared between cycles. That is what makes approval survive a cycle boundary.

## A caution

Concurrent `/kp-ui` sessions contest `BRIEF.md`, the proposals and the manifest. Use cycle-scoped briefs, append-only writes, and last-moment manifest edits.

## See also

- [[the-pipeline]] · [[the-gates]]
