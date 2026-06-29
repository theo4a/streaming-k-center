import heapq
from itertools import combinations
import math
import random
from typing import Callable

from algorithms.online.doubling_k_center import DoublingKCenter
from model.types import Point


class RandomizedDoublingKCenter(DoublingKCenter):

    def __init__(self, k: int, d: Callable[[Point, Point], float]):

        self.k = k
        self.d = d

        self.alpha: float = math.e / (math.e - 1)
        self.beta: float = math.e

        self.r: float = 0

        self.distances: list[tuple[float, int, int]] = []
        self.centers: dict[int, Point] = {}

        self._initialized = False


    def _initialize(self) -> None:

        points = list(self.centers.values())
        min_dist = min(self.d(a, b) for a, b in combinations(points, 2))
        x = min_dist / 2

        v = random.random()
        u = math.exp(v - 1)

        self.r = x * u

        for a, b in combinations(points, 2):
            heapq.heappush(self.distances, (self.d(a, b), id(a), id(b)))

        self._merge_stage()
        self._initialized = True