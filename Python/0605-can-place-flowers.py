# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftpot = (i == 0) or (flowerbed[i-1] == 0)
                rightpot = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                if leftpot and rightpot:
                    flowerbed[i] += 1
                    n -= 1
        return count >= n


flowerbed = [1, 0, 0, 0, 0]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))
