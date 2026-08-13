/**
 * What the teaching layer currently contains, and what it mounts.
 *
 * This imports the real `content/teaching.ts` rather than parsing it. A regex
 * over TypeScript would drift the moment the formatting changed, and the whole
 * point of this repo is that the code is the authority.
 *
 *   bun tools/code_scan.ts            summary
 *   bun tools/code_scan.ts --json     the full scan
 */

import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative } from "node:path";

import { FINAL_DAY } from "../game/src/game/content/arc";
import {
  MECHANIC_INVENTORY,
  TEACHING,
  TEACH_TIPS,
  TUTORIAL_BEATS,
  taughtMechanics,
} from "../game/src/game/content/teaching";

const ROOT = join(import.meta.dir, "..");
const COMPONENTS = join(ROOT, "game", "src", "components");

/** Caps the harness enforces. Mirrored from dev/teach-sim.ts. */
const MAX_FIRST_SIGHT_PER_SURFACE = 2;
const MAX_MOMENTS_PER_SURFACE = 4;

function walk(dir: string): string[] {
  const out: string[] = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else if (p.endsWith(".tsx")) out.push(p);
  }
  return out;
}

/** Every `<Teach id="...">` actually rendered, and where. */
function mounts() {
  const found: { id: string; file: string; line: number; text: string }[] = [];
  for (const file of walk(COMPONENTS)) {
    const lines = readFileSync(file, "utf8").split("\n");
    lines.forEach((text, i) => {
      const m = text.match(/<Teach\s+id="([^"]+)"/);
      if (m) {
        found.push({
          id: m[1],
          file: relative(join(ROOT, "game"), file),
          line: i + 1,
          text: text.trimEnd(),
        });
      }
    });
  }
  return found;
}

const taught = taughtMechanics();
const mounted = mounts();
const mountedIds = new Set(mounted.map((m) => m.id));

const uncovered = MECHANIC_INVENTORY.filter(
  (m) => !taught.has(m.id) && !(m.waiver && m.waiver.length >= 20),
);
const waived = MECHANIC_INVENTORY.filter((m) => m.waiver && m.waiver.length >= 20);

/** A moment in the data with no mount renders nothing. The harness cannot see this. */
const unmounted = TEACHING.filter((m) => !mountedIds.has(m.id));
const orphanMounts = mounted.filter((m) => !TEACHING.some((t) => t.id === m.id));

const surfaces: Record<string, { moments: number; firstSight: number; ids: string[] }> = {};
for (const m of TEACHING) {
  const s = (surfaces[m.surface] ??= { moments: 0, firstSight: 0, ids: [] });
  s.moments += 1;
  if (m.when === "firstSight") s.firstSight += 1;
  s.ids.push(m.id);
}

const usedOrders = TEACHING.map((m) => m.order).sort((a, b) => a - b);
const freeOrders: number[] = [];
for (let n = 10; n <= 120 && freeOrders.length < 20; n += 1) {
  if (!usedOrders.includes(n)) freeOrders.push(n);
}

const scan = {
  schema: "kp-code-scan/1",
  limits: {
    finalDay: FINAL_DAY,
    maxCoachLine: 160,
    maxLines: 2,
    maxTipLen: 130,
    surfaces: [
      "tutorial", "duel", "day", "analyze", "loadout",
      "solder", "result", "upgrade", "finalePre", "runEnd", "desktop",
    ],
    whens: [
      "firstSight", "overPar", "holdingCells", "cascadeBanked",
      "draftOffered", "craftReady", "swapOffered",
    ],
    anchors: ["readout", "rows", "draft", "par", "screen", "patch", "grid", "craft"],
  },
  inventory: MECHANIC_INVENTORY.map((m) => ({
    id: m.id,
    label: m.label,
    firstContact: m.firstContact,
    waiver: m.waiver ?? null,
    waiverPremise: m.waiverPremise ?? null,
    covered: taught.has(m.id),
  })),
  moments: TEACHING.map((m) => ({
    id: m.id,
    teaches: m.teaches,
    surface: m.surface,
    when: m.when,
    anchor: m.anchor,
    order: m.order,
    notBeforeDay: m.notBeforeDay,
    title: m.title,
    lines: m.lines,
    mounted: mountedIds.has(m.id),
  })),
  tips: TEACH_TIPS.map((t) => ({ id: t.id, teaches: t.teaches, control: t.control, text: t.text })),
  beats: TUTORIAL_BEATS.map((b) => ({ id: b.id, teaches: b.teaches, line: b.line })),
  mounts: mounted,
  gaps: {
    uncovered: uncovered.map((m) => ({
      id: m.id,
      label: m.label,
      firstContact: m.firstContact,
    })),
    unmounted: unmounted.map((m) => m.id),
    orphanMounts: orphanMounts.map((m) => `${m.id} (${m.file}:${m.line})`),
  },
  budget: {
    maxFirstSightPerSurface: MAX_FIRST_SIGHT_PER_SURFACE,
    maxMomentsPerSurface: MAX_MOMENTS_PER_SURFACE,
    surfaces,
  },
  orders: { used: usedOrders, free: freeOrders },
  counts: {
    mechanics: MECHANIC_INVENTORY.length,
    covered: MECHANIC_INVENTORY.length - waived.length - uncovered.length,
    waived: waived.length,
    uncovered: uncovered.length,
    moments: TEACHING.length,
    tips: TEACH_TIPS.length,
    beats: TUTORIAL_BEATS.length,
  },
};

if (process.argv.includes("--json")) {
  console.log(JSON.stringify(scan, null, 2));
} else {
  const c = scan.counts;
  console.log(
    `${c.mechanics} mechanics: ${c.covered} covered, ${c.waived} waived, ${c.uncovered} UNCOVERED`,
  );
  console.log(`${c.moments} moments, ${c.tips} tips, ${c.beats} beats, ${mounted.length} mounts\n`);

  if (uncovered.length) {
    console.log("uncovered:");
    for (const m of uncovered) console.log(`  ${m.id.padEnd(16)} ${m.label}  (first contact: ${m.firstContact})`);
    console.log("");
  }
  if (unmounted.length) {
    console.log("in the data but never rendered (the harness cannot see this):");
    for (const m of unmounted) console.log(`  ${m.id}`);
    console.log("");
  }
  if (orphanMounts.length) {
    console.log("mounted but not in the data:");
    for (const m of orphanMounts) console.log(`  ${m}`);
    console.log("");
  }

  console.log("per surface (cap 2 firstSight, 4 total):");
  for (const [name, s] of Object.entries(surfaces).sort()) {
    const flag = s.firstSight >= MAX_FIRST_SIGHT_PER_SURFACE ? "  AT FIRSTSIGHT CAP" : "";
    console.log(`  ${name.padEnd(10)} ${s.moments}/4 moments, ${s.firstSight}/2 firstSight${flag}`);
  }
  console.log(`\nfree orders: ${freeOrders.slice(0, 12).join(", ")}`);
}
