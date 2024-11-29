from collections import defaultdict
from typing import Counter, List


class DetectSquares:

    def __init__(self):
        self.pointsMap = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsMap[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        for y1 in self.pointsMap[x]:
            if y == y1:
                continue
            distance = abs(y1 - y)
            for x1 in [x-distance, x + distance]:
                total += self.pointsMap[x][y1] * \
                    self.pointsMap[x1][y] * self.pointsMap[x1][y1]
        return total


obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))
print(obj.count([14, 8]))
obj.add([11, 2])
print(obj.count([11, 10]))
