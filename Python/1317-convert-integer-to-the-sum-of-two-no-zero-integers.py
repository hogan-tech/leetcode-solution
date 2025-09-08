# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]


n = 2
print(Solution().getNoZeroIntegers(n))
n = 11
print(Solution().getNoZeroIntegers(n))
n = 1010
print(Solution().getNoZeroIntegers(n))
