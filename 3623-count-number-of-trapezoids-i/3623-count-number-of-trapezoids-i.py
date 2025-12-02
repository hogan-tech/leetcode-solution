# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List
from math import comb

MOD = 10**9 + 7


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        yPoints = defaultdict(list)
        for x, y in points:
            yPoints[y].append(x)

        pairsPerY = []
        for y in yPoints:
            m = len(yPoints[y])
            if m >= 2:
                count = comb(m, 2)
                pairsPerY.append(count)

        sumPairs = sum(pairsPerY)
        sumSquares = sum(count * count for count in pairsPerY)
        total = (sumPairs * sumPairs - sumSquares) // 2

        return total % MOD


points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]
print(Solution().countTrapezoids(points))
points = [[0, 0], [1, 0], [0, 1], [2, 1]]
print(Solution().countTrapezoids(points))
