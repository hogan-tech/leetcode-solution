# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
