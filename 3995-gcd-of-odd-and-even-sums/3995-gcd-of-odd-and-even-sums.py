# time complexity: O(1)
# space complexity: O(1)
import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n * n
        even = n * (n + 1)
        return math.gcd(odd, even)


n = 4
print(Solution().gcdOfOddEvenSums(n))
n = 5
print(Solution().gcdOfOddEvenSums(n))
