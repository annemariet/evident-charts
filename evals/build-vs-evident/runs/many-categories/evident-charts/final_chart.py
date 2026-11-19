"""evident-charts run: Construction highlight, C3-compliant legend."""
from __future__ import annotations

import json
from pathlib import Path

import evident as ev
import pandas as pd
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE.parents[2] / "data" / "unemployment-industries.json").read_text())

df = pd.DataFrame(raw)
snap = df[df["year"] == 2009].groupby("series", as_index=False)["rate"].mean()
snap = snap.sort_values("rate", ascending=True)
highlight = "Construction"
accent = "#D55E00"
gray = "#BDBDBD"
colors = [accent if s == highlight else gray for s in snap["series"]]
fig, ax = ev.figure(dest="blog")
ax.barh(snap["series"], snap["rate"], color=colors, edgecolor="white", linewidth=1)
ax.set_xlabel("Unemployment rate (%)")
ax.set_ylabel("")
ax.set_xlim(0, float(snap["rate"].max()) * 1.08)
spread = float(snap["rate"].max() - snap["rate"].min())
ax.legend(
    handles=[Patch(facecolor=accent, edgecolor="white", label=highlight), Patch(facecolor=gray, edgecolor="white", label="Other industries")],
    loc="lower right",
    frameon=False,
)
ev.titles(
    fig,
    "Construction led industry unemployment in 2009",
    f"14 industries, mean monthly rate (%), Vega sample (spread ≈ {spread:.1f} pp)",
)