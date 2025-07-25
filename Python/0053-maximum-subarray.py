# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        prefix = 0
        for num in nums:
            prefix += num
            prefix = max(prefix, num)
            result = max(result, prefix)
        return result


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
nums = [1]
print(Solution().maxSubArray(nums))
nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
