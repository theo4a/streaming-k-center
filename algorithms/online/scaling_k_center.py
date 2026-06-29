import heapq
from itertools import combinations
from typing import Callable

from algorithms.online.doubling_k_center import DoublingKCenter
from model.types import Point


class ScalingKCenter(DoublingKCenter):

    def __init__(self, k: int, d: Callable[[Point, Point], float], beta: float, r1: float):

        self.k = k
        self.d = d

        self.alpha = beta / (beta - 1)
        self.beta = beta

        self.r: float = r1

        self.distances: list[tuple[float, int, int]] = []
        self.centers: dict[int, Point] = {}

        self._initialized = False


    def _initialize(self) -> None:

        points = list(self.centers.values())

        for a, b in combinations(points, 2):
            heapq.heappush(self.distances, (self.d(a, b), id(a), id(b)))

        self._merge_stage()
        self._initialized = True