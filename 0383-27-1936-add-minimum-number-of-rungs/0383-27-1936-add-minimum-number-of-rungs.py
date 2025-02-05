# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        curr = 0
        result = 0
        for rung in rungs:
            result += (rung - curr - 1) // dist
            curr = rung

        return result


rungs = [4, 8, 12, 16]
dist = 3
print(Solution().addRungs(rungs, dist))
rungs = [1, 3, 5, 10]
dist = 2
print(Solution().addRungs(rungs, dist))
rungs = [3, 6, 8, 10]
dist = 3
print(Solution().addRungs(rungs, dist))
rungs = [3, 4, 6, 7]
dist = 2
print(Solution().addRungs(rungs, dist))
