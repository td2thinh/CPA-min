from Point import Point
from typing import List


class Circle:
    def __init__(self, center: "Point", radius: float) -> "Circle":
        self.center = center
        self.radius = radius

    def __str__(self) -> str:
        return "Circle(%s, %s)" % (self.center, self.radius)

    def __eq__(self, other: "Circle") -> bool:
        return self.center == other.center and self.radius == other.radius

    def contains(self, point: "Point") -> bool:
        return self.center.distance(point) <= self.radius

    def isMiniDisk(self, points: List["Point"]) -> bool:
        for point in points:
            if not self.contains(point):
                return False
        return True
