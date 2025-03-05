# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = prices[0]
        count = 1
        result = 1
        for i in range(1, len(prices)):
            price = prices[i]
            if price == prev - 1:
                count += 1
            else:
                count = 1
            prev = price
            result += count

        return result


prices = [3, 2, 1, 4]
print(Solution().getDescentPeriods(prices))
prices = [8, 6, 7, 7]
print(Solution().getDescentPeriods(prices))
prices = [1]
print(Solution().getDescentPeriods(prices))
