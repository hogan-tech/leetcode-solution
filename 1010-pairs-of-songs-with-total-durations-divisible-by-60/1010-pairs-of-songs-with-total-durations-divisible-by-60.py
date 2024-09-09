# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        result = 0
        for t in time:
            result += count[-t % 60]
            count[t % 60] += 1
        return result


time = [30, 20, 150, 100, 40]
print(Solution().numPairsDivisibleBy60(time))
