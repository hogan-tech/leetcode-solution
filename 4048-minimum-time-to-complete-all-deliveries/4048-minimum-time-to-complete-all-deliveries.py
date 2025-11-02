# time complexity: O(logn)
# space complexity: O(1)
from math import gcd
from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        def lcm(a, b):
            return a * b // gcd(a, b)

        LCM = lcm(r1, r2)

        left, right = 0, 10**18
        result = right

        while left <= right:
            mid = (left + right) // 2
            a1 = mid - mid // r1
            a2 = mid - mid // r2

            total = mid - mid // LCM

            if a1 >= d1 and a2 >= d2 and total >= d1 + d2:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result


d = [3, 1]
r = [2, 3]
print(Solution().minimumTime(d, r))
d = [1, 3]
r = [2, 2]
print(Solution().minimumTime(d, r))
d = [2, 1]
r = [3, 4]
print(Solution().minimumTime(d, r))
