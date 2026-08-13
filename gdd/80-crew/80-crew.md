---
title: Crew
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-dev-crew]]", "[[the-pipeline]]", "[[the-gates]]"]
---

# Crew

The AI development crew that produces content for the game.

[[the-dev-crew]] - the org and the principles
[[the-pipeline]] - how work flows
[[the-gates]] - the two questions asked of every artifact
[[the-plays]] - the user-invoked commands
[[token-budget]] - what it cost

## The agents

[[orchestrator]] · [[loremaster]] · [[narrative-director]] · [[encounter-generator]] · [[ability-agent]] · [[arc-composer]] · [[validation]] · [[tutorial-agent]] · [[ux-agent]] · [[art-lead]]

## Memory

Each agent with `memory: project` keeps notes across sessions at `.claude/agent-memory/<agent>/`, symlinked into this vault at `80-crew/memory`.

Those are the agents' own working notes, not canon. Canon lives in [[60-story]].

## See also

- [[verification-gate]] - what the crew's work has to pass
