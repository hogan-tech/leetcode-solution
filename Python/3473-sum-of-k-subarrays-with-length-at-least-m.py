# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [[-float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            maxPrev = -float('inf')
            for i in range(m, n + 1):
                if i - m >= 0:
                    maxPrev = max(maxPrev, dp[i - m][j - 1])
                if maxPrev != float('inf'):
                    dp[i][j] = max(dp[i][j], maxPrev +
                                   prefix[i] - prefix[i - m])
                if i > m:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + nums[i - 1])

        result = -float('inf')
        for i in range(n + 1):
            if dp[i][k] != -float('inf'):
                result = max(result, dp[i][k])

        return result


nums = [1, 2, -1, 3, 3, 4]
k = 2
m = 2
print(Solution().maxSum(nums, k, m))
nums = [-10, 3, -1, -2]
k = 4
m = 1
print(Solution().maxSum(nums, k, m))
