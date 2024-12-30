# time complexity: O(nlogk)
# space complexity: O(k)
from heapq import heapify, heappop
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(sqrt(x**2 + y**2), x, y) for x, y in points]
        heapify(minHeap)
        result = []
        while k:
            _, currX, currY = heappop(minHeap)
            result.append([currX, currY])
            k -= 1
        return result


points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest(points, k))
