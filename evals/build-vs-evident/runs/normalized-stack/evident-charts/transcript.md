# Live run: evident-charts (talk-build) — normalized stack

Skill: `skills/evident-charts/SKILL.md` + `references/talk-build.md`. Same answers as build-my-chart.

## Transcript

| Step | Agent question | User answer |
| --- | --- | --- |
| 0 | Explore or communicate? | Communicate. (Message, audience, comparison recorded per talk-build.) |
| 1 | Dataset and columns? | Synthetic CSV; category, level, value. Agent summarized rows and types. |
| Brief | (internal) | Takeaway: mid/high dominate share \| Audience: teammate \| Destination: blog |
| 4 | Mark? | Horizontal bars. |
| 5 | Encodings? | y=category, x=share, color=level. |
| 6 | Normalize stack? | Yes, within category. |
| 8 | Palette? | Ordered levels → sequential blues/gray ramp in matplotlib (C3 within 4 hues). |
| 12 | Title states takeaway? | Yes — mid and high carry most value. |
| 13 | Misread + checks? | Percent vs absolute flagged; `check_chart` not run in-session (no committed script yet). |

## Final output

`final_chart.py` → matplotlib PNG via `render_charts.py`.