# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        leftPot = False
        rightPot = False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftPot = i == 0 or flowerbed[i - 1] == 0
                rightPot = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                if rightPot and leftPot:
                    flowerbed[i] += 1
                    n -= 1
            if n <= 0:
                return True
        return False


flowerbed = [1, 0, 0, 0, 0]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))
flowerbed = [1, 0, 0, 0, 1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))
