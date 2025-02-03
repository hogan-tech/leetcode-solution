# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3:
            return []
        else:
            idx = num // 3
            return [idx - 1, idx, idx + 1]


num = 33
print(Solution().sumOfThree(num))
num = 4
print(Solution().sumOfThree(num))
