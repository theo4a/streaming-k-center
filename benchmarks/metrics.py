import math

from model.types import Point


def euclidean_distance(a: Point, b: Point) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def manhattan_distance(a: Point, b: Point) -> float:
    return sum(abs(x - y) for x, y in zip(a, b))

def chebyshev_distance(a: Point, b: Point) -> float:
    return max(abs(x - y) for x, y in zip(a, b))

