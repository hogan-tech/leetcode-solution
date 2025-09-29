# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        for i, digit in enumerate(str(n)[::-1]):
            if digit != '0':
                result.append(int(digit) * (10 ** i))
        return result[::-1]


n = 537
print(Solution().decimalRepresentation(n))
n = 102
print(Solution().decimalRepresentation(n))
n = 6
print(Solution().decimalRepresentation(n))
n = 123000048272
print(Solution().decimalRepresentation(n))
