import heapq
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

        # NEU: Heap speichert (distanz, id_a, id_b) — O(log k) push/pop
        self.heap: list[tuple[float, int, int]] = []
        # NEU: id(Point) → Point, damit wir nach Heap-Pop das Objekt finden
        self.center_map: dict[int, Point] = {}

        self._initialized = False


    def insert(self, point: Point) -> None:

        if not self._initialized:
            self.centers.append(point)
            if len(self.centers) == self.k + 1:
                self._initialize()
        else:
            self._update_stage(point)
            while len(self.centers) >= self.k + 1:
                self._merge_stage()


    def query(self) -> Solution:
        return Solution(radius=self.alpha * self.r, centers=self.centers)


    def _initialize(self) -> None:

        min_dist = min(self.d(a, b) for a, b in combinations(self.centers, 2))
        self.r = min_dist / 2

        # NEU: center_map aufbauen
        self.center_map = {id(c): c for c in self.centers}

        # NEU: alle O(k²) Kanten einmalig in Heap einfügen
        # Jede Kante bekommt log k Credits (amortisierte Analyse aus Theorem 8)
        for a, b in combinations(self.centers, 2):
            heapq.heappush(self.heap, (self.d(a, b), id(a), id(b)))

        self._merge_stage()
        self._initialized = True


    def _merge_stage(self) -> None:

        # r verdoppeln → das ist d_{i+1} = β · d_i
        self.r *= self.beta
        threshold = self.r

        # ERSETZT: die O(k²)-while-Schleife mit List-Comprehension
        # NEU: Kanten aus Heap extrahieren, die unter dem Threshold liegen
        # Kosten: O(m log k), gedeckt durch die log-k-Credits der Kanten
        merged_into: dict[int, int] = {}  # id_b → id_a (wer wird in wen gemergt)

        while self.heap and self.heap[0][0] <= threshold:
            dist, id_a, id_b = heapq.heappop(self.heap)

            # Überspringe, falls eines der Zentren bereits gemergt wurde
            # (Union-Find wäre noch sauberer, reicht hier aber für k klein)
            root_a = self._find_root(id_a, merged_into)
            root_b = self._find_root(id_b, merged_into)

            if root_a != root_b:
                # b in a mergen: b aus aktiven Zentren entfernen
                merged_into[root_b] = root_a

        # Zentrumsliste aus center_map neu aufbauen — nur nicht-gemergde Zentren
        active_ids = {
            self._find_root(cid, merged_into)
            for cid in list(self.center_map.keys())
        }
        self.centers = [self.center_map[cid] for cid in active_ids
                        if cid in self.center_map]
        self.center_map = {id(c): c for c in self.centers}


    def _find_root(self, cid: int, merged_into: dict[int, int]) -> int:
        # Pfadkompression für Union-Find
        while cid in merged_into:
            merged_into[cid] = merged_into.get(merged_into[cid], merged_into[cid])
            cid = merged_into[cid]
        return cid


    def _update_stage(self, point: Point) -> None:

        if not self.centers:
            self.centers.append(point)
            self.center_map[id(point)] = point
            return

        closest = min(self.centers, key=lambda c: self.d(c, point))

        # ANGEPASST: Grenze ist α · r (nicht α · 2 · r wie vorher)
        if self.d(closest, point) > self.alpha * self.r:
            # NEU: neues Zentrum → O(k) Distanzen berechnen + O(k log k) in Heap
            # Jede neue Kante bekommt log k Credits für die spätere Merge Stage
            for c in self.centers:
                heapq.heappush(self.heap, (self.d(c, point), id(c), id(point)))

            self.centers.append(point)
            self.center_map[id(point)] = point