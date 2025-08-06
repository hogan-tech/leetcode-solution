# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        maxLen = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            maxLen = max(maxLen, right - left + 1)

        return n - maxLen


nums = [2, 1, 5]
k = 2
print(Solution().minRemoval(nums, k))
nums = [1, 6, 2, 9]
k = 3
print(Solution().minRemoval(nums, k))
nums = [4, 6]
k = 2
print(Solution().minRemoval(nums, k))
