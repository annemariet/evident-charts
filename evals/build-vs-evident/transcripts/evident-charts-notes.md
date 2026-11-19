# evident-charts (+ talk-build mode) — scripted run notes

Skill: this fork's `skills/evident-charts/` with `references/talk-build.md` for one-question steps. Same answers as build-my-chart.

## Normalized stack

- Talk-build asked intent split across turns, then data read, then mark/encodings; finished with matplotlib stack mirroring user normalize choice.
- **Caught:** takeaway title (TI-1); percent axis; ordered levels; white bar edges (C17); misread noted in step 13.
- **Missed:** slower path (no native Altair in default stack); did not run `check_chart.py` on a committed script in this eval folder (Chrome/SVG checks skipped in agent-less replay).

## Many categories (14 industries)

- After user requested 14 legend hues, agent applied C2 override: highlight Construction, gray others (one accent on gray).
- **Caught:** >10 category palette problem; legend replaced with semantic highlight; zero baseline; title states Construction lead.
- **Missed:** talk-build step cadence is longer than build-my-chart's fixed 13-step table; less Altair grammar teaching per turn.

## Time series

- Highlight Construction (#D55E00), gray comparator; y from zero; recession framing in title.
- **Caught:** visual emphasis matches communicate intent (C2); axis zero for share-like rates (H1 context).
- **Missed:** did not flag Jan–Feb 2010 as truncated end of sample; no automated time-axis check without exported SVG + Chrome.