# time complexity: O(2 ^ (n ** 0.5))
# space complexity: O(2 ^ (n ** 0.5))
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        factors = []
        for i in range(2, n//2 + 1):
            if n % i == 0:
                factors.append(i)
        result = []

        def backtrack(start: int, balance: int, comb):
            if start == len(factors):
                return
            if balance == 1:
                if len(comb) > 1:
                    result.append(list(comb))
                return
            for i in range(start, len(factors)):
                value = factors[i]
                comb.append(value)
                if balance % value == 0:
                    backtrack(i, balance//value, comb)
                comb.pop()
        backtrack(0, n, [])
        return (result)


n = 1
print(Solution().getFactors(n))
n = 12
print(Solution().getFactors(n))
n = 37
print(Solution().getFactors(n))
