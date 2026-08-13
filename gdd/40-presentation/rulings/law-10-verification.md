---
title: Law 10 - Verification
status: canon
source: rulings
owner: ux-agent
updated: 2026-08-05
related: ["[[ui-rulings]]", "[[verification-gate]]", "[[law-9-build-recipe]]"]
---

# Law 10 - Verification

The Chrome extension is often unavailable. **Drive headless Chrome over CDP instead**, which is the better harness anyway because it clicks the demo's own rig and measures real geometry.

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --remote-debugging-port=9222 \
  --user-data-dir=<scratch> about:blank
```

Then a bun script over the `webSocketDebuggerUrl` from `/json/list`, using `Runtime.evaluate` and `Page.captureScreenshot`.

## Four gotchas that cost real time

1. **Let the load choreography settle (~2.5s) before reading text.** Count-ups and typewriters read as `0` or empty mid-flight and look like failures.
2. **Divide out ancestor transforms.** Anything under a `transform: scale()` returns inflated `getBoundingClientRect()` values. Measure with the tube OFF; layout is identical in every CRT mode.
3. **Frame timing:** sample `requestAnimationFrame` deltas over 400+ frames and report mean, p50, p95 and worst per mode.
4. **Keep TypeScript annotations out of strings you evaluate in the page.** They are not valid JS there and the evaluate throws.

## The standing acceptance checklist

Every panel, every time:

- [ ] The focal element is **measurably** the largest text
- [ ] No internal scrollbar
- [ ] No `border-radius` on UI chrome
- [ ] No em or en dash
- [ ] Both schemes resolve all eight roles distinctly
- [ ] Every viewport renders the same arrangement and fits its desk
- [ ] The sparse run state occupies the same footprint as the full one
- [ ] Reduced motion renders the settled state in one frame

## The principle

Every item is **measured, not eyeballed**. "The focal element is measurably the largest text" is a `getBoundingClientRect` assertion, not an opinion. That is the same standard the game's own [[verification-gate]] holds balance claims to.

## See also

- [[law-7-motion]] · [[verification-gate]]
