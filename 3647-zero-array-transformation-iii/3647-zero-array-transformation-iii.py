# time complexity: O(n + mlogm)
# space complexity: O(n)
from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queue = deque(sorted(queries))
        available = []
        working = []
        for i in range(len(nums)):
            while queue and queue[0][0] <= i:
                heappush(available, -queue.popleft()[1])
            while working and working[0] < i:
                heappop(working)
            while nums[i] > len(working):
                if available and -available[0] >= i:
                    heappush(working, -heappop(available))
                else:
                    return -1
        return len(available)


nums = [2, 0, 2]
queries = [[0, 2], [0, 2], [1, 1]]
print(Solution().maxRemoval(nums, queries))
nums = [1, 1, 1, 1]
queries = [[1, 3], [0, 2], [1, 3], [1, 2]]
print(Solution().maxRemoval(nums, queries))
nums = [1, 2, 3, 4]
queries = [[0, 3]]
print(Solution().maxRemoval(nums, queries))
