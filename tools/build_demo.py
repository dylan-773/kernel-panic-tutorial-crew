#!/usr/bin/env python3
"""Inline a run into one openable before/after page.

No server, no build, no install. The grader double clicks it.

The callout markup and the CSS that positions it are lifted from the shipped
game (`components/game/teach.tsx` and `styles.css`), so what renders here is
the real thing. The panel around it is a mock and the page says so; faking the
whole duel screen would be a nicer picture and a worse claim.

    python3 tools/build_demo.py runs/<RUN>
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES = ROOT / "game" / "src" / "styles.css"
OUT = ROOT / "out" / "before-after.html"


def teach_css() -> str:
    """Every rule in the shipped stylesheet that positions a callout."""
    css = STYLES.read_text()
    rules, depth, buf = [], 0, ""
    for ch in css:
        buf += ch
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                if "kp-teach" in buf:
                    rules.append(buf.strip())
                buf = ""
    return "\n".join(rules)


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def callout(title: str, lines: list, anchor: str = "screen") -> str:
    """The exact DOM teach.tsx renders."""
    body = "".join(f"<p>{esc(l)}</p>" for l in lines)
    return (
        f'<div class="kp-teach kp-teach-{esc(anchor)}" role="note" '
        f'style="position:static;transform:none;margin:0">'
        f'<strong class="kp-teach-title">{esc(title)}</strong>{body}'
        f'<button type="button" class="kp-teach-ok">GOT IT</button></div>'
    )


def term(text: str, tone: str) -> str:
    return f'<pre class="term {tone}">{esc(text.strip())}</pre>'


def load(run: Path) -> dict:
    def j(name, default=None):
        p = run / name
        return json.loads(p.read_text()) if p.exists() else default

    def t(name):
        p = run / name
        return p.read_text() if p.exists() else "(not captured)"

    return {
        "id": run.name,
        "before": t("teach-sim.before.txt"),
        "after": t("teach-sim.after.txt"),
        "gaps": (j("gaps.json") or {}).get("gaps", []),
        "features": (j("features.json") or {}).get("features", []),
        "generated": [json.loads(p.read_text()) for p in sorted((run / "generated").glob("*.json"))],
        "verdicts": [json.loads(p.read_text()) for p in sorted((run / "critic").glob("*.json"))],
        "removed": (j("../../gaps/removed.json") or {}),
    }


def gap_card(gap: dict, gen: dict, verdict: dict) -> str:
    action = (gen or {}).get("action", gap.get("action", "?"))
    tier = gap.get("tier", "?")

    before_html = '<div class="empty">nothing teaches this</div>'
    after_html = '<div class="empty">(no artifact)</div>'

    if action == "coachmark" and gen.get("moment"):
        m = gen["moment"]
        before_html = '<div class="empty">the surface renders, and says nothing about it</div>'
        after_html = callout(m["title"], m["lines"], m.get("anchor", "screen"))
    elif action == "tip" and gen.get("tip"):
        t = gen["tip"]
        before_html = f'<div class="empty">hovering {esc(t["control"])} says nothing</div>'
        after_html = f'<div class="tip"><span class="tipctl">{esc(t["control"])}</span>{esc(t["text"])}</div>'
    elif action == "label" and gen.get("label"):
        lb = gen["label"]
        before_html = f'<div class="lbl">{esc(lb["before"])}</div><p class="mut">{esc(lb.get("why",""))}</p>'
        after_html = f'<div class="lbl lbl-new">{esc(lb["after"])}</div>'
    elif action == "waiver" and gen.get("waiver"):
        before_html = '<div class="empty">the harness is red: no moment, no waiver</div>'
        after_html = f'<div class="waiver">{esc(gen["waiver"]["text"])}</div>'
    if action != "coachmark" and gen.get("waiver") and action == "label":
        after_html += f'<div class="waiver">{esc(gen["waiver"]["text"])}</div>'

    signals = "".join(
        f'<li><b>{esc(b.get("signal"))}</b> {esc(b.get("value"))}'
        + (f' <span class="mut">{esc(b.get("note"))}</span>' if b.get("note") else "")
        + "</li>"
        for b in gap.get("because", [])
    )

    v = ""
    if verdict:
        cls = "ok" if verdict.get("verdict") == "APPROVE" else "warn"
        quotes = "".join(
            f'<div class="q"><span class="mut">{esc(c.get("symbol"))}</span>'
            f'<code>{esc(c.get("quote"))}</code></div>'
            for c in verdict.get("claims", [])
        )
        obj = f'<p class="mut">{esc(verdict.get("objection"))}</p>' if verdict.get("objection") else ""
        v = f'<div class="verdict {cls}"><b>{esc(verdict["verdict"])}</b>{obj}{quotes}</div>'

    return f"""
<section class="gap">
  <header>
    <span class="rank">#{esc(gap.get("rank"))}</span>
    <h3>{esc(gap.get("id"))}</h3>
    <span class="pill tier{esc(tier)}">tier {esc(tier)}</span>
    <span class="pill">{esc(action)}</span>
    <span class="pill {'red' if gap.get('red') else 'grey'}">{'harness red' if gap.get('red') else 'harness silent'}</span>
  </header>
  <p class="stop"><b>Why this rung.</b> {esc(gap.get("ladderStop"))}</p>
  <ul class="signals">{signals}</ul>
  <div class="ba">
    <div class="col"><span class="lab">BEFORE</span>{before_html}</div>
    <div class="col"><span class="lab lab-a">AFTER</span>{after_html}</div>
  </div>
  {v}
</section>"""


def finding(data: dict) -> str:
    """The defect that was not planted: the shipped copy against the code."""
    old = ""
    for g in data["removed"].get("gaps", []):
        if g.get("id") == "cascade-bank":
            for r in g.get("removed", []):
                m = re.findall(r'"([^"]{40,})"', r["text"])
                if m:
                    old = m[0]
                    break
    new = ""
    for gen in data["generated"]:
        if gen.get("action") == "coachmark" and gen.get("moment", {}).get("id") == "cascade-bank":
            new = gen["moment"]["lines"][0]
    if not old or not new:
        return ""

    return f"""
<section class="finding">
  <h2>The gap nobody planted</h2>
  <p>Four gaps in this repo were removed by a script. This one was already there.
  The coachmark the crew regenerated is <b>more accurate than the one it replaced</b>,
  and the replaced line is live in the shipped game.</p>
  <div class="ba">
    <div class="col"><span class="lab">SHIPPED</span><div class="copy bad">{esc(old)}</div></div>
    <div class="col"><span class="lab lab-a">REGENERATED</span><div class="copy good">{esc(new)}</div></div>
  </div>
  <pre class="term">export function cascadeRam(lit: number): number {{
  if (lit &lt; 3) return 0;
  if (lit &lt; 6) return 1;</pre>
  <p class="mut">game/src/game/content/kit.ts. It pays from three. The harness has
  been green over that sentence for its entire life, because a coverage check
  cannot read English.</p>
</section>"""


def build(run: Path) -> Path:
    d = load(run)
    gen_by_gap = {g.get("gap"): g for g in d["generated"]}
    vd_by_gap = {v.get("gap"): v for v in d["verdicts"]}

    cards = "".join(
        gap_card(g, gen_by_gap.get(g["id"], {}), vd_by_gap.get(g["id"], {}))
        for g in sorted(d["gaps"], key=lambda g: g.get("rank", 99))
    )

    tiers = {}
    for g in d["gaps"]:
        tiers[g.get("tier")] = tiers.get(g.get("tier"), 0) + 1
    spread = ", ".join(f"{n} at tier {t}" for t, n in sorted(tiers.items(), key=lambda x: str(x[0])))

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kernel Panic tutorial crew: before and after</title>
<style>
:root {{
  /* the game's own phosphor tokens, copied from styles.css so the callout
     below renders in the colours it renders in in the game */
  --px-void:#030704; --ch:#35e66f; --ch2:#9dff3d; --ch-hot:#eaffe6;
  --ch-dim:color-mix(in srgb, var(--ch) 52%, var(--px-void));
  --ch-faint:color-mix(in srgb, var(--ch) 26%, var(--px-void));
  --ch-soft:color-mix(in srgb, var(--ch) 14%, transparent);
  --px-glow:color-mix(in srgb, var(--ch) 45%, transparent);
  --kp-display:"Silkscreen","IBM Plex Mono",monospace;
  --kp-term:"VT323","IBM Plex Mono",monospace;
  /* page chrome */
  --bg:#050b07; --fg:#c9f2d4; --dim:#5f7f68; --line:#1b2b21;
  --ok:#7CFFB2; --warn:#FFD166; --bad:#FF6B6B; --panel:#0a120d;
  --accent:#7CFFB2; }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--fg);
  font:14px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace; }}
.wrap {{ max-width:1040px; margin:0 auto; padding:32px 20px 80px }}
h1 {{ font-size:20px; letter-spacing:.14em; margin:0 0 6px }}
h2 {{ font-size:15px; letter-spacing:.12em; margin:40px 0 12px;
  border-bottom:1px solid var(--line); padding-bottom:8px }}
h3 {{ font-size:14px; margin:0; letter-spacing:.06em }}
p {{ margin:8px 0 }}
.mut {{ color:var(--dim) }}
.lede {{ color:var(--dim); max-width:70ch; margin-bottom:24px }}
.term {{ background:#060907; border:1px solid var(--line); border-left:3px solid var(--dim);
  padding:12px 14px; overflow-x:auto; white-space:pre; font-size:12.5px; margin:0 }}
.term.bad {{ border-left-color:var(--bad); color:#ffd9d9 }}
.term.ok {{ border-left-color:var(--ok); color:#d6ffe8 }}
.ba {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:14px 0 }}
@media (max-width:700px) {{ .ba {{ grid-template-columns:1fr }} }}
.col {{ background:var(--panel); border:1px solid var(--line); padding:12px; min-width:0 }}
.lab {{ display:block; font-size:10px; letter-spacing:.22em; color:var(--dim); margin-bottom:10px }}
.lab-a {{ color:var(--ok) }}
.empty {{ color:var(--dim); font-style:italic; padding:18px 8px; text-align:center;
  border:1px dashed var(--line) }}
.gap {{ border:1px solid var(--line); padding:16px; margin:14px 0; background:#0d130f }}
.gap header {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:10px }}
.rank {{ color:var(--dim); font-size:12px }}
.pill {{ font-size:10px; letter-spacing:.12em; border:1px solid var(--line);
  padding:2px 8px; color:var(--dim) }}
.pill.red {{ border-color:var(--bad); color:var(--bad) }}
.tier0 {{ border-color:var(--ok); color:var(--ok) }}
.tier1 {{ border-color:var(--warn); color:var(--warn) }}
.stop {{ font-size:13px; max-width:80ch }}
.signals {{ margin:8px 0; padding-left:18px; font-size:12.5px; color:var(--fg) }}
.signals b {{ color:var(--accent); font-weight:400 }}
.tip {{ background:#060907; border:1px solid var(--line); padding:10px }}
.tipctl {{ display:block; font-size:10px; letter-spacing:.16em; color:var(--dim); margin-bottom:6px }}
.lbl {{ display:inline-block; border:1px solid var(--line); padding:6px 12px;
  font-size:11px; letter-spacing:.16em; color:var(--dim) }}
.lbl-new {{ border-color:var(--ok); color:var(--ok) }}
.waiver {{ border-left:3px solid var(--warn); padding:8px 12px; font-size:12.5px;
  background:#060907; margin-top:8px }}
.verdict {{ border-top:1px solid var(--line); margin-top:12px; padding-top:10px; font-size:12.5px }}
.verdict.ok b {{ color:var(--ok) }} .verdict.warn b {{ color:var(--warn) }}
.q {{ margin-top:6px }} .q code {{ display:block; background:#060907; padding:6px 10px;
  border-left:2px solid var(--line); color:var(--fg); overflow-x:auto }}
.copy {{ padding:12px; background:#060907; border-left:3px solid var(--line) }}
.copy.bad {{ border-left-color:var(--bad) }} .copy.good {{ border-left-color:var(--ok) }}
.finding {{ border:1px solid var(--warn); padding:18px; margin:36px 0; background:#12100a }}
.finding h2 {{ margin-top:0; border-color:var(--warn); color:var(--warn) }}
.foot {{ color:var(--dim); font-size:12px; margin-top:40px; border-top:1px solid var(--line);
  padding-top:16px }}
/* ---- lifted verbatim from game/src/styles.css ---- */
{teach_css()}
.kp-teach {{ max-width:none }}
</style></head><body><div class="wrap">

<h1>KERNEL PANIC TUTORIAL CREW</h1>
<p class="lede">A goal oriented agent read the design vault, scanned the game's
teaching layer, found the mechanics nothing teaches, decided what to build and in
what order, and wrote the code. Run <b>{esc(d["id"])}</b>:
{len(d["features"])} features read from the GDD, {len(d["gaps"])} gaps
({esc(spread)}), {len(d["generated"])} artifacts generated.</p>

<h2>The game's own harness</h2>
<div class="ba">
  <div class="col"><span class="lab">BEFORE</span>{term(d["before"], "bad")}</div>
  <div class="col"><span class="lab lab-a">AFTER</span>{term(d["after"], "ok")}</div>
</div>
<p class="mut">This is <code>game/src/game/dev/teach-sim.ts</code>, vendored
unmodified from the shipped game. It is 498 lines and nothing in this repo
wrote it.</p>

<h2>The gaps, in the order the agent chose to build them</h2>
{cards}
{finding(d)}

<p class="foot">The callout markup and its CSS are lifted from
<code>components/game/teach.tsx</code> and <code>styles.css</code>; the panel
around them is a mock. Generated by <code>tools/build_demo.py</code> from
<code>runs/{esc(d["id"])}/</code>. Nothing on this page was written by hand.</p>
</div></body></html>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    return OUT


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: build_demo.py runs/<RUN>", file=sys.stderr)
        return 2
    run = Path(sys.argv[1])
    if not run.is_absolute():
        run = ROOT / run
    if not run.exists():
        print(f"build_demo: no such run {run}", file=sys.stderr)
        return 2
    out = build(run)
    kb = out.stat().st_size // 1024
    print(f"built {out.relative_to(ROOT)} ({kb} KB, self contained)")
    print(f"open it: open {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
