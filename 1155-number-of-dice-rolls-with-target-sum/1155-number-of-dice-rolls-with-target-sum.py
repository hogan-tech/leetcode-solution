from functools import lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(nLeft, sumLeft):
            if nLeft == 0 and sumLeft == 0:
                return 1
            if nLeft < 0 or sumLeft < 0:
                return 0
            res = 0
            for i in range(1, k + 1):
                res += dfs(nLeft - 1, sumLeft - i)
            return res % MOD
        return dfs(n, target)


n = 30
k = 30
target = 500
print(Solution().numRollsToTarget(n, k, target))
