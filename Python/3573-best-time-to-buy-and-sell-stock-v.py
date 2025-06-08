# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if k == 0 or n < 2:
            return 0

        cash = [[-float('inf')] * n for _ in range(k+1)]
        holdBuy = [[-float('inf')] * n for _ in range(k+1)]
        holdShort = [[-float('inf')] * n for _ in range(k+1)]

        cash[0][0] = 0
        holdBuy[0][0] = -prices[0]
        holdShort[0][0] = prices[0]

        for i in range(1, n):
            for t in range(k+1):
                cash[t][i] = cash[t][i-1]
                if t > 0:
                    if holdBuy[t-1][i-1] != -float('inf'):
                        cash[t][i] = max(
                            cash[t][i], holdBuy[t-1][i-1] + prices[i])
                    if holdShort[t-1][i-1] != -float('inf'):
                        cash[t][i] = max(
                            cash[t][i], holdShort[t-1][i-1] - prices[i])

                holdBuy[t][i] = holdBuy[t][i-1]
                if cash[t][i-1] != -float('inf'):
                    holdBuy[t][i] = max(
                        holdBuy[t][i], cash[t][i-1] - prices[i])

                holdShort[t][i] = holdShort[t][i-1]
                if cash[t][i-1] != -float('inf'):
                    holdShort[t][i] = max(
                        holdShort[t][i], cash[t][i-1] + prices[i])

        maxProfit = 0
        for t in range(k+1):
            if cash[t][n-1] > maxProfit:
                maxProfit = cash[t][n-1]

        return maxProfit


prices = [1, 7, 9, 8, 2]
k = 2
print(Solution().maximumProfit(prices, k))
prices = [12, 16, 19, 19, 8, 1, 19, 13, 9]
k = 3
print(Solution().maximumProfit(prices, k))
