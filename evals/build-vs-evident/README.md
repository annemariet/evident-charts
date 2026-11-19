# build-my-chart vs evident-charts eval

Not a CI harness. Regenerates PNG pairs and supports [EVALUATION.md](../../EVALUATION.md).

- **Data:** `data/stack_synthetic.csv` (talk-shaped table); `data/unemployment-industries.json` (Vega public sample).
- **Answers:** `scripted_answers.md` (shared across both skills).
- **Transcripts:** `transcripts/` (what each skill caught or missed in scripted replays).
- **Render:** `scripts/render_charts.py` (needs dev deps: Altair, vl-convert, matplotlib).