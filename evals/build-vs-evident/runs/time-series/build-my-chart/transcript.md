# Live run: build-my-chart — Construction vs Leisure and hospitality

## Transcript

| Step | Agent question | User answer |
| --- | --- | --- |
| 0 | Communicate; Construction rate stayed highest vs Leisure and hospitality through 2008–2010. | per script |
| 1 | Filter series | Construction and **Leisure and hospitality**; date and **rate**. (Agent confirmed both present in data.) |
| 4 | Mark | Lines. |
| 5 | x=date, y=**rate**, color=series. | per script |
| 8 | y scale zero on rate? | Yes. |
| 12 | Title | Construction unemployment rate vs leisure and hospitality through the recession. |
| 13 | Sample ends Feb 2010; two series same visual weight. | Agent noted end date; equal colour weight unless user asks emphasis. |

## Final spec

`final_chart.py` — two lines, `rate` on y, axis titled percent.