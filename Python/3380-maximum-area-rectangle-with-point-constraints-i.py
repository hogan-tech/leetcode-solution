# time complexity: O(n)
# space complexity: O(n)
from itertools import combinations
from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        pointSet = set(map(tuple, points))
        maxArea = -1
        for (x1, y1), (x2, y2) in combinations(points, 2):
            if x1 != x2 and y1 != y2:
                if (x1, y2) in pointSet and (x2, y1) in pointSet:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    valid = True
                    for px, py in pointSet:
                        if (x1 < px < x2 or x2 < px < x1) and (y1 < py < y2 or y2 < py < y1):
                            valid = False
                            break
                        if (px == x1 or px == x2) and (min(y1, y2) < py < max(y1, y2)):
                            valid = False
                            break
                        if (py == y1 or py == y2) and (min(x1, x2) < px < max(x1, x2)):
                            valid = False
                            break
                    if valid:
                        maxArea = max(maxArea, area)

        return maxArea


points = [[1, 1], [1, 3], [3, 1], [3, 3]]
print(Solution().maxRectangleArea(points))
points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
print(Solution().maxRectangleArea(points))
points = [[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [3, 2]]
print(Solution().maxRectangleArea(points))
points = [[96, 44], [23, 72], [96, 72], [23, 44], [65, 44]]
print(Solution().maxRectangleArea(points))
