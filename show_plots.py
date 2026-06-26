
import math
import os

from matplotlib import pyplot as plt
import numpy as np

from benchmarks.synthetic.points import generate_clustered_points
from results.plots.plot import boxplot_rs
from results.plots.table import analyze_results

algorithms = {
    "PSA-16 r": "psa_r",
    "PSA-16 r'": "psa_c_r",
    "DA r": "da_r",
    "DA r'": "da_c_r",
    "Gonzalez r": "gonzalez_r",
}

#boxplot_rs("k", "k", False, title="", value_name="", algorithms=algorithms)
#create_summary_table()


def plot_example_cluster_sd():

    datasets = [
        (sd, generate_clustered_points(
            k=10,
            n=500,
            cluster_std=sd,
            dim=2,
            center_std=10,
            seed=0
        )) for sd in [0.25, 0.5, 1, 2, 4, 8]
    ]

    fig, axes = plt.subplots(2, 3, figsize=(20, 10))

    axes = axes.flatten()

    for ax, (std, points) in zip(axes, datasets):

        points = np.array(points)

        ax.scatter(points[:, 0], points[:, 1], s=5)

        ax.set_title(f"Cluster SD = {std}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.grid(True, linestyle="--", alpha=0.5)

        # Damit alle Subplots die gleiche Größe haben
        ax.set_xlim(-40, 40)
        ax.set_ylim(-40, 40)

        ax.set_aspect("equal")

    plt.tight_layout()
    plt.show()

def plot_example_cluster_k():

    datasets = [
        (k, generate_clustered_points(
            k=k,
            n=512,
            cluster_std=2,
            dim=2,
            center_std=5 * math.sqrt(k),
            seed=0
        )) for k in [2, 4, 8, 16, 32, 64, 128, 256]
    ]

    fig, axes = plt.subplots(2, 3, figsize=(20, 10))

    axes = axes.flatten()

    for ax, (k, points) in zip(axes, datasets):

        points = np.array(points)

        ax.scatter(points[:, 0], points[:, 1], s=5)

        ax.set_title(f"k = {k}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.grid(True, linestyle="--", alpha=0.5)

        # Damit alle Subplots die gleiche Größe haben
        ax.set_xlim(-120, 120)
        ax.set_ylim(-120, 120)

        ax.set_aspect("equal")

    plt.tight_layout()
    plt.show()


input_path = os.path.join(
    os.path.dirname(__file__),
    "results",
    "data",
    "dim.json"
)

output_path = os.path.join(
    os.path.dirname(__file__),
    "results",
    "data",
    "dim_stats.json"
)

analyze_results(input_path, output_path)

#plot_example_cluster_k()