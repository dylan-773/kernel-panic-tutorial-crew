# Deferred items, run 2026-08-13-d

These four artifacts were authored for the uninventoried mechanics the
gap-prioritizer surfaced (oneUndo, builtVsPower, splitBoards, winConditions).
They fail verify_teaching.py with "unknown mechanic" because no
MECHANIC_INVENTORY row exists for any of them, and the teaching-author traced
the full toolchain and found no path that lets a generated file introduce a
new mechanic id and reference it in the same pass:

- verify_teaching.py checks every tip.teaches and waiver.id against the
  inventory scanned from the current, unmodified game/, and never accounts
  for a pending label insertion.
- apply_patch.py runs add_waiver() in its first loop against pre-batch file
  content, before any label edit that would insert the row, so the batch
  would roll back even if the check were passed.

Closing these needs either the checker or the patcher taught about pending
inventory insertions, or the four bare MECHANIC_INVENTORY rows seeded by
whoever owns game/. Neither is a teaching-author action, and the orchestrator
does not hand edit game/. Deferred, not dropped: the artifacts are kept here
verbatim for a future cycle.

None of the four is red in the harness; the five artifacts that shipped cover
all five mechanics teach-sim names.
