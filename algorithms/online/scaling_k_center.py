import heapq
from itertools import combinations
from typing import Callable

from algorithms.online.doubling_k_center import DoublingKCenter
from model.types import Point


class ScalingKCenter(DoublingKCenter):

    def __init__(self, k: int, d: Callable[[Point, Point], float], beta: float, r0: float):

        self.k = k
        self.d = d

        self.alpha = beta / (beta - 1)
        self.beta = beta

        self.centers: list[Point] = []
        self.r: float = r0

        # NEU: wie in DoublingKCenter.__init__
        self.heap: list[tuple[float, int, int]] = []
        self.center_map: dict[int, Point] = {}

        self._initialized = False

    def _initialize(self) -> None:
    
        # r bleibt r0, kein min_dist nötig
    
        # NEU: wie in DoublingKCenter._initialize
        self.center_map = {id(c): c for c in self.centers}
    
        for a, b in combinations(self.centers, 2):
            heapq.heappush(self.heap, (self.d(a, b), id(a), id(b)))
    
        self._merge_stage()
        self._initialized = True