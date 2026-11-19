# build-my-chart (talk repo skill) — scripted run notes

Reference skill: `annemariet/compute-altair-talk` → `skills/build-my-chart/SKILL.md`. Answers from `../scripted_answers.md`. Rendered PNGs match talk eval style (`final_chart.py` patterns).

## Normalized stack

- Walked steps 0→13 one turn at a time; step cards named grammar elements and cited Vega-Lite stack docs at step 6.
- **Caught:** percent-stack misread (step 13); ordered `level` domain; smallest snippet per step.
- **Missed:** no automated colour-blind check; title left generic unless step 12 answer supplied; no source publisher line beyond filename; blues scheme not challenged at 3 categories.

## Many categories (14 industries)

- Followed user request to colour every industry in the legend (step 5 answer).
- **Caught:** zero baseline on rate at step 8; step 13 could note rainbow legend weight.
- **Missed:** did not flag C2-style >4 hue limit or redundant legend; no highlight path for the stated Construction message; title echoes user words without sharpening the comparison.

## Time series

- Lines with default categorical colour scale for two series (Construction vs Accommodation).
- **Caught:** `scale.zero` on y when user asked; linked-brush pattern not needed.
- **Missed:** no check for partial 2010 endpoint; both series equal visual weight despite communicate intent naming Construction; no `check_svg` or integrity pass.