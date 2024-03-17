from typing import List
from Point import Point
import random


def readPointsFromFile(filename: str) -> List["Point"]:
    points = []
    with open(filename, "r") as file:
        for line in file:
            x, y = line.split(" ")
            point = Point(float(x), float(y))
            points.append(point)
    return points


def readPointsInstance(numInstance: int) -> List["Point"]:
    testFileNums = list(range(2, 1665))
    random.shuffle(testFileNums)
    if numInstance > 1664:
        raise ValueError("The number of instances is greater than 1664")
    inputPoints = []
    instanceTried = 0
    while instanceTried < numInstance:
        testFileNum = testFileNums.pop(-1)
        filename = "input/test-" + str(testFileNum) + ".points"
        print(filename)
        inputPoints.extend(readPointsFromFile(filename))
        instanceTried += 1
    # Removing duplicates
    inputPoints = list(set(inputPoints))
    while len(inputPoints) < 256 * numInstance:
        if len(testFileNums) == 0:
            raise ValueError("Ran out of test files")
        testFileNum = testFileNums.pop(-1)
        filename = "input/test-" + str(testFileNum) + ".points"
        print(filename)
        inputPoints.extend(readPointsFromFile(filename))
        inputPoints = list(set(inputPoints))

    inputPoints = inputPoints[: 256 * numInstance]
    return inputPoints
