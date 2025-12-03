# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slopeToIntercept = defaultdict(list)
        midToSlope = defaultdict(list)
        result = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slopeToIntercept[k].append(b)
                midToSlope[mid].append(k)

        for sti in slopeToIntercept.values():
            if len(sti) == 1:
                continue

            counter = defaultdict(int)
            for bVal in sti:
                counter[bVal] += 1

            totalSum = 0
            for count in counter.values():
                result += totalSum * count
                totalSum += count

        for mts in midToSlope.values():
            if len(mts) == 1:
                continue

            counter = defaultdict(int)
            for kVal in mts:
                counter[kVal] += 1

            totalSum = 0
            for count in counter.values():
                result -= totalSum * count
                totalSum += count

        return result


points = [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]
print(Solution().countTrapezoids(points))
points = [[0, 0], [1, 0], [0, 1], [2, 1]]
print(Solution().countTrapezoids(points))
