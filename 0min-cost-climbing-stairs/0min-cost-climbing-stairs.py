from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i: int, cost: List[int]):
            if i <= 1:
                return 0
            if i not in memo:
                memo[i] = min(dp(i-1, cost) + cost[i-1],
                              dp(i-2, cost) + cost[i - 2])
            return memo[i]
        memo = {}
        return dp(len(cost), cost)


cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
