"""build-my-chart walk-through final: normalized stack."""
from pathlib import Path

import altair as alt
import pandas as pd

LEVEL_ORDER = ["low", "mid", "high"]
HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE.parents[2] / "data" / "stack_synthetic.csv")

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("value:Q", stack="normalize", axis=alt.Axis(format="%", title="Share of value")),
        y=alt.Y("category:N", title=None),
        color=alt.Color(
            "level:O",
            sort=LEVEL_ORDER,
            scale=alt.Scale(domain=LEVEL_ORDER, scheme="blues"),
            legend=alt.Legend(title="Level"),
        ),
    )
    .properties(title=alt.Title("Share of value by level within category", subtitle="Synthetic demo table"))
)