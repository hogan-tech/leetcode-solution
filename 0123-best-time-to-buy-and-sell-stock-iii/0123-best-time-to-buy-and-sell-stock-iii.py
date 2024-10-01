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
        leftProfits = [0] * length
        rightProfits = [0] * (length + 1)

        for l in range(1, length):
            leftProfits[l] = max(leftProfits[l - 1], prices[l] - leftMin)
            leftMin = min(leftMin, prices[l])

            r = length - 1 - l
            rightProfits[r] = max(rightProfits[r + 1], rightMax - prices[r])
            rightMax = max(rightMax, prices[r])

        maxProfit = 0
        print(leftProfits)
        print(rightProfits)
        for i in range(0, length):
            maxProfit = max(maxProfit, leftProfits[i] + rightProfits[i + 1])

        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
# leftProfit = [0, 0, 4, 4, 5, 5]
# rightProfit = [5, 5, 3, 3, 0, 0, 0]
print(Solution().maxProfit(prices))
