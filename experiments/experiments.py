
from algorithms.offline.gonzalez import gonzalez
from algorithms.online.doubling_k_center import DoublingKCenter
from algorithms.online.randomized_doubling_k_center import RandomizedDoublingKCenter
from algorithms.online.scaling_k_center_parallelized import ParallelizedScalingKCenter
from benchmarks.metrics import chebyshev_distance, euclidean_distance, manhattan_distance
from benchmarks.synthetic.points import generate_uniform_points, worst_case_1d
from experiments.utils import simulate_online, write_json


# amortisierte worst case Güte des randomisierten Doubling-Algorithmus
def average_worst_case() -> None:

    d = euclidean_distance
    k = 10
    worst_case_points = worst_case_1d(k=k)

    rs: list[float] = []
    for _ in range(0, 1000):
        algo = RandomizedDoublingKCenter(k, d)
        solution = simulate_online(algo, worst_case_points, [len(worst_case_points)])[0]
        rs.append(solution.radius)

    avg = sum(rs) / len(rs)
    print(avg)

# k hat keinen einflus auf die lösungsgüte
def test_k_with_fixed_n() -> None:

    solutions: dict = {}

    ks = [2, 4, 8, 16, 32, 64]
    d = euclidean_distance

    for k in ks:
        doubling_rs = []
        p_scaling_rs = []
        gonzales_rs = []

        for i in range(0, 10):
            n = k * 10
            points = generate_uniform_points(n, 2, -100, 100, i)

            doubling = DoublingKCenter(k=k, d=d)
            doubling_rs.append(simulate_online(doubling, points, [n])[0].radius)

            p_scaling = ParallelizedScalingKCenter(k=k, d=d, m=16)
            p_scaling_rs.append(simulate_online(p_scaling, points, [n])[0].radius)

            gonzales_rs.append(gonzalez(k, d, points).radius)

        solutions[str(k)] = {
            "doubling_r": sum(doubling_rs) / len(doubling_rs),
            "p_scaling_r": sum(p_scaling_rs) / len(p_scaling_rs),
            "gonzales_r": sum(gonzales_rs) / len(gonzales_rs)
        }

    write_json("test_k_with_fixed_k.json", solutions)

# k hat auch bei gleichbleibendem n keinen einfluss auf die Lösungsgüte
def test_k() -> None:

    solutions: dict = {}

    ks = [2, 4, 8, 16, 32, 64]
    d = euclidean_distance

    for k in ks:
        doubling_rs = []
        p_scaling_rs = []
        gonzales_rs = []

        for i in range(0, 10):
            n = 200
            points = generate_uniform_points(n, 2, -100, 100, i)

            doubling = DoublingKCenter(k=k, d=d)
            doubling_rs.append(simulate_online(doubling, points, [n])[0].radius)

            p_scaling = ParallelizedScalingKCenter(k=k, d=d, m=16)
            p_scaling_rs.append(simulate_online(p_scaling, points, [n])[0].radius)

            gonzales_rs.append(gonzalez(k, d, points).radius)

        solutions[str(k)] = {
            "doubling_r": sum(doubling_rs) / len(doubling_rs),
            "p_scaling_r": sum(p_scaling_rs) / len(p_scaling_rs),
            "gonzales_r": sum(gonzales_rs) / len(gonzales_rs)
        }

    write_json("test_k.json", solutions)

# Die Metrik hat auch keinen Einflus auf die Lösungsgüte
def test_metrics() -> None:

    solutions: dict = {}

    metrics = {
        "euclidean": euclidean_distance,
        "manhattan": manhattan_distance,
        "chebyshev": chebyshev_distance
    }

    k = 10

    for metric_name, d in metrics.items():
        doubling_rs = []
        p_scaling_rs = []
        gonzales_rs = []

        for i in range(0, 100):
            n = k * 100
            points = generate_uniform_points(n, 2, -100, 100)

            doubling = DoublingKCenter(k=k, d=d)
            doubling_rs.append(simulate_online(doubling, points, [n])[0].radius)

            p_scaling = ParallelizedScalingKCenter(k=k, d=d, m=16)
            p_scaling_rs.append(simulate_online(p_scaling, points, [n])[0].radius)

            gonzales_rs.append(gonzalez(k, d, points).radius)

        solutions[metric_name] = {
            "doubling_r": sum(doubling_rs) / len(doubling_rs),
            "p_scaling_r": sum(p_scaling_rs) / len(p_scaling_rs),
            "gonzales_r": sum(gonzales_rs) / len(gonzales_rs)
        }

    write_json("test_metrics.json", solutions)