# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = 0
        result = 0
        for i in range(len(flips)):
            right = max(right, flips[i])
            if right == i + 1:
                result += 1
        return result


flips = [3, 2, 4, 1, 5]
print(Solution().numTimesAllBlue(flips))
flips = [4, 1, 2, 3]
print(Solution().numTimesAllBlue(flips))
