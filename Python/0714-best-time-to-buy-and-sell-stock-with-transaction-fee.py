# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)
        return free[-1]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit(prices, fee))
