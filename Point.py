from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def distance(self, other: "Point") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
