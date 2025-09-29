# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0

        for i in range(n + 1):
            for j in range(i + 1, min(i + 4, n + 1)):
                cost = dp[i] + costs[j - 1] + (j - i) ** 2
                if cost < dp[j]:
                    dp[j] = cost

        return dp[n]


n = 4
costs = [1, 2, 3, 4]
print(Solution().climbStairs(n, costs))
n = 4
costs = [5, 1, 6, 2]
print(Solution().climbStairs(n, costs))
n = 3
costs = [9, 8, 3]
print(Solution().climbStairs(n, costs))
