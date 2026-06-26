import csv
import json
import os
from typing import Callable

from algorithms.online.streaming_k_center import StreamingKCenter
from model.types import Solution, Point

def simulate_offline(
    k: int,
    d: Callable,
    offline_algo: Callable,
    points: list[Point],
) -> Solution:
    
    solution: Solution
    for i in range(len(points)):
        if i > k:
            solution = offline_algo(k, d, points[:i])

    return solution

def simulate_streaming(
    streaming_algo: StreamingKCenter,
    points: list[Point]
) -> Solution:

    for point in points:
        streaming_algo.insert(point)

    return streaming_algo.query()

def check_radius(
    d: Callable,
    points: list[Point],
    centers: list[Point]
) -> float:

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
        "data",
        f"{file_name}.json"
    )

    # Ordner sicher erstellen
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # In Datei schreiben
    with open(path, "w", encoding="utf-8") as datei:
        json.dump(dict, datei, ensure_ascii=False, indent=4)

def write_csv(file_name: str, rows: list[dict], fieldnames: list) -> None:

    # Zielpfad
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "results",
        "data",
        f"{file_name}.csv"
    )

    # Ordner sicher erstellen
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)