from abc import ABC, abstractmethod

from benchmarks.metrics import Point
from model.types import Solution

class StreamingKCenter(ABC):

    @abstractmethod
    def insert(self, point: Point) -> None:
        pass

    @abstractmethod
    def query(self) -> Solution:
        pass

