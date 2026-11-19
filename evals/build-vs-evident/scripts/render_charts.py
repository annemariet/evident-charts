"""Render paired PNGs for build-my-chart vs evident-charts eval (not a CI harness)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# Deterministic raster output (Patty #4).
mpl.use("Agg")
mpl.rcParams.update({"savefig.dpi": 150, "figure.dpi": 100})
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig-evident-eval")

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "evident-charts"
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "charts"
RUNS = HERE.parent / "runs"

sys.path.insert(0, str(SKILL / "scripts"))
import evident as ev

CHART_W = 640
CHART_H = 400
SCALE_FACTOR = 2


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ev.save(fig, path)


def _load_final_py(case: str, skill: str) -> Path:
    return RUNS / case / skill / "final_chart.py"


def render_build_normalized_stack(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("normalized-stack", "build-my-chart")))
    chart = ns["chart"]
    chart.width = CHART_W
    chart.height = CHART_H
    chart.save(str(out), scale_factor=SCALE_FACTOR)


def render_evident_normalized_stack(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("normalized-stack", "evident-charts")))
    fig = ns["fig"]
    _save(fig, out)
    plt.close(fig)


def render_build_many_categories(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("many-categories", "build-my-chart")))
    chart = ns["chart"]
    chart.width = CHART_W
    chart.height = CHART_H
    chart.save(str(out), scale_factor=SCALE_FACTOR)


def render_evident_many_categories(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("many-categories", "evident-charts")))
    fig = ns["fig"]
    _save(fig, out)
    plt.close(fig)


def render_build_time_series(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("time-series", "build-my-chart")))
    chart = ns["chart"]
    chart.width = CHART_W
    chart.height = CHART_H
    chart.save(str(out), scale_factor=SCALE_FACTOR)


def render_evident_time_series(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("time-series", "evident-charts")))
    fig = ns["fig"]
    _save(fig, out)
    plt.close(fig)


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