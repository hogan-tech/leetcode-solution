# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        maxForVal = {}
        for xi, yi in zip(x, y):
            if xi not in maxForVal or yi > maxForVal[xi]:
                maxForVal[xi] = yi

        if len(maxForVal) < 3:
            return -1

        topThree = sorted(maxForVal.values(), reverse=True)[:3]
        return sum(topThree)


x = [1, 2, 1, 3, 2]
y = [5, 3, 4, 6, 2]
print(Solution().maxSumDistinctTriplet(x, y))
x = [1, 2, 1, 2]
y = [4, 5, 6, 7]
print(Solution().maxSumDistinctTriplet(x, y))
