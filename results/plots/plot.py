import json
import os
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
from benchmarks.metrics import Point
from model.types import Snapshot, Solution



def plot_parameter() -> None:
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "results",
        "parameter",
        "result.json"
    )
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    points = data["points"]
    p_scaling = Solution(**data["solutions"]["p_scaling"])
    doubling = Solution(**data["solutions"]["doubling"])

    plot_combined([
        (p_scaling, points, "p_scaling"),
        (doubling,  points, "doubling"),
    ])


def plot_combined(plots: list[tuple[Solution, list[Point], str]]) -> None:
    fig, axes = plt.subplots(1, len(plots), figsize=(6 * len(plots), 6))
    if len(plots) == 1:
        axes = [axes]

    for ax, (solution, points, label) in zip(axes, plots):
        plot_solution(solution, points, label, ax)

    plt.tight_layout()
    plt.show()


def plot_solution(solution: Solution, points: list[Point], label: str, ax: plt.Axes | None = None) -> plt.Figure:
    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(6, 6))
    else:
        fig = ax.get_figure()

    px, py = zip(*points)
    ax.scatter(px, py, s=15, color="steelblue", alpha=0.4)

    color = "tomato"
    for cx, cy in solution.centers:
        ax.scatter(cx, cy, s=80, color=color, marker="*", zorder=5)
        circle = plt.Circle(
            (cx, cy),
            solution.radius,
            color=color,
            fill=False,
            linestyle="--",
            alpha=0.6,
        )
        ax.add_patch(circle)

    ax.scatter([], [], color=color, marker="*",
               label=f"{label} r={solution.radius:.2f} rr={solution.real_radius:.2f}")
    ax.set_title(label)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend()

    if standalone:
        plt.tight_layout()
        plt.show()

    return fig