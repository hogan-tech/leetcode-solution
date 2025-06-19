# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        result = 0
        for (x2, y2), n in self.freq.items():
            xDist = abs(x2 - x1)
            yDist = abs(y2 - y1)
            if xDist == yDist and xDist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                if corner1 in self.freq and corner2 in self.freq:
                    result += n * self.freq[corner1] * self.freq[corner2]
        return result


obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))
print(obj.count([14, 8]))
obj.add([11, 2])
print(obj.count([11, 10]))
