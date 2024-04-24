# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache


class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def fib(n: int) -> int:
            if n == 1 or n == 2:
                return 1
            if n == 0:
                return 0
            return fib(n-1) + fib(n-2) + fib(n-3)
        return fib(n)


print(Solution().tribonacci(5))
