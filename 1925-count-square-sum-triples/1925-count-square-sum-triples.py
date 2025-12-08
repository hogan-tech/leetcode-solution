# time complexity: O(n^2)
# space complexity: O(1)
from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int(sqrt(a**2 + b**2 + 1))
                if c <= n and a ** 2 + b ** 2 == c ** 2:
                    count += 1
        return count


n = 5
print(Solution().countTriples(n))
n = 10
print(Solution().countTriples(n))
