# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        minSum = prices[0] + prices[1]
        if minSum <= money:
            return  money - minSum 
        return money


prices = [3, 2, 3]
money = 3


print(Solution().buyChoco(prices, money))
