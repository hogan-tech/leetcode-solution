# time complexity: O(n)
# space complexity: O(n)
from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        @cache
        def p(n: int):
            if n == 2:
                return 1
            return (p(n-1) + f(n-2)) % MOD

        @cache
        def f(n: int):
            if n <= 2:
                return n
            return (f(n-1) + f(n-2) + 2 * p(n-1)) % MOD

        return f(n)


n = 3
print(Solution().numTilings(n))
