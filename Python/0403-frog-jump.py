from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneSet = set(stones)

        @lru_cache(None)
        def solve(stone, k):
            if stone in stoneSet:
                if stone == stones[-1]:
                    return True
                for nextLeap in range(max(k-1, 1), k + 2):
                    if solve(stone + nextLeap, nextLeap):
                        return True
            return False
        return solve(0, 0)


stones = [0, 1, 3, 5, 6, 8, 12, 17]
print(Solution().canCross(stones))
