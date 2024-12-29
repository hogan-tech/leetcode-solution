# time complexity: O(x + klogx)
# space complexity: O(x)
from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        n = len(matrix)
        for r in range(min(k, n)):
            heappush(minHeap, (matrix[r][0], r, 0))

        while k:
            currVal, currR, currC = heappop(minHeap)
            if currC < n - 1:
                heappush(minHeap, (matrix[currR][currC + 1], currR, currC+1))
            k -= 1
        return currVal


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix, k))
matrix = [[-5]]
k = 1
print(Solution().kthSmallest(matrix, k))
