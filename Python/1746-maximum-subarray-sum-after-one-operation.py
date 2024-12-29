# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        maxLeft = [0] * n
        maxRight = [0] * n
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1] + nums[i - 1], 0)

        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1] + nums[i + 1], 0)

        maxSum = 0

        for i in range(n):
            maxSum = max(maxSum, maxLeft[i] + maxRight[i] + nums[i] ** 2)
        return maxSum


nums = [2, -1, -4, -3]
print(Solution().maxSumAfterOperation(nums))
nums = [1, -1, 1, 1, -1, -1, 1]
print(Solution().maxSumAfterOperation(nums))
