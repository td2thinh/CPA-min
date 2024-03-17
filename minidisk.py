from Point import Point
from Circle import Circle
from typing import List

# Implmentation of Welzl's algorithm
# Paper source:
#  https://people.inf.ethz.ch/emo/PublFiles/SmallEnclDisk_LNCS555_91.pdf


def minidisk(points: List["Point"]) -> "Circle":
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    else:
        import random

        randomIndex = random.randint(0, len(points) - 1)
        randomPoint = points[randomIndex]
        pointsCopy = points.copy()
        pointsCopy.remove(randomPoint)
        D = minidisk(pointsCopy)
        if not (D.contains(randomPoint)):
            boundary = []
            boundary.append(randomPoint)
            D = b_minidisk(pointsCopy, boundary)

    return D


def b_minidisk(points: List["Point"], boundary: List["Point"]) -> "Circle":
    if len(points) == 0 or len(boundary) == 3:
        return minidiskTrivial(boundary)
    else:
        import random

        randomIndex = random.randint(0, len(points) - 1)
        randomPoint = points[randomIndex]
        pointsCopy = points.copy()
        pointsCopy.remove(randomPoint)
        D = b_minidisk(pointsCopy, boundary)
        non_defined = Circle(Point(0, 0), 0)
        if (D != non_defined) and not (D.contains(randomPoint)):
            boundary.append(randomPoint)
            D = b_minidisk(pointsCopy, boundary)
            boundary.remove(randomPoint)
    return D


def minidiskTrivial(points: List["Point"]) -> "Circle":
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    elif len(points) == 1:
        return Circle(points[0], 0)
    elif len(points) == 2:
        center = centerFromTwoPoints(points[0], points[1])
        return Circle(center, center.distance(points[0]))
    else:
        # When there is 3 points, there are cases where the circle can be found
        # with 2 points, .ie when the 3 points are colinear or when the 3 points
        # form a certain kinds of triangle .ie isosceles triangle, equilateral,
        # right-angled triangle
        for i in range(3):
            for j in range(i + 1, 3):
                center = centerFromTwoPoints(points[i], points[j])
                radius = center.distance(points[i])
                if center.distance(points[j]) > radius:
                    radius = center.distance(points[j])
                candidate = Circle(center, points[i].distance(center))
                if candidate.isMiniDisk(points):
                    return candidate
    # Here we are certain that the circle is not found with 2 points of the 3
    return circleFromThreePoints(points[0], points[1], points[2])


def vectorLength(point):
    return point.x * point.x + point.y * point.y


# Calculating circumcenter of 3 points in 2D
# Source: https://en.wikipedia.org/wiki/Circumcircle [Circumcenter coordinates section]
def circleFromThreePoints(p1: "Point", p2: "Point", p3: "Point") -> "Circle":
    determinant = (
        p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    ) * 2
    if determinant == 0:
        return Circle(Point(0, 0), 0)
    x = (
        (vectorLength(p1) * (p2.y - p3.y))
        + (vectorLength(p2) * (p3.y - p1.y))
        + (vectorLength(p3) * (p1.y - p2.y))
    ) / determinant

    y = (
        (vectorLength(p1) * (p3.x - p2.x))
        + (vectorLength(p2) * (p1.x - p3.x))
        + (vectorLength(p3) * (p2.x - p1.x))
    ) / determinant

    return Circle(Point(x, y), Point(x, y).distance(p1))


def centerFromTwoPoints(p1: "Point", p2: "Point") -> "Point":
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
