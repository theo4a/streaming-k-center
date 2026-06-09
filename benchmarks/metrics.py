import math
from typing import Sequence

from model.types import Point


# Euklidische Distanz (L2)
def euclidean_distance(a: Point, b: Point) -> float:
    """
    Euklidische Distanz zwischen zwei n-dimensionalen Vektoren.
    """
    if len(a) != len(b):
        raise ValueError("Vektoren müssen gleich viele Dimensionen haben.")

    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# Manhattan-Distanz (L1)
def manhattan_distance(a: Point, b: Point) -> float:
    """
    Manhattan- bzw. Taxicab-Distanz.
    """
    if len(a) != len(b):
        raise ValueError("Vektoren müssen gleich viele Dimensionen haben.")

    return sum(abs(x - y) for x, y in zip(a, b))


# Minkowski-Distanz
def minkowski_distance(a: Point, b: Point, p: float = 2) -> float:
    """
    Allgemeine Minkowski-Distanz.
    p=1 -> Manhattan
    p=2 -> Euklidisch
    """
    if len(a) != len(b):
        raise ValueError("Vektoren müssen gleich viele Dimensionen haben.")

    if p <= 0:
        raise ValueError("p muss > 0 sein.")

    return sum(abs(x - y) ** p for x, y in zip(a, b)) ** (1 / p)


# Chebyshev-Distanz
def chebyshev_distance(a: Point, b: Point) -> float:
    """
    Maximum-Distanz.
    """
    if len(a) != len(b):
        raise ValueError("Vektoren müssen gleich viele Dimensionen haben.")

    return max(abs(x - y) for x, y in zip(a, b))


# Cosine Distance
def cosine_distance(a: Point, b: Point) -> float:
    """
    Cosine Distance = 1 - Cosine Similarity
    """
    if len(a) != len(b):
        raise ValueError("Vektoren müssen gleich viele Dimensionen haben.")

    dot_product = sum(x * y for x, y in zip(a, b))

    norm_a = math.sqrt(sum(x ** 2 for x in a))
    norm_b = math.sqrt(sum(y ** 2 for y in b))

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Nullvektoren sind nicht erlaubt.")

    cosine_similarity = dot_product / (norm_a * norm_b)

    return 1 - cosine_similarity


# Hamming-Distanz
def hamming_distance(a: Sequence, b: Sequence) -> int:
    """
    Anzahl unterschiedlicher Elemente.
    Geeignet für Strings, Binärvektoren usw.
    """
    if len(a) != len(b):
        raise ValueError("Sequenzen müssen gleich lang sein.")

    return sum(x != y for x, y in zip(a, b))
