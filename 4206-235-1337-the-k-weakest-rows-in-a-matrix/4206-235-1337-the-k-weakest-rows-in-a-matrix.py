# time complexity: O(nlogn)
# space complexity: O(k)
from heapq import heappop, heappush
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(nums: List[int]):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        minHeap = []

        for r in range(len(mat)):
            heappush(minHeap, (binarySearch(mat[r]), r))
        result = []
        for _ in range(k):
            _, currNum = heappop(minHeap)
            result.append(currNum)

        return result


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
print(Solution().kWeakestRows(mat, k))

mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
k = 1
print(Solution().kWeakestRows(mat, k))

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
print(Solution().kWeakestRows(mat, k))
