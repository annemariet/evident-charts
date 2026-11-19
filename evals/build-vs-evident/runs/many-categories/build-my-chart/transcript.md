# Live run: build-my-chart — 14 industries (2009)

## Transcript

| Step | Agent question | User answer |
| --- | --- | --- |
| 0–0d | Intent (communicate, Construction highest in 2009, conference, rank by rate) | per script |
| 1 | Data path | `unemployment-industries.json`; 2009 mean rate by series (14 rows). |
| 4 | Mark? | Horizontal bars. |
| 5 | Encodings? | y=series, x=rate, color=series. |
| 8 | Colour scheme? | **Agent follow-up (best-practice 8b):** 14 industries need ≤10 hues or shades+accent—use one gray ramp plus Construction accent, or facet? |
| 8 | User reply | Insist on one hue per industry anyway. |
| 8 | Zero baseline? | Yes on rate. |
| 12 | Title | Average unemployment rate by industry in 2009 (Construction on top when sorted). |
| 13 | Misread? | Many similar hues hard to match legend to bars. |

## Final spec

`final_chart.py` — 14 distinct nominal colours (user override after 8b follow-up).