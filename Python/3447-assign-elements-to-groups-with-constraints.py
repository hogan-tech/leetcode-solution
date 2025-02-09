# time complexity: O(n)
# space complexity: O(n)
import math
from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        divisorMap = {}
        for i, element in enumerate(elements):
            if element not in divisorMap:
                divisorMap[element] = i

        result = []

        for group in groups:
            tempIdx = float('inf')

            for d in range(1, int(math.sqrt(group)) + 1):
                if group % d == 0:
                    if d in divisorMap:
                        tempIdx = min(tempIdx, divisorMap[d])
                    if group // d in divisorMap:
                        tempIdx = min(tempIdx, divisorMap[group // d])

            tempIdx = tempIdx if tempIdx != float('inf') else -1
            result.append(tempIdx)
        return result


groups = [8, 4, 3, 2, 4]
elements = [4, 2]
print(Solution().assignElements(groups, elements))
groups = [2, 3, 5, 7]
elements = [5, 3, 3]
print(Solution().assignElements(groups, elements))
groups = [10, 21, 30, 41]
elements = [2, 1]
print(Solution().assignElements(groups, elements))
