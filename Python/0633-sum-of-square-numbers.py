# time complexity: O(c^-2 * logc)
# space complexity: O(1)
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a*a)
            if int(b) == b:
                return True
        return False


c = 3
print(Solution().judgeSquareSum(c))
