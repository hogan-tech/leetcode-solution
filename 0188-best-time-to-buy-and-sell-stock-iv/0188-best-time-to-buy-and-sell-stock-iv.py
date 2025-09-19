# time complexity: O(n*k)
# space complexity: O(k)
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        profit = [0 for _ in range((k + 1))]
        cost = [float("inf") for _ in range((k + 1))]
        for price in prices:
            for i in range(k):
                cost[i + 1] = min(cost[i + 1], price - profit[i])
                profit[i + 1] = max(profit[i + 1], price - cost[i + 1])
        return profit[k]

# DP
# time complexity: O(nk)
# space complexity: O(nk)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        if k * 2 >= n:
            result = 0
            for i, j in zip(prices[1:], prices[:-1]):
                result += max(0, i - j)
            return result
        dp = [[[float('-inf')] * 2 for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                if j > 0:
                    dp[i][j][1] = max(
                        dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        result = max(dp[n - 1][j][0] for j in range(k + 1))
        return result


k = 2
prices = [2, 4, 1]
print(Solution().maxProfit(k, prices))
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(Solution().maxProfit(k, prices))
