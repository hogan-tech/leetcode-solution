# time complexity: O(n^3)
# space complexity: O(1)
from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return 0.5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1] - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])

        return max(area(p, q, r) for p, q, r in combinations(points, 3))


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(Solution().largestTriangleArea(points))
points = [[1, 0], [0, 0], [0, 1]]
print(Solution().largestTriangleArea(points))
