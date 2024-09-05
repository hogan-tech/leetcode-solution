from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxAmount = max(candies)
        candiesResult = []
        for i in range(len(candies)):
            if candies[i] + extraCandies < maxAmount:
                candiesResult.append(False)
            else:
                candiesResult.append(True)
        return candiesResult


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))
