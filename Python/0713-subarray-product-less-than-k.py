# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        product = 1
        for right, num in enumerate(nums):
            product *= num
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            result += right - left + 1
        return result


nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))
nums = [1, 2, 3]
k = 0
print(Solution().numSubarrayProductLessThanK(nums, k))
