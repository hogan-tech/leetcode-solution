# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapify(nums)
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            count += 1
        return count


nums = [2, 11, 10, 1, 3]
k = 10
print(Solution().minOperations(nums, k))
nums = [1, 1, 2, 4, 9]
k = 20
print(Solution().minOperations(nums, k))
