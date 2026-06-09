from typing import Callable

from algorithms.online.doubling_k_center import DoublingKCenter
from model.types import Point


class ScalingKCenter(DoublingKCenter):

    def __init__(self, k: int, d: Callable[[Point, Point], float], beta: float, r0: float):

        self.k = k
        self.d = d

        self.alpha = beta/(beta-1)
        self.beta = beta

        self.centers: list[Point] = []
        self.r: float = r0
        
        self._initialized = False

    def _initialize(self) -> None:

        # Phase mit der merge stage starten, da k+1 Zentren vorhanden sind
        self._merge_stage()

        self._initialized = True