"""build-my-chart walk-through final: two-series rate lines."""
from __future__ import annotations

import json
from pathlib import Path

import altair as alt
import pandas as pd

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE.parents[2] / "data" / "unemployment-industries.json").read_text())
df = pd.DataFrame(raw)
df["date"] = pd.to_datetime(df["date"])
keep = ["Construction", "Leisure and hospitality"]
df = df[df["series"].isin(keep)]

chart = (
    alt.Chart(df)
    .mark_line()
    .encode(
        x=alt.X("date:T", title="Month"),
        y=alt.Y("rate:Q", title="Unemployment rate (%)", scale=alt.Scale(zero=True)),
        color=alt.Color("series:N", legend=alt.Legend(title="Industry")),
    )
    .properties(
        title=alt.Title(
            "Construction vs leisure and hospitality unemployment rates",
            subtitle="Monthly rate (%), Vega unemployment-across-industries sample",
        )
    )
)