# time complexity: O(logn)
# space complexity: O(1)
from math import isqrt
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def findClosestPair(n: int) -> List[int]:
            for i in range(isqrt(n), 0, -1):
                if n % i == 0:
                    return [i, n // i]

        pair1 = findClosestPair(num + 1)
        pair2 = findClosestPair(num + 2)

        return pair1 if abs(pair1[0] - pair1[1]) <= abs(pair2[0] - pair2[1]) else pair2


num = 8
print(Solution().closestDivisors(num))
num = 123
print(Solution().closestDivisors(num))
num = 999
print(Solution().closestDivisors(num))
