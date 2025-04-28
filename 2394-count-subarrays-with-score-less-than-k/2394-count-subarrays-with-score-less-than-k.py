# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            result += right - left + 1
        return result


nums = [2, 1, 4, 3, 5]
k = 10
print(Solution().countSubarrays(nums, k))
nums = [1, 1, 1]
k = 5
print(Solution().countSubarrays(nums, k))
