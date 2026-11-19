"""build-my-chart walk-through: 14 nominal hues per scripted encodings."""
from __future__ import annotations

import json
from pathlib import Path

import altair as alt
import pandas as pd

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE.parents[2] / "data" / "unemployment-industries.json").read_text())
df = pd.DataFrame(raw)
snap = df[df["year"] == 2009].groupby("series", as_index=False)["rate"].mean()
snap = snap.sort_values("rate", ascending=True)

chart = (
    alt.Chart(snap)
    .mark_bar()
    .encode(
        x=alt.X("rate:Q", title="Unemployment rate (%)", scale=alt.Scale(zero=True)),
        y=alt.Y("series:N", sort="-x", title=None),
        color=alt.Color("series:N", legend=alt.Legend(title="Industry")),
    )
    .properties(
        title=alt.Title(
            "Average unemployment rate by industry in 2009",
            subtitle="Vega sample: unemployment across industries",
        )
    )
)