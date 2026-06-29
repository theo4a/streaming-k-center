
import json
import os

from matplotlib import pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import pandas as pd


def boxplot(file_name: str,
            parameter_name: str,
            title: str,
            value_name: str,
            algorithms: dict,
            colors: dict = None
    ):

    # JSON laden
    with open(os.path.join(os.path.dirname(__file__), "..", "data", f"{file_name}.json"), "r") as f:
        data = json.load(f)

    # Cluster sortieren
    try:
        cluster_order = sorted(data.keys(), key=lambda x: float(x))
    except:
        cluster_order = sorted(data.keys(), key=lambda x: str(x))

    # Default-Farben, falls nicht übergeben
    if colors is None:
        default_colors = plt.get_cmap("tab10")
        colors = {
            name: default_colors(i % 10)
            for i, name in enumerate(algorithms.keys())
        }

    plt.figure(figsize=(16, 8))

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.size": 12
    })

    n = len(algorithms)
    base_positions = np.arange(len(cluster_order))

    # Breite & Abstand dynamisch je nach Anzahl Algorithmen
    total_width = 0.8  # Gesamtbreite pro Cluster-Gruppe (bleibt konstant)
    box_width = total_width / n
    # Offsets symmetrisch um 0 zentriert
    offsets = np.linspace(-(total_width - box_width) / 2, (total_width - box_width) / 2, n)

    positions_map = {
        name: base_positions + offsets[i]
        for i, name in enumerate(algorithms.keys())
    }

    # Plotten
    for i, (label, key) in enumerate(algorithms.items()):

        box_data = []
        positions = positions_map[label]
        color = colors[label]

        for cluster in cluster_order:
            values = data[cluster].get(key, [])
            box_data.append(values)

        plt.boxplot(
            box_data,
            positions=positions,
            widths=box_width * 0.9,  # kleiner Abstand zwischen Boxen
            patch_artist=True,
            showfliers=False,
            boxprops=dict(facecolor=color, color=color),
            whiskerprops=dict(color=color),
            capprops=dict(color=color),
            medianprops=dict(color="black")
        )

    # X-Achse
    plt.xticks(base_positions, cluster_order)
    plt.xlabel(parameter_name)
    plt.ylabel(value_name)
    plt.title(title)

    # Legend
    legend_handles = [
        Patch(facecolor=colors[name], label=name)
        for name in algorithms.keys()
    ]

    plt.legend(handles=legend_handles)
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


def plot_cluster_sd_comparison() -> None:
    algorithms = {
        "Gonzalez r": "gonzalez_r",

        "DA r": "da_r",
        "DA r'": "da_c_r",

        "PSA-16 r": "psa_r",
        "PSA-16 r'": "psa_c_r",
    }

    boxplot(
        file_name="cluster_sd_comparison",
        parameter_name="Cluster SD",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_dimension_comparison() -> None:
    algorithms = {
        "Gonzalez r": "gonzalez_r",

        "DA r": "da_r",
        "DA r'": "da_c_r",

        "PSA-16 r": "psa_r",
        "PSA-16 r'": "psa_c_r",
    }

    boxplot(
        file_name="dimension_comparison",
        parameter_name="Dimensions",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_dimension_rda_comparison() -> None:
    algorithms = {
        "DA r": "da_r",
        "DA r'": "da_c_r",

        "RDA r": "rda_r",
        "RDA r'": "rda_c_r",
    }

    boxplot(
        file_name="dimension_comparison",
        parameter_name="Dimensions",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_k_comparison() -> None:
    algorithms = {
        "Gonzalez r": "gonzalez_r",

        "DA r": "da_r",
        "DA r'": "da_c_r",

        "PSA-16 r": "psa_r",
        "PSA-16 r'": "psa_c_r",
    }

    boxplot(
        file_name="k_comparison",
        parameter_name="k",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_m_comparison_cluster_sd_1() -> None:
    algorithms = {
        "PSA r": "psa_r",
        "PSA r'": "psa_c_r",
    }

    boxplot(
        file_name="m_comparison_cluster_sd_1",
        parameter_name="m",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_m_comparison_cluster_sd_8() -> None:
    algorithms = {
        "PSA r": "psa_r",
        "PSA r'": "psa_c_r",
    }

    boxplot(
        file_name="m_comparison_cluster_sd_8",
        parameter_name="m",
        title="",
        value_name="",
        algorithms=algorithms
    )

def plot_metrics_comparison() -> None:
    algorithms = {
        "Gonzalez r": "gonzalez_r",

        "DA r": "da_r",
        "DA r'": "da_c_r",

        "PSA-16 r": "psa_r",
        "PSA-16 r'": "psa_c_r",
    }

    boxplot(
        file_name="metrics_comparison",
        parameter_name="Metric",
        title="",
        value_name="",
        algorithms=algorithms
    )