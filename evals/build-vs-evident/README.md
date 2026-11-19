# build-my-chart vs evident-charts eval

Not a CI harness. **Walk-throughs** (not live agent sessions) live under `walkthroughs/<case>/{build-my-chart|evident-charts}/` (`walkthrough.md` + `final_chart.py`). PNGs replay those finals via `scripts/render_charts.py`; byte-identical PNGs are promised for **two consecutive runs in the same `uv sync --locked` environment**, not across arbitrary machines.

- **Data:** `data/stack_synthetic.csv` (**synthetic**); `data/unemployment-industries.json` (Vega public).
- **Answers:** `scripted_answers.md`.
- **Summary:** [EVALUATION.md](../../EVALUATION.md).