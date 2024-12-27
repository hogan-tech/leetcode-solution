# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = float('-inf')
        maxLeft = 0
        for i in range(len(values)):
            result = max(result, maxLeft + values[i] - i)
            maxLeft = max(maxLeft, values[i] + i)
        return result


values = [8, 1, 5, 2, 6]
print(Solution().maxScoreSightseeingPair(values))
values = [1, 2]
print(Solution().maxScoreSightseeingPair(values))
