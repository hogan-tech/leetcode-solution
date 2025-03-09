# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[i] = 0
                    break
        return len(baskets) - baskets.count(0)


fruits = [4, 2, 5]
baskets = [3, 5, 4]
print(Solution().numOfUnplacedFruits(fruits, baskets))
fruits = [3, 6, 1]
baskets = [6, 4, 7]
print(Solution().numOfUnplacedFruits(fruits, baskets))
