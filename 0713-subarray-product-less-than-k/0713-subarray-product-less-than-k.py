# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left, product = 0, 1
        for right, num in enumerate(nums):
            product *= num
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))
