import math
import random

from typing import List
from model.types import Point


def cluster_with_fixed_radius(k: int, n: int, r: float, dim: int, seed: int) -> list[object]:
    rng = random.Random(seed)

    # Zentren erzeugen
    centers = []
    while len(centers) < k:
        candidate = tuple(rng.uniform(0, 100) for _ in range(dim))
        if all(math.dist(candidate, c) >= 2 * r for c in centers):
            centers.append(candidate)

    # Punktanzahl pro Cluster
    counts = [n // k] * k
    for i in range(n % k):
        counts[i] += 1

    # Position des Randpunkts pro Cluster
    boundary_positions = [rng.randrange(counts[i]) for i in range(k)]

    # Punkte pro Cluster erzeugen
    cluster_points: list[list[tuple]] = [[] for _ in range(k)]

    for idx in range(k):
        for pos in range(counts[idx]):
            angle_angles = [rng.uniform(0, 2 * math.pi) for _ in range(dim - 1)]

            if pos == boundary_positions[idx]:
                dist = r
            else:
                dist = min(abs(rng.gauss(0, r / 2)), r - 1e-12)

            direction = angles_to_unit_vector(angle_angles)
            point = tuple(centers[idx][d] + dist * direction[d] for d in range(dim))
            cluster_points[idx].append(point)

    # Alle Punkte zusammenführen und permutieren
    points = [p for cluster in cluster_points for p in cluster]
    rng.shuffle(points)

    return points


def angles_to_unit_vector(angles: list[float]) -> tuple:
    """
    Konvertiert dim-1 Winkel in einen dim-dimensionalen Einheitsvektor
    via sphärische Koordinaten.
    """
    dim = len(angles) + 1
    coords = []
    for i in range(dim):
        v = math.cos(angles[i]) if i < len(angles) else 1.0
        for j in range(i):
            v *= math.sin(angles[j])
        coords.append(v)
    return tuple(coords)


# Uniforme Punktmenge
def generate_uniform_points(
    n: int,
    dim: int,
    lower: float = 0.0,
    upper: float = 100.0,
    seed: int | None = None,
) -> List[Point]:
    """
    Gleichverteilte Punkte im n-dimensionalen Raum.
    """
    rng = random.Random(seed)
    points: list[Point] = [
        [rng.uniform(lower, upper) for _ in range(dim)]
        for _ in range(n)
    ]

    return points


# 2. Gaussian Cluster
def generate_gaussian_clusters(
    num_points: int,
    dim: int,
    num_clusters: int = 3,
    spread: float = 5.0,
    center_range: float = 100.0,
) -> List[Point]:
    """
    Erzeugt mehrere Gaussian-Cluster.
    """

    centers = [
        [random.uniform(0, center_range) for _ in range(dim)]
        for _ in range(num_clusters)
    ]

    points = []

    for _ in range(num_points):
        center = random.choice(centers)

        point = [
            random.gauss(center[d], spread)
            for d in range(dim)
        ]

        points.append(point)

    return points


# 3. Punktmenge mit Outliers
def generate_outlier_dataset(
    num_points: int,
    dim: int,
    outlier_ratio: float = 0.05,
    cluster_spread: float = 5.0,
    outlier_distance: float = 1000.0,
) -> List[Point]:
    """
    Normale Cluster + entfernte Outlier.
    """

    num_outliers = int(num_points * outlier_ratio)
    num_normal = num_points - num_outliers

    center = [0.0] * dim

    points = []

    # normale Punkte
    for _ in range(num_normal):
        point = [
            random.gauss(center[d], cluster_spread)
            for d in range(dim)
        ]
        points.append(point)

    # Outlier
    for _ in range(num_outliers):
        point = [
            random.uniform(-outlier_distance, outlier_distance)
            for _ in range(dim)
        ]
        points.append(point)

    return points


# 4. Punkte auf einer Linie
def generate_line_dataset(
    num_points: int,
    dim: int,
    noise: float = 0.1,
) -> List[Point]:
    """
    Punkte liegen ungefähr auf einer Linie.
    """

    direction = [random.uniform(-1, 1) for _ in range(dim)]

    points = []

    for i in range(num_points):
        t = i

        point = [
            t * direction[d] + random.uniform(-noise, noise)
            for d in range(dim)
        ]

        points.append(point)

    return points


# 5. Grid / Gitter
def generate_grid_dataset(
    points_per_axis: int,
    dim: int,
    spacing: float = 1.0,
) -> List[Point]:
    """
    Erzeugt ein n-dimensionales Gitter.
    Gesamtpunkte = points_per_axis^n
    """

    points = []

    def build(current, depth):
        if depth == dim:
            points.append(current[:])
            return

        for i in range(points_per_axis):
            current.append(i * spacing)
            build(current, depth + 1)
            current.pop()

    build([], 0)

    return points


# 6. Punkte auf einer Kugeloberfläche
def generate_sphere_surface_points(
    num_points: int,
    dim: int,
    radius: float = 50.0,
) -> List[Point]:
    """
    Punkte auf der Oberfläche einer n-dimensionalen Kugel.
    """

    points = []

    for _ in range(num_points):

        # zufälliger Richtungsvektor
        vec = [random.gauss(0, 1) for _ in range(dim)]

        norm = math.sqrt(sum(x*x for x in vec))

        point = [
            radius * x / norm
            for x in vec
        ]

        points.append(point)

    return points


# 7. Unterschiedliche Dichten
def generate_variable_density_clusters(
    num_points: int,
    dim: int,
) -> List[Point]:
    """
    Zwei Cluster:
    - dicht
    - dünn
    """

    points = []

    dense_center = [0.0] * dim
    sparse_center = [100.0] * dim

    for _ in range(num_points // 2):
        point = [
            random.gauss(dense_center[d], 1.0)
            for d in range(dim)
        ]
        points.append(point)

    for _ in range(num_points // 2):
        point = [
            random.gauss(sparse_center[d], 15.0)
            for d in range(dim)
        ]
        points.append(point)

    return points


# 8. Adversarial Stream
def generate_adversarial_stream(
    num_points: int,
    dim: int,
    distance: float = 1000.0
) -> List[Point]:
    """
    Punkte wechseln zwischen extrem entfernten Regionen.
    """

    points = []

    for i in range(num_points):

        sign = -1 if i % 2 == 0 else 1

        point = [
            sign * distance + random.uniform(-1, 1)
            for _ in range(dim)
        ]

        points.append(point)

    return points


def worst_case_1d(k: int) -> list[Point]:

    eps = 0.001
    result = []

    # k+1 Punkte nah beieinander sodass min_dist = 1
    for i in range(k + 1):
        result.append([float(i)])

    # Radius des ersten clusters berechnen und auf die nächste zweierpotenz aufrunden
    a = math.floor((k + 1)/2)
    b = 2 ** math.ceil(math.log2(a))

    # k-1 weitere Cluster, weit genug entfernt
    for i in range(1, k):
        cx = i * b * (8 + eps)
        result.append([cx])
        result.append([cx + b * 4 + eps])
        result.append([cx + b * 2 + eps/2])

    print(f"Optimaler Radius: {b*2+eps/2}")

    return result

def generate_worst_case(points: list[Point]) -> list[Point]:
    ...