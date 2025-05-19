# time complexity: O(1)
# space complexity: O(1)
from math import isqrt


class Solution:
    def minOperations(self, k: int) -> int:
        x = isqrt(k)
        y = (x + k - 1) // x
        return x + y - 2


'''
[1]

2, 3, 4, 5

(1 + x) * x >= k

x ^ 2 + x - k = 0

-1 + sqrt(1+4k) / 2

x = 2

'''
k = 11
print(Solution().minOperations(k))
k = 1
print(Solution().minOperations(k))
