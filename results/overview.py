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

    analyzed: dict = {}

    for cluster_sd, value in results.items():

        analyzed[cluster_sd] = {
            "gonzalez_r_mean": statistics.mean(value["gonzalez_r"]),
            "da_r_mean": statistics.mean(value["da_r"]),
            "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / statistics.mean(value["gonzalez_r"]),
            "da_c_r_mean": statistics.mean(value["da_c_r"]),
            "da_c_r_mean/gonzalez_r_mean": statistics.mean(value["da_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_r_mean": statistics.mean(value["rda_r"]),
            "rda_r_mean/gonzalez_r_mean": statistics.mean(value["rda_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_c_r_mean": statistics.mean(value["rda_c_r"]),
            "rda_c_r_mean/gonzalez_r_mean": statistics.mean(value["rda_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            "psa_c_r_mean/gonzalez_r_mean": statistics.mean(value["psa_c_r"]) / statistics.mean(value["gonzalez_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "cluster_sd_comparison.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)

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

    analyzed: dict = {}

    for dimensions, value in results.items():

        analyzed[dimensions] = {
            "gonzalez_r_mean": statistics.mean(value["gonzalez_r"]),
            "da_r_mean": statistics.mean(value["da_r"]),
            "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / statistics.mean(value["gonzalez_r"]),
            "da_c_r_mean": statistics.mean(value["da_c_r"]),
            "da_c_r_mean/gonzalez_r_mean": statistics.mean(value["da_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_r_mean": statistics.mean(value["rda_r"]),
            "rda_r_mean/gonzalez_r_mean": statistics.mean(value["rda_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_c_r_mean": statistics.mean(value["rda_c_r"]),
            "rda_c_r_mean/gonzalez_r_mean": statistics.mean(value["rda_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            "psa_c_r_mean/gonzalez_r_mean": statistics.mean(value["psa_c_r"]) / statistics.mean(value["gonzalez_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "dimension_comparison.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)

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

    analyzed: dict = {}

    for k, value in results.items():

        analyzed[k] = {
            "gonzalez_r_mean": statistics.mean(value["gonzalez_r"]),
            "da_r_mean": statistics.mean(value["da_r"]),
            "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / statistics.mean(value["gonzalez_r"]),
            "da_c_r_mean": statistics.mean(value["da_c_r"]),
            "da_c_r_mean/gonzalez_r_mean": statistics.mean(value["da_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_r_mean": statistics.mean(value["rda_r"]),
            "rda_r_mean/gonzalez_r_mean": statistics.mean(value["rda_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_c_r_mean": statistics.mean(value["rda_c_r"]),
            "rda_c_r_mean/gonzalez_r_mean": statistics.mean(value["rda_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            "psa_c_r_mean/gonzalez_r_mean": statistics.mean(value["psa_c_r"]) / statistics.mean(value["gonzalez_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "k_comparison.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)

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

    analyzed: dict = {}

    for m, value in results.items():

        analyzed[m] = {
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "m_comparison_cluster_sd_1.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)

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

    analyzed: dict = {}

    for m, value in results.items():

        analyzed[m] = {
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "m_comparison_cluster_sd_8.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)

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

    analyzed: dict = {}

    for k, value in results.items():

        analyzed[k] = {
            "gonzalez_r_mean": statistics.mean(value["gonzalez_r"]),
            "da_r_mean": statistics.mean(value["da_r"]),
            "da_r_mean/gonzalez_r_mean": statistics.mean(value["da_r"]) / statistics.mean(value["gonzalez_r"]),
            "da_c_r_mean": statistics.mean(value["da_c_r"]),
            "da_c_r_mean/gonzalez_r_mean": statistics.mean(value["da_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_r_mean": statistics.mean(value["rda_r"]),
            "rda_r_mean/gonzalez_r_mean": statistics.mean(value["rda_r"]) / statistics.mean(value["gonzalez_r"]),
            "rda_c_r_mean": statistics.mean(value["rda_c_r"]),
            "rda_c_r_mean/gonzalez_r_mean": statistics.mean(value["rda_c_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_r_mean": statistics.mean(value["psa_r"]),
            "psa_r_mean/gonzalez_r_mean": statistics.mean(value["psa_r"]) / statistics.mean(value["gonzalez_r"]),
            "psa_c_r_mean": statistics.mean(value["psa_c_r"]),
            "psa_c_r_mean/gonzalez_r_mean": statistics.mean(value["psa_c_r"]) / statistics.mean(value["gonzalez_r"]),
        }

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "overview",
        "metrics_comparison.json"
    )

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)