# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            currX, currY = points[i]
            targetX, targetY = points[i + 1]
            ans += max(abs(targetX - currX), abs(targetY - currY))

        return ans


points = [[1, 1], [3, 4], [-1, 0]]
print(Solution().minTimeToVisitAllPoints(points))
