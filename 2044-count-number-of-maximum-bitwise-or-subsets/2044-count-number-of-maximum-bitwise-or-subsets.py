# time complexity: O(n*max)
# space complexity: O(2^n)
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOrValue = 0
        dp = [0] * (1 << 17)
        dp[0] = 1

        for num in nums:
            for i in range(maxOrValue, -1, -1):
                dp[i | num] += dp[i]

            maxOrValue |= num
        return dp[maxOrValue]


nums = [3, 1]
print(Solution().countMaxOrSubsets(nums))
