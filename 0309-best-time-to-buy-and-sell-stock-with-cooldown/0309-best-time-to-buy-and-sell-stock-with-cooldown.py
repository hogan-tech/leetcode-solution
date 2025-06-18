# time complexity: O(n)
# space complexity: O(1)
# state machine
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0
        for price in prices:
            preSold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, preSold)
        return max(sold, reset)


prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(prices))
'''
sold[i]=hold[i−1]+price[i]
held[i]=max(held[i−1],reset[i−1]−price[i])
reset[i]=max(reset[i−1],sold[i−1])
'''