# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        profit, smallestPrice = 0, 99999
        for price in prices:
            if price < smallestPrice:
                smallestPrice = price
            else:
                profit = max(profit, price - smallestPrice)
        return profit


PriceList = [7, 1, 5, 3, 6, 4]

solution = Solution()

print(solution.maxProfit(PriceList))
