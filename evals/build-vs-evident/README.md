# build-my-chart vs evident-charts eval

Not a CI harness. **Live runs** live under `runs/<case>/{build-my-chart|evident-charts}/` (transcript + `final_chart.py`). PNGs are replays of those finals via `scripts/render_charts.py`.

- **Data:** `data/stack_synthetic.csv` (**synthetic**, talk-shaped table); `data/unemployment-industries.json` (Vega public sample).
- **Answers:** `scripted_answers.md` (shared across both skills per case).
- **Summary:** [EVALUATION.md](../../EVALUATION.md).