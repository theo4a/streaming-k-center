import json
import os
from typing import Callable

from algorithms.online.streaming_k_center import StreamingKCenter
from model.types import Solution, Point



def simulate_online(
    streaming_algo: StreamingKCenter,
    points: list[Point],
    snapshots_points: list[int]
) -> list[Solution]:

    solutions: list[Solution] = []
    inserted_points: list[Point] = []

    for i, point in enumerate(points):

        streaming_algo.insert(point)
        inserted_points.append(point)

        if i == snapshots_points[0]-1:
            snapshots_points.pop(0)

            r, centers = streaming_algo.query()
            solutions.append(Solution(radius=r, centers=list(centers)))

        if len(snapshots_points) == 0:
            break

    return solutions


def check_radius(
    d: Callable,
    points: list[Point],
    centers: list[Point]
) -> float:

    if not points or not centers:
        raise ValueError("points und centers dürfen nicht leer sein")

    max_dist = 0.0

    for p in points:

        # minimale Distanz von p zu einem Center
        min_dist = min(d(p, c) for c in centers)

        # worst-case (Radius)
        max_dist = max(max_dist, min_dist)

    return max_dist


def write_json(file_name: str, dict: dict) -> None:

    # Zielpfad
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "parameter",
        f"{file_name}"
    )

    # Ordner sicher erstellen
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # In Datei schreiben
    with open(path, "w", encoding="utf-8") as datei:
        json.dump(dict, datei, ensure_ascii=False, indent=4)