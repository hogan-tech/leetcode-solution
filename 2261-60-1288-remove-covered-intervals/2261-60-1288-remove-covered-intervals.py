# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prevEnd = 0
        count = 0
        for _, end in intervals:
            if end > prevEnd:
                count += 1
                prevEnd = end
        return count


intervals = [[1, 2], [1, 4], [3, 4]]
print(Solution().removeCoveredIntervals(intervals))
intervals = [[1, 4], [3, 6], [2, 8]]
print(Solution().removeCoveredIntervals(intervals))
intervals = [[1, 4], [2, 3]]
print(Solution().removeCoveredIntervals(intervals))
intervals = [[3, 10], [4, 10], [5, 11]]
print(Solution().removeCoveredIntervals(intervals))
