# time complexity: O(n)
# space complexity: O(nlogn)
from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        @lru_cache(None)
        def dp(i, k):
            if i == n-1:
                return True
            ans = False
            for jump in [k-1, k, k + 1]:
                if jump == 0:
                    continue
                next = bisect_left(stones[i+1:], stones[i] + jump) + (i + 1)
                if next == n or stones[next] != stones[i] + jump:
                    continue
                ans = ans or dp(next, jump)
            return ans

        return dp(0, 0)


stones = [0, 1, 3, 5, 6, 8, 12, 17]
print(Solution().canCross(stones))
stones = [0, 1, 2, 3, 4, 8, 9, 11]
print(Solution().canCross(stones))
