# time complexity: O(n^2)
# space complexity: O(n)
import math
from typing import List


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for right in range(1, n + 1):
            for left in range(1, right + 1):
                if math.gcd(nums[left - 1], nums[right - 1]) > 1:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]


nums = [2, 6, 3, 4, 3]
print(Solution().validSubarraySplit(nums))
nums = [3, 5]
print(Solution().validSubarraySplit(nums))
nums = [1, 2, 1]
print(Solution().validSubarraySplit(nums))
