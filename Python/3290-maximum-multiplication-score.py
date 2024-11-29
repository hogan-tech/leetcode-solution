# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [-float('inf')] * 4

        for i in range(n):
            if dp[2] != -float('inf'):
                dp[3] = max(dp[3], dp[2] + a[3] * b[i])
            if dp[1] != -float('inf'):
                dp[2] = max(dp[2], dp[1] + a[2] * b[i])
            if dp[0] != -float('inf'):
                dp[1] = max(dp[1], dp[0] + a[1] * b[i])
            dp[0] = max(dp[0], a[0] * b[i])

        return dp[3]


a = [-1, 4, 5, -2]
b = [-5, -1, -3, -2, -4]
print(Solution().maxScore(a, b))
