---
title: DAD.LOG archive
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[ruling-12-dad-log-reframe]]", "[[reveal-schedule]]", "[[dad-log-window]]"]
---

# DAD.LOG archive

> [!info] Source
> `content/journal.ts:JOURNAL_ENTRIES`, ten entries; `DADLOG_CHROME`, `visibleJournal(meta)`.

**Not a diary the player keeps.** An archive reader over DAD.VOL, [[dad]]'s own read-only recovered volume, mounted and read file by file, one more file pieced back with every dive attempt. See [[ruling-12-dad-log-reframe]].

```ts
{ id, unlockAtRun, requiresOpened?, kind: "note"|"bill"|"memo",
  filename, doctype, provenance, title, body: string[], benchNote? }
```

## The ten files

| Unlock | File | Doctype | Title | Provenance |
|---|---|---|---|---|
| run 0 | `WILL.SCN` | SCAN | [[entry-will\|THE WILL]] | scanned paper, taped inside the register, folded in four |
| run 0 | `TICKET_QUERY.LOG` | LOG | [[entry-backroom\|THE BACK ROOM]] | shop system query, bench terminal, day one |
| run 1 | `SESSION_001.LOG` | LOG | [[entry-failed1\|ANOTHER FAILED RUN]] | tower telemetry, first dive, tonight |
| run 2 | `NOTICE_07.SCN` | SCAN | [[entry-bills\|FINAL NOTICE]] | scanned paper, bottom drawer, one of eleven filed under W |
| run 3 | `FRAGMENT_03.REC` | FRAG | [[entry-solder\|SOLDER SMOKE]] | partial recovery, surfaced off a lost dive |
| run 4 | `RECEIPTS.SCN` | SCAN | [[entry-receipts\|RECEIPTS]] | scanned paper, shoebox, pharmacy on 9th, six years of stubs |
| run 5 | `CONSULT_SUMMARY.SCN` | SCAN | [[entry-diagnosis\|THE DIAGNOSIS]] | scanned paper, sealed envelope, never opened until now |
| run 6 | `LEDGER_XREF.QRY` | QUERY | [[entry-notickets\|NO TICKETS]] | ledger cross reference, run twice to be sure |
| run 8 | `SESSION_SUMMARY.LOG` | LOG | [[entry-grading\|IT IS GRADING ME]] | tower telemetry, aggregate, eight sessions logged |
| finale win | `PATCH.SYS` | SYS | [[entry-patch\|PATCH]] | full volume unlocked, recovered whole, the morning after |

Locked entries render as `doctype: DAMAGED`, title `????`, provenance "partial recovery, more passes needed".

## Three kinds of artifact

- **note** - papers. The will, and PATCH.
- **bill** - paperwork from institutions. The notices, the receipts, the consult summary.
- **memo** - machine output. Queries and telemetry.

The mix matters: the story arrives as **documents that already existed**, not as narration. A clinic's billing system and a shop's ledger tell the truth accidentally, because that is all they can do.

## The two voices

Per [[ruling-12-dad-log-reframe]]:

- The **artifact body** prints only what its own diegetic source could plausibly print.
- The **bench annotation** carries the player's inference, comparison or reaction, typographically subordinate, never sharing the artifact's treatment.

An artifact that draws a conclusion is a canon violation.

## Provenance is a ruling

Telemetry about the player's own current dives sits on the same volume as Dad's historical papers, because it is the same machine and the only drive it has. That is legitimate and ruled. What is forbidden is attributing that telemetry to Dad's authorship. See [[ruling-13-dad-vol-provenance]].

## See also

- [[dad-log-window]] - the reader
- [[reveal-schedule]] - the unlock gate
