"""Render paired PNGs from walk-through finals (not a CI harness)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("Agg")
mpl.rcParams.update(
    {
        "savefig.dpi": 150,
        "figure.dpi": 100,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
    }
)
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig-evident-eval")

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "evident-charts"
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "charts"
WALKTHROUGHS = HERE.parent / "walkthroughs"

sys.path.insert(0, str(SKILL / "scripts"))
import evident as ev

CHART_W = 640
CHART_H = 400
SCALE_FACTOR = 2
_PNG_METADATA = {
    "Software": None,
    "Creation Time": None,
}


def _normalize_png(path: Path) -> None:
    from PIL import Image

    with Image.open(path) as img:
        rgb = img.convert("RGB")
        rgb.save(path, format="PNG", compress_level=6, optimize=False)


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ev.save(fig, path, metadata=dict(_PNG_METADATA))
    _normalize_png(path)


def _save_altair(chart, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    chart.width = CHART_W
    chart.height = CHART_H
    chart.save(str(path), scale_factor=SCALE_FACTOR)
    _normalize_png(path)


def _load_final_py(case: str, skill: str) -> Path:
    return WALKTHROUGHS / case / skill / "final_chart.py"


def render_build_normalized_stack(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("normalized-stack", "build-my-chart")))
    _save_altair(ns["chart"], out)


def render_evident_normalized_stack(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("normalized-stack", "evident-charts")))
    _save(ns["fig"], out)
    plt.close(ns["fig"])


def render_build_many_categories(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("many-categories", "build-my-chart")))
    _save_altair(ns["chart"], out)


def render_evident_many_categories(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("many-categories", "evident-charts")))
    _save(ns["fig"], out)
    plt.close(ns["fig"])


def render_build_time_series(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("time-series", "build-my-chart")))
    _save_altair(ns["chart"], out)


def render_evident_time_series(out: Path) -> None:
    import runpy

    ns = runpy.run_path(str(_load_final_py("time-series", "evident-charts")))
    _save(ns["fig"], out)
    plt.close(ns["fig"])


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