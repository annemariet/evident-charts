# Live run: build-my-chart — normalized stack

Skill: `compute-altair-talk/skills/build-my-chart/SKILL.md`. Data: synthetic `stack_synthetic.csv`. Answers: `scripted_answers.md` case A.

## Transcript

| Step | Agent question | User answer |
| --- | --- | --- |
| 0 | What is the chart for: explore or communicate? | Communicate one point. |
| 0 | What is the message in one sentence? | Within each category, mid and high levels take most of the value share. |
| 0 | Who will read it? | Teammate in a weekly review. |
| 0 | Which comparison matters most? | Share of total value by level within each category. |
| 1 | Which dataset and columns? | `stack_synthetic.csv`; category, level, value. (Agent: 6 rows, 3 levels, no missing.) |
| 4 | Which mark? | Horizontal bars. |
| 5 | Encodings? | y=category, x=value, color=level. |
| 6 | Stack or normalize? | Normalize to 100% within category. |
| 7 | Category order for level? | low < mid < high. |
| 8 | Colour scheme? | Fixed domain for level; blues sequential (ordered levels). |
| 12 | Title? | Share of value by level within category. |
| 13 | Misread risk? | Reader may think bar length is absolute value, not share. |

## Final spec

See `final_chart.py`. Vega-Lite uses `stack: "normalize"`, ordered `level`, `scheme: "blues"` (matches step 8b guidance for **ordered** magnitudes, not categorical rainbow).