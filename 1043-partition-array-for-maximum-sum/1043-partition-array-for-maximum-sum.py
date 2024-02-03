# time complexity: O(n * k)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curMaxI, best = 0, 0
            for j in range(1, k + 1):
                if j <= i:
                    curMaxI = max(curMaxI, arr[i - j])
                    best = max(best, dp[i - j]+curMaxI * j)
            dp[i] = best
        return dp[n]


arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(Solution().maxSumAfterPartitioning(arr, k))
