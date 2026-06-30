import csv
import json
import os
import statistics


def overview_cluster_sd_comparison() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "cluster_sd_comparison.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "cluster_sd_comparison.csv"
    )

    fieldnames = [
        "cluster_sd",
        "gonzalez_r_mean",
        "da_r_mean/gonzalez_r_mean",
        "psa_r_mean/gonzalez_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for cluster_sd, value in results.items():
            gonzalez_r_mean = statistics.mean(value["gonzalez_r"])
            writer.writerow({
                "cluster_sd": cluster_sd,
                "gonzalez_r_mean": gonzalez_r_mean,
                "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / gonzalez_r_mean,
                "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / gonzalez_r_mean,
            })

def overview_dimension_comparison() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "dimension_comparison.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "dimension_comparison.csv"
    )

    fieldnames = [
        "dimensions",
        "gonzalez_r_mean",
        "da_r_mean/gonzalez_r_mean",
        "psa_r_mean/gonzalez_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for dimensions, value in results.items():
            gonzalez_r_mean = statistics.mean(value["gonzalez_r"])
            writer.writerow({
                "dimensions": dimensions,
                "gonzalez_r_mean": gonzalez_r_mean,
                "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / gonzalez_r_mean,
                "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / gonzalez_r_mean,
            })

def overview_k_comparison() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "k_comparison.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "k_comparison.csv"
    )

    fieldnames = [
        "k",
        "gonzalez_r_mean",
        "da_r_mean/gonzalez_r_mean",
        "psa_r_mean/gonzalez_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for k, value in results.items():
            gonzalez_r_mean = statistics.mean(value["gonzalez_r"])
            writer.writerow({
                "k": k,
                "gonzalez_r_mean": gonzalez_r_mean,
                "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / gonzalez_r_mean,
                "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / gonzalez_r_mean,
            })

def overview_m_comparison_cluster_sd_1() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "m_comparison_cluster_sd_1.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "m_comparison_cluster_sd_1.csv"
    )

    fieldnames = [
        "m",
        "psa_r_mean",
        "psa_c_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for m, value in results.items():
            writer.writerow({
                "m": m,
                "psa_r_mean": statistics.mean(value["psa_r"]),
                "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            })

def overview_m_comparison_cluster_sd_8() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "m_comparison_cluster_sd_8.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "m_comparison_cluster_sd_8.csv"
    )

    fieldnames = [
        "m",
        "psa_r_mean",
        "psa_c_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for m, value in results.items():
            writer.writerow({
                "m": m,
                "psa_r_mean": statistics.mean(value["psa_r"]),
                "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            })

def overview_metrics_comparison() -> None:

    input_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        "metrics_comparison.json"
    )

    with open(input_path, "r") as f:
        results = json.load(f)

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "metrics_comparison.csv"
    )

    fieldnames = [
        "metric",
        "gonzalez_r_mean",
        "da_r_mean/gonzalez_r_mean",
        "psa_r_mean/gonzalez_r_mean",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for metric, value in results.items():
            gonzalez_r_mean = statistics.mean(value["gonzalez_r"])
            writer.writerow({
                "metric": metric,
                "gonzalez_r_mean": gonzalez_r_mean,
                "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / gonzalez_r_mean,
                "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / gonzalez_r_mean,
            })
