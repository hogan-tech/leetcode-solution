# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache
from math import factorial


class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        MOD = 10**9
        dp = [[1] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
        return dp[r-1][c-1]


# time complexity: O((m + n)(log(m + n) * log(log(m + n)) ^ 2))
# space complexity: O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)


m = 3
n = 7
print(Solution().uniquePaths(m, n))
m = 3
n = 2
print(Solution().uniquePaths(m, n))
