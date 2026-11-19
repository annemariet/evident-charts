"""evident-charts walk-through final: normalized stack."""
from pathlib import Path

import evident as ev
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LEVEL_ORDER = ["low", "mid", "high"]
HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE.parents[2] / "data" / "stack_synthetic.csv")
df = raw.groupby(["category", "level"], as_index=False)["value"].sum()
totals = df.groupby("category")["value"].transform("sum")
df = df.assign(share=df["value"] / totals)
categories = sorted(df["category"].unique())
fig, ax = ev.figure(dest="blog")
bottom = np.zeros(len(categories))
colors = {"low": "#BDBDBD", "mid": "#56B4E9", "high": "#0072B2"}
for level in LEVEL_ORDER:
    subset = df[df["level"] == level].set_index("category").reindex(categories)
    vals = subset["share"].fillna(0).to_numpy()
    ax.barh(categories, vals, left=bottom, label=level, color=colors[level], edgecolor="white", linewidth=1)
    bottom += vals
ax.set_xlim(0, 1)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))
ax.set_xlabel("Share of value")
ax.set_ylabel("")
ax.legend(title="Level", loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3)
ev.titles(
    fig,
    "Mid and high levels carry most value in both regions",
    "Shares within each category, synthetic demo table",
)
fig.subplots_adjust(bottom=0.22)