"""Render paired PNGs for build-my-chart vs evident-charts eval (not a CI harness)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "evident-charts"
EVIDENT = SKILL / "scripts" / "evident.py"
HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "charts"

sys.path.insert(0, str(SKILL / "scripts"))
import evident as ev

LEVEL_ORDER = ["low", "mid", "high"]
def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ev.save(fig, path)


def render_build_normalized_stack(out: Path) -> None:
    import altair as alt

    df = pd.read_csv(DATA / "stack_synthetic.csv")
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
    chart.save(str(out), scale_factor=2)


def render_evident_normalized_stack(out: Path) -> None:
    raw = pd.read_csv(DATA / "stack_synthetic.csv")
    df = raw.groupby(["category", "level"], as_index=False)["value"].sum()
    totals = df.groupby("category")["value"].transform("sum")
    df = df.assign(share=df["value"] / totals)
    categories = df["category"].unique().tolist()
    fig, ax = ev.figure(dest="blog")
    bottom = np.zeros(len(categories))
    colors = {"low": "#BDBDBD", "mid": "#56B4E9", "high": "#0072B2"}
    for level in LEVEL_ORDER:
        subset = df[df["level"] == level].set_index("category").reindex(categories)
        vals = subset["share"].fillna(0).to_numpy()
        ax.barh(categories, vals, left=bottom, label=level, color=colors[level], edgecolor="white")
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
    _save(fig, out)


def _unemployment_2009_bars() -> pd.DataFrame:
    raw = json.loads((DATA / "unemployment-industries.json").read_text())
    df = pd.DataFrame(raw)
    df["date"] = pd.to_datetime(df["date"])
    snap = df[df["year"] == 2009].groupby("series", as_index=False)["rate"].mean()
    return snap.sort_values("rate", ascending=True)


def render_build_many_categories(out: Path) -> None:
    import altair as alt

    df = _unemployment_2009_bars()
    chart = (
        alt.Chart(df)
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
    chart.save(str(out), scale_factor=2)


def render_evident_many_categories(out: Path) -> None:
    df = _unemployment_2009_bars()
    fig, ax = ev.figure(dest="blog")
    highlight = "Construction"
    colors = ["#D55E00" if s == highlight else "#BDBDBD" for s in df["series"]]
    ax.barh(df["series"], df["rate"], color=colors, edgecolor="white")
    ax.set_xlabel("Unemployment rate (%)")
    ax.set_ylabel("")
    ax.set_xlim(0, df["rate"].max() * 1.08)
    ax.barh([], [], color="#D55E00", label=highlight)
    ax.barh([], [], color="#BDBDBD", label="Other industries")
    ax.legend(loc="lower right", frameon=False)
    spread = df["rate"].max() - df["rate"].min()
    ev.titles(
        fig,
        "Construction led industry unemployment in 2009",
        f"14 industries, mean monthly rate, Vega sample (spread ≈ {spread:.1f} pp)",
    )
    _save(fig, out)


def _unemployment_series() -> pd.DataFrame:
    raw = json.loads((DATA / "unemployment-industries.json").read_text())
    df = pd.DataFrame(raw)
    df["date"] = pd.to_datetime(df["date"])
    keep = ["Construction", "Accommodation"]
    return df[df["series"].isin(keep)].copy()


def render_build_time_series(out: Path) -> None:
    import altair as alt

    df = _unemployment_series()
    chart = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X("date:T", title="Month"),
            y=alt.Y("count:Q", title="Unemployment share", scale=alt.Scale(zero=True)),
            color=alt.Color("series:N", legend=alt.Legend(title="Industry")),
        )
        .properties(
            title=alt.Title(
                "Construction unemployment share through the recession",
                subtitle="Vega sample: unemployment across industries",
            )
        )
    )
    chart.save(str(out), scale_factor=2)


def render_evident_time_series(out: Path) -> None:
    df = _unemployment_series()
    fig, ax = ev.figure(dest="blog")
    for series, sub in df.groupby("series"):
        color = "#D55E00" if series == "Construction" else "#BDBDBD"
        lw = 2.5 if series == "Construction" else 1.2
        ax.plot(sub["date"], sub["count"], label=series, color=color, linewidth=lw)
    ax.set_ylabel("Unemployment share")
    ax.set_xlabel("Month")
    ax.set_ylim(0, None)
    ax.legend(loc="upper right", frameon=False)
    ev.titles(
        fig,
        "Construction unemployment peaked above lodging through 2008–2010",
        "Monthly share, Vega unemployment-across-industries sample",
    )
    _save(fig, out)


def main() -> None:
    try:
        import altair  # noqa: F401
    except ImportError as exc:
        raise SystemExit("Install altair and vl-convert-python for build-my-chart PNGs") from exc

    render_build_normalized_stack(OUT / "normalized-stack-build-my-chart.png")
    render_evident_normalized_stack(OUT / "normalized-stack-evident-charts.png")
    render_build_many_categories(OUT / "many-categories-build-my-chart.png")
    render_evident_many_categories(OUT / "many-categories-evident-charts.png")
    render_build_time_series(OUT / "time-series-build-my-chart.png")
    render_evident_time_series(OUT / "time-series-evident-charts.png")
    print("Wrote PNGs to", OUT)


if __name__ == "__main__":
    main()