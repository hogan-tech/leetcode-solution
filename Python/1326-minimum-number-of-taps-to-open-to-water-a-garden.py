from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            tapStart = max(0, i-ranges[i])
            tapEnd = min(n, i+ranges[i])
            for j in range(tapStart, tapEnd + 1):
                dp[tapEnd] = min(dp[tapEnd], dp[j] + 1)
        if dp[n] == float('inf'):
            return -1
        return dp[n]


n = 5
ranges = [3, 4, 1, 1, 0, 0]
print(Solution().minTaps(n, ranges))
