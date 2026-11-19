"""evident-charts walk-through final: rate time series."""
from __future__ import annotations

import json
from pathlib import Path

import evident as ev
import pandas as pd

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE.parents[2] / "data" / "unemployment-industries.json").read_text())
df = pd.DataFrame(raw)
df["date"] = pd.to_datetime(df["date"])
keep = ["Construction", "Leisure and hospitality"]
df = df[df["series"].isin(keep)].sort_values("date")
fig, ax = ev.figure(dest="blog")
for series, sub in df.groupby("series", sort=False):
    if series == "Construction":
        ax.plot(sub["date"], sub["rate"], color="#D55E00", linewidth=2.5, label=series)
    else:
        ax.plot(sub["date"], sub["rate"], color="#BDBDBD", linewidth=1.5, label=series)
ax.set_ylabel("Unemployment rate (%)")
ax.set_xlabel("Month")
ax.set_ylim(0, None)
ax.legend(loc="upper right", frameon=False)
ev.titles(
    fig,
    "Construction unemployment rate peaked above leisure and hospitality in 2009",
    "Monthly rate (%), two industries shown, Vega sample through Feb 2010",
)