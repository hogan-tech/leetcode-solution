# time complexity: O(n * nlogn)
# space complexity: O(n)
import bisect
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 != stone2:
                bisect.insort(stones, stone1 - stone2)
        return stones[0] if stones else 0


stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeight(stones))
