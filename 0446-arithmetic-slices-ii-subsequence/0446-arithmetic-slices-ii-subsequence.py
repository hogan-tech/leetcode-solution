from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        totalCount = 0

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff < -2**31 or diff > 2**31 - 1:
                    continue

                count = dp[j][diff] if diff in dp[j] else 0

                totalCount += count
                dp[i][diff] += count + 1

        return totalCount
