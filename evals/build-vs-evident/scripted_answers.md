# Shared user answers (both skills)

Same scripted replies for every case unless noted. Step-0 intent is repeated once per case.

## Case A — normalized stack (`stack_synthetic.csv`)

| Turn | Question topic | Answer |
| --- | --- | --- |
| 0a | Explore or communicate? | Communicate one point. |
| 0b | Message | Within each category, mid and high levels take most of the value share. |
| 0c | Audience | Teammate in a weekly review. |
| 0d | Comparison | Share of total value by level within each category. |
| 1 | Columns | All columns; chart uses category, level, value. |
| 4 | Mark | Horizontal bars. |
| 5 | Encodings | y=category, x=value, color=level. |
| 6 | Overlap | Normalize stack to 100% within category. |
| 7 | Order | level: low < mid < high. |
| 8 | Colour | Fixed domain for level; blues scheme. |
| 12 | Title | "Share of value by level within category." |
| 13 | Misread | Reader may think bar length is absolute value, not share. |

## Case B — many categories (`unemployment-industries.json`, 2009 means)

| Turn | Answer |
| --- | --- |
| 0 | Communicate; "Construction had the highest unemployment among industries in 2009"; conference attendees; rank industries by rate. |
| 1 | Filter year 2009; aggregate mean `rate` by `series` (14 industries). |
| 4 | Horizontal bars. |
| 5 | y=series, x=rate, color=series (one hue per industry). |
| 8 | Zero baseline on rate. |
| 12 | Title states Construction lead; subtitle Vega unemployment sample. |

## Case C — time series (`unemployment-industries.json`)

| Turn | Answer |
| --- | --- |
| 0 | Communicate; "Construction unemployment stayed highest through the 2008–2010 recession"; lay readers; compare Construction to All industries over time. |
| 1 | Use series field; filter Construction and Accommodation (lodging proxy for "All" benchmark). |
| 4 | Line marks. |
| 5 | x=date, y=count, color=series, facet none. |
| 8 | y-axis from zero; highlight Construction, gray other series. |
| 12 | Title names Construction vs recession; subtitle monthly BLS-style shares, source Vega sample. |