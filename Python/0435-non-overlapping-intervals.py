# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevEnd = float('-inf')
        result = 0
        for start, end in intervals:
            if prevEnd > start:
                print(prevEnd, start, end)
                result += 1
            else:
                prevEnd = end
        return result


intervals = [[1, 2], [2, 3], [3, 4], [2, 7]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1, 2], [1, 2], [1, 2]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1, 2], [2, 3]]
print(Solution().eraseOverlapIntervals(intervals))
