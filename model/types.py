from dataclasses import dataclass
from typing import Sequence

from pydantic import BaseModel

Point = Sequence[float]

class Solution(BaseModel):
    radius: float
    centers: list[Point]

class Snapshot(BaseModel):
    points: list[Point]
    solutions: list[Solution]