# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices


prices = [8, 4, 6, 2, 3]
print(Solution().finalPrices(prices))
prices = [1, 2, 3, 4, 5]
print(Solution().finalPrices(prices))
prices = [10, 1, 1, 6]
print(Solution().finalPrices(prices))
