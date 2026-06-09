from itertools import combinations
from typing import Callable

from algorithms.online.streaming_k_center import StreamingKCenter
from model.types import Point, Solution


class DoublingKCenter(StreamingKCenter):

    def __init__(self, k: int, d: Callable[[Point, Point], float]):

        self.k = k
        self.d = d

        self.alpha: float = 2
        self.beta: float = 2

        self.centers: list[Point] = []
        self.r: float = 0
        
        self._initialized = False


    def insert(self, point: Point) -> None:

        if not self._initialized:
            self.centers.append(point)
            if len(self.centers) == self.k + 1:
                self._initialize()
        else:
            self._update_stage(point)
            while len(self.centers) >= self.k + 1:
                # Nächste Phase startet ab hier
                self._merge_stage()

    def query(self) -> Solution:
        return self.alpha * 2 * self.r, self.centers


    def _initialize(self) -> None:

        # initialisiere r mit dem halben minimalen Zentrenabstand
        min_dist = min(self.d(a, b) for a, b in combinations(self.centers, 2))
        self.r = min_dist / 2

        # Phase mit der merge stage starten, da k+1 Zentren vorhanden sind
        self._merge_stage()

        self._initialized = True


    def _merge_stage(self) -> None:

        self.r *= self.beta

        merged = []

        while self.centers:
            current = self.centers.pop(0)
            merged.append(current)

            # Entferne alle Nachbarn aus der Zentrumsmenge
            self.centers = [
                c for c in self.centers
                if self.d(current, c) > self.r * 2
            ]

        self.centers = merged


    def _update_stage(self, point: Point) -> None:

        closest = min(self.centers, key=lambda c: self.d(c, point))

        # Neues Zentrum erstellen, falls das nächste Zentrum zu weit entfernt ist
        if self.d(closest, point) > self.alpha * 2 * self.r:
            self.centers.append(point)

