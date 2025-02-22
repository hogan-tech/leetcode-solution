# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop
from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xSet = set()
        for x, _ in points:
            xSet.add(x)
        hp = list(xSet)
        heapify(hp)
        count = 0
        while hp:
            currX = hp[0]
            while hp and hp[0] <= currX + w:
                heappop(hp)
            count += 1
        return count


points = [[1, 3], [8, 8]]
w = 1
print(Solution().minRectanglesToCoverPoints(points, w))
points = [[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]]
w = 1
print(Solution().minRectanglesToCoverPoints(points, w))
points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
w = 2
print(Solution().minRectanglesToCoverPoints(points, w))
points = [[2, 3], [1, 2]]
w = 0
print(Solution().minRectanglesToCoverPoints(points, w))
