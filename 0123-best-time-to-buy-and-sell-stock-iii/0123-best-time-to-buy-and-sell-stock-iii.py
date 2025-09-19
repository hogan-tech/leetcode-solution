# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        leftMin = prices[0]
        rightMax = prices[-1]
        length = len(prices)
        leftProfits = [0 for _ in range(length)]
        rightProfits = [0 for _ in range(length + 1)] 
        for l in range(1, length):
            leftProfits[l] = max(leftProfits[l - 1], prices[l] - leftMin)
            leftMin = min(leftMin, prices[l])
            r = length - 1 - l
            rightProfits[r] = max(rightProfits[r + 1], rightMax - prices[r])
            rightMax = max(rightMax, prices[r])
        maxProfit = 0
        for i in range(0, length):
            maxProfit = max(maxProfit, leftProfits[i] + rightProfits[i + 1])
        return maxProfit

# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        t1Cost = float("inf")
        t2Cost = float("inf")
        t1Profit = 0
        t2Profit = 0

        for price in prices:
            t1Cost = min(t1Cost, price)
            t1Profit = max(t1Profit, price - t1Cost)
            t2Cost = min(t2Cost, price - t1Profit)
            t2Profit = max(t2Profit, price - t2Cost)

        return t2Profit

prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(Solution().maxProfit(prices))
prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))
