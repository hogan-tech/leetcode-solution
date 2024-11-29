from cmath import inf
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:

        def getNext(number):
            totalSum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                totalSum += digit ** 2
            return totalSum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getNext(n)

        return n == 1


n = 19

print(Solution().isHappy(n))
