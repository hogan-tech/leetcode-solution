# time complexity: O(n^2)
# space complexity: O(n)
from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for num in range(1, n + 1):
            for denominator in range(1, n):
                if num == denominator:
                    break
                if gcd(num, denominator) == 1:
                    result.append(f"{denominator}/{num}")
        return result


n = 2
print(Solution().simplifiedFractions(n))
n = 3
print(Solution().simplifiedFractions(n))
n = 4
print(Solution().simplifiedFractions(n))
n = 6
print(Solution().simplifiedFractions(n))
