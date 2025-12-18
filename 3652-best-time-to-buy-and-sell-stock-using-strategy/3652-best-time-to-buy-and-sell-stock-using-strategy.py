# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = sum(p * s for p, s in zip(prices, strategy))

        half = k // 2

        conPrefix = [0]*(n+1)
        for i in range(n):
            conPrefix[i+1] = conPrefix[i] + strategy[i]*prices[i]

        pricePrefix = [0]*(n+1)
        for i in range(n):
            pricePrefix[i+1] = pricePrefix[i] + prices[i]

        bestDelta = 0

        for l in range(n-k+1):
            mid = l+half
            r = l+k

            loss = conPrefix[mid] - conPrefix[l]

            gain = (pricePrefix[r] - pricePrefix[mid]) - \
                (conPrefix[r] - conPrefix[mid])

            delta = -loss + gain
            if delta > bestDelta:
                bestDelta = delta

        return base + bestDelta


prices = [4, 2, 8]
strategy = [-1, 0, 1]
k = 2
print(Solution().maxProfit(prices, strategy, k))
prices = [5, 4, 3]
strategy = [1, 1, 0]
k = 2
print(Solution().maxProfit(prices, strategy, k))
