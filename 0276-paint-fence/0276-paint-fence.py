from functools import lru_cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        def totalWays(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k-1) * (totalWays(i-1) + totalWays(i-2))

        return totalWays(n)


n = 7
k = 2
print(Solution().numWays(n, k))
