# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallestPirce = float("inf")
        for price in prices:
            smallestPirce = min(smallestPirce, price)
            profit = max(profit, price - smallestPirce)
        return profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
