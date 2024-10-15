# time complexity: O(n*m)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for p, f in zip(present, future):
            for i in range(budget, p-1, -1):
                dp[i] = max(dp[i], dp[i-p] + f - p)
        return dp[-1]


present = [5, 4, 6, 2, 3]
future = [8, 5, 4, 3, 5]
budget = 10
print(Solution().maximumProfit(present, future, budget))
