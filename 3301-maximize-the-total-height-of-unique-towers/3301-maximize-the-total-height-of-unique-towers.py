# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]):
        maximumHeight.sort()
        prevH = float('inf')
        result = 0
        for i in range(len(maximumHeight) - 1, -1, -1):
            currH = min(prevH - 1, maximumHeight[i])
            if currH <= 0:
                return -1
            result += currH
            prevH = currH
        return result


maximumHeight = [2, 2, 1]
print(Solution().maximumTotalSum(maximumHeight))
