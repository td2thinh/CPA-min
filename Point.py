from math import sqrt


class Point:
    def __init__(self, x: float, y: float) -> "Point":
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def distance(self, other: "Point") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
