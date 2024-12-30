# time complexity: O(nlogk)
# space complexity: O(k)
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        for i, num in enumerate(nums):
            heappush(minHeap, (num, i))
            if len(minHeap) > k:
                heappop(minHeap)
        return [num for num, _ in sorted(minHeap, key=lambda item: item[1])]


nums = [2, 1, 3, 3]
k = 2
print(Solution().maxSubsequence(nums, k))
nums = [-1, -2, 3, 4]
k = 3
print(Solution().maxSubsequence(nums, k))
nums = [3, 4, 3, 3]
k = 2
print(Solution().maxSubsequence(nums, k))
