# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        firstEnd = points[0][1]
        for pointStart, pointEnd in points:
            if firstEnd < pointStart:
                arrows += 1
                firstEnd = pointEnd
        return arrows


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(Solution().findMinArrowShots(points))
