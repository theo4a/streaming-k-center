import math
import time

from algorithms.offline.gonzalez import gonzalez
from algorithms.online.doubling_k_center import DoublingKCenter
from algorithms.online.scaling_k_center_parallelized import ParallelizedScalingKCenter
from benchmarks.metrics import chebyshev_distance, euclidean_distance, manhattan_distance
from benchmarks.synthetic.points import generate_clustered_points
from experiments.utils import check_radius, simulate_streaming, write_json


def test_cluster_std() -> None:

    n = 500
    k = 10
    sample_size = 100
    cluster_sds = [0.25, 0.5, 1, 2, 4, 8]
    d = euclidean_distance
    psa_m = 16

    results: dict[str, dict[str, list[float]]] = {}

    for cluster_sd in cluster_sds:

        results[str(cluster_sd)] = {
            "gonzalez_sec": [],
            "gonzalez_r": [],
            "da_sec": [],
            "da_r": [],
            "da_c_r": [],
            "psa_sec": [],
            "psa_r": [],
            "psa_c_r": [],
        }

        for i in range(sample_size):
            print(i)

            points = generate_clustered_points(
                k=k,
                n=n,
                cluster_std=cluster_sd,
                dim=2,
                center_std=10,
                seed=i
            )

            # Gonzalez
            gonzalez_start = time.perf_counter()
            gonzalez_solution = gonzalez(k, d, points)
            gonzalez_end = time.perf_counter()
            results[str(cluster_sd)]["gonzalez_sec"].append(gonzalez_end - gonzalez_start)
            results[str(cluster_sd)]["gonzalez_r"].append(gonzalez_solution.radius)

            # DA
            da = DoublingKCenter(k=k, d=d)
            da_start = time.perf_counter()
            da_solution = simulate_streaming(da, points)
            da_end = time.perf_counter()
            da_c_r = check_radius(d, points, da_solution.centers)
            results[str(cluster_sd)]["da_sec"].append(da_end - da_start)
            results[str(cluster_sd)]["da_r"].append(da_solution.radius)
            results[str(cluster_sd)]["da_c_r"].append(da_c_r)

            # PSA
            psa = ParallelizedScalingKCenter(k=k, d=d, m=psa_m)
            psa_start = time.perf_counter()
            psa_solution = simulate_streaming(psa, points)
            psa_end = time.perf_counter()
            psa_c_r = check_radius(d, points, psa_solution.centers)
            results[str(cluster_sd)]["psa_sec"].append(psa_end - psa_start)
            results[str(cluster_sd)]["psa_r"].append(psa_solution.radius)
            results[str(cluster_sd)]["psa_c_r"].append(psa_c_r)

    # Save results
    write_json("temp", results)

def test_k() -> None:

    n = 512
    sample_size = 100
    ks = [2, 4, 8, 16, 32, 64, 128]
    d = euclidean_distance
    psa_m = 16

    results: dict[str, dict[str, list[float]]] = {}

    for k in ks:

        results[str(k)] = {
            "gonzalez_sec": [],
            "gonzalez_r": [],
            "da_sec": [],
            "da_r": [],
            "da_c_r": [],
            "psa_sec": [],
            "psa_r": [],
            "psa_c_r": [],
        }

        for i in range(sample_size):
            print(i)

            points = generate_clustered_points(
                k=k,
                n=n,
                cluster_std=1,
                dim=2,
                center_std=2 * math.sqrt(k),
                seed=i
            )

            # Gonzalez
            gonzalez_start = time.perf_counter()
            gonzalez_solution = gonzalez(k, d, points)
            gonzalez_end = time.perf_counter()
            results[str(k)]["gonzalez_sec"].append(gonzalez_end - gonzalez_start)
            results[str(k)]["gonzalez_r"].append(gonzalez_solution.radius)

            # DA
            da = DoublingKCenter(k=k, d=d)
            da_start = time.perf_counter()
            da_solution = simulate_streaming(da, points)
            da_end = time.perf_counter()
            da_c_r = check_radius(d, points, da_solution.centers)
            results[str(k)]["da_sec"].append(da_end - da_start)
            results[str(k)]["da_r"].append(da_solution.radius)
            results[str(k)]["da_c_r"].append(da_c_r)

            # PSA
            psa = ParallelizedScalingKCenter(k=k, d=d, m=psa_m)
            psa_start = time.perf_counter()
            psa_solution = simulate_streaming(psa, points)
            psa_end = time.perf_counter()
            psa_c_r = check_radius(d, points, psa_solution.centers)
            results[str(k)]["psa_sec"].append(psa_end - psa_start)
            results[str(k)]["psa_r"].append(psa_solution.radius)
            results[str(k)]["psa_c_r"].append(psa_c_r)

    # Save results
    write_json("k", results)

def test_metrics() -> None:

    metrics = {
        "euclidean": euclidean_distance,
        "manhattan": manhattan_distance,
        "chebyshev": chebyshev_distance
    }
    k = 10
    n = 500
    psa_m = 16

    results: dict[str, dict[str, list[float]]] = {}

    for metric_name, d in metrics.items():
        
        results[metric_name] = {
            "gonzalez_sec": [],
            "gonzalez_r": [],
            "da_sec": [],
            "da_r": [],
            "da_c_r": [],
            "psa_sec": [],
            "psa_r": [],
            "psa_c_r": [],
        }

        for i in range(0, 100):
            print(i)
            points = generate_clustered_points(
                k=k,
                n=n,
                cluster_std=1,
                dim=2,
                center_std=10,
                seed=i
            )

            # Gonzalez
            gonzalez_start = time.perf_counter()
            gonzalez_solution = gonzalez(k, d, points)
            gonzalez_end = time.perf_counter()
            results[str(metric_name)]["gonzalez_sec"].append(gonzalez_end - gonzalez_start)
            results[str(metric_name)]["gonzalez_r"].append(gonzalez_solution.radius)

            # DA
            da = DoublingKCenter(k=k, d=d)
            da_start = time.perf_counter()
            da_solution = simulate_streaming(da, points)
            da_end = time.perf_counter()
            da_c_r = check_radius(d, points, da_solution.centers)
            results[str(metric_name)]["da_sec"].append(da_end - da_start)
            results[str(metric_name)]["da_r"].append(da_solution.radius)
            results[str(metric_name)]["da_c_r"].append(da_c_r)

            # PSA
            psa = ParallelizedScalingKCenter(k=k, d=d, m=psa_m)
            psa_start = time.perf_counter()
            psa_solution = simulate_streaming(psa, points)
            psa_end = time.perf_counter()
            psa_c_r = check_radius(d, points, psa_solution.centers)
            results[str(metric_name)]["psa_sec"].append(psa_end - psa_start)
            results[str(metric_name)]["psa_r"].append(psa_solution.radius)
            results[str(metric_name)]["psa_c_r"].append(psa_c_r)

    # Save results
    write_json("metrics", results)

def test_dimension() -> None:

    n = 100
    k = 5
    sample_size = 100
    dims = [2, 4, 8, 16, 32, 64, 128, 256]
    d = euclidean_distance
    psa_m = 16

    results: dict[str, dict[str, list[float]]] = {}

    for dim in dims:
        results[str(dim)] = {
            "gonzalez_sec": [],
            "gonzalez_r": [],
            "da_sec": [],
            "da_r": [],
            "da_c_r": [],
            "psa_sec": [],
            "psa_r": [],
            "psa_c_r": [],
        }

        for i in range(sample_size):
            print(i)

            points = generate_clustered_points(
                k=k,
                n=n,
                cluster_std=1,
                dim=dim,
                center_std=10,
                seed=i
            )

            # Gonzalez
            gonzalez_start = time.perf_counter()
            gonzalez_solution = gonzalez(k, d, points)
            gonzalez_end = time.perf_counter()
            results[str(dim)]["gonzalez_sec"].append(gonzalez_end - gonzalez_start)
            results[str(dim)]["gonzalez_r"].append(gonzalez_solution.radius)

            # DA
            da = DoublingKCenter(k=k, d=d)
            da_start = time.perf_counter()
            da_solution = simulate_streaming(da, points)
            da_end = time.perf_counter()
            da_c_r = check_radius(d, points, da_solution.centers)
            results[str(dim)]["da_sec"].append(da_end - da_start)
            results[str(dim)]["da_r"].append(da_solution.radius)
            results[str(dim)]["da_c_r"].append(da_c_r)

            # PSA
            psa = ParallelizedScalingKCenter(k=k, d=d, m=psa_m)
            psa_start = time.perf_counter()
            psa_solution = simulate_streaming(psa, points)
            psa_end = time.perf_counter()
            psa_c_r = check_radius(d, points, psa_solution.centers)
            results[str(dim)]["psa_sec"].append(psa_end - psa_start)
            results[str(dim)]["psa_r"].append(psa_solution.radius)
            results[str(dim)]["psa_c_r"].append(psa_c_r)


    # Save results
    write_json("dim", results)

def test_m() -> None:

    n = 500
    k = 5
    sample_size = 100
    psa_ms = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    d = euclidean_distance

    results: dict[str, dict[str, list[float]]] = {}

    for m in psa_ms:
        results[str(m)] = {
            "psa_sec": [],
            "psa_r": [],
            "psa_c_r": []
        }

        for i in range(sample_size):
            print(i)

            points = generate_clustered_points(
                k=k,
                n=n,
                cluster_std=8,
                dim=2,
                center_std=10,
                seed=i
            )

            # PSA
            psa = ParallelizedScalingKCenter(k=k, d=d, m=m)
            psa_start = time.perf_counter()
            psa_solution = simulate_streaming(psa, points)
            psa_end = time.perf_counter()
            psa_c_r = check_radius(d, points, psa_solution.centers)
            results[str(m)]["psa_sec"].append(psa_end - psa_start)
            results[str(m)]["psa_r"].append(psa_solution.radius)
            results[str(m)]["psa_c_r"].append(psa_c_r)

    # Save results
    write_json("m_8", results)

