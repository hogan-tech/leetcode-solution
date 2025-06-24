# time complexity: O(logn)
# space complexity: O(logn)
from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @lru_cache(None)
        def binaryExp(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n < 0:
                return 1.0 / binaryExp(x, -n)
            if n % 2:
                return x * binaryExp(x * x, (n - 1) // 2)
            else:
                return binaryExp(x * x, n // 2)
        return binaryExp(x, n)

# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            x *= x
            n //= 2
        return result


x = 2.00000
n = 10
print(Solution().myPow(x, n))
x = 2.10000
n = 3
print(Solution().myPow(x, n))
x = 2.00000
n = -2
print(Solution().myPow(x, n))
