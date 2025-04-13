# time complexity: O(n^2)
# space complexity: O(n^2)
from functools import lru_cache


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7

        def decToBase(s: str, base: int) -> list:
            num = int(s)
            if num == 0:
                return [0]
            digits = []
            while num:
                digits.append(num % base)
                num //= base
            return digits[::-1]

        def decStrMinusOne(s: str) -> str:
            n = int(s)
            if n == 0:
                return "-1"
            else:
                return str(n-1)

        digitsR = decToBase(r, b)
        maxLen = len(digitsR)
        maxN = maxLen + b

        comb = [[0]*(maxN+1) for _ in range(maxN+1)]
        for i in range(maxN+1):
            comb[i][0] = 1
            for j in range(1, i+1):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        def countCombinatorial(m: int) -> int:
            return comb[m + b - 2][m]

        def countUpto(x: str) -> int:
            if x == "-1":
                return 0
            if int(x) == 0:
                return 1

            digits = decToBase(x, b)
            n = len(digits)
            total = 0
            for m in range(1, n):
                total = (total + countCombinatorial(m)) % MOD

            @lru_cache(maxsize=None)
            def dp(pos: int, prev: int, tight: bool) -> int:
                if pos == n:
                    return 1
                limit = digits[pos] if tight else (b - 1)
                ways = 0
                if pos == 0:

                    for d in range(1, limit + 1):
                        newTight = (tight and d == limit)
                        ways = (ways + dp(pos+1, d, newTight)) % MOD
                else:

                    for d in range(prev, limit + 1):
                        newTight = (tight and d == limit)
                        ways = (ways + dp(pos+1, d, newTight)) % MOD
                return ways

            total = (total + dp(0, 0, True)) % MOD
            return (total + 1) % MOD
        lMinus = decStrMinusOne(l)
        result = (countUpto(r) - countUpto(lMinus)) % MOD
        return result


l = "23"
r = "28"
b = 8
print(Solution().countNumbers(l, r, b))
l = "2"
r = "7"
b = 2
print(Solution().countNumbers(l, r, b))
l = "1"
r = "1"
b = 2
print(Solution().countNumbers(l, r, b))
