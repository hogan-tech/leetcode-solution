# time complexity: O(nlogm)
# space complexity: O(1)
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = 1
        right = max(nums)
        n = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            thefts = 0
            i = 0
            while i < n:
                if nums[i] <= mid:
                    thefts += 1
                    i += 2
                else:
                    i += 1
            if thefts >= k:
                right = mid
            else:
                left = mid + 1
        return left


nums = [2, 3, 5, 9]
k = 2
print(Solution().minCapability(nums, k))
nums = [2, 7, 9, 3, 1]
k = 2
print(Solution().minCapability(nums, k))
