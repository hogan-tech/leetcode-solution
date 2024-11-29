# time complexity: O(n*k)
# space complexity: O(k)
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        profit = [0] * (k + 1)
        cost = [float("inf")] * (k + 1)
        for price in prices:
            for i in range(k):
                cost[i + 1] = min(cost[i + 1], price - profit[i])
                profit[i + 1] = max(profit[i + 1], price - cost[i + 1])
        return profit[k]

# DP
# time complexity: O(nk)
# space complexity: O(nk)
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         n = len(prices)
#         # solve special cases
#         if not prices or k == 0:
#             return 0
#         if k * 2 >= n:
#             res = 0
#             for i, j in zip(prices[1:], prices[:-1]):
#                 res += max(0, i - j)
#             return res
#         # dp[i][used_k][ishold] = balance
#         # ishold: 0 nothold, 1 hold
#         dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]
#         # set starting value
#         dp[0][0][0] = 0
#         dp[0][1][1] = -prices[0]
#         # fill the array
#         for i in range(1, n):
#             for j in range(k + 1):
#                 # transition equation
#                 dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
#                 # you can't hold stock without any transaction
#                 if j > 0:
#                     dp[i][j][1] = max(
#                         dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]
#                     )
#         res = max(dp[n - 1][j][0] for j in range(k + 1))
#         return res


k = 2
prices = [2, 4, 1]
print(Solution().maxProfit(k, prices))
