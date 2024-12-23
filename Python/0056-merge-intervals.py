# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergeResult = [intervals[0]]
        for interval in intervals:
            if mergeResult[-1][1] < interval[0]:
                mergeResult.append(interval)
            else:
                mergeResult[-1][1] = max(mergeResult[-1][1], interval[1])
        return mergeResult


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
intervals = [[1, 4], [4, 5]]
print(Solution().merge(intervals))
intervals = [[1, 4], [2, 3]]
print(Solution().merge(intervals))
intervals = [[1, 4], [1, 4]]
print(Solution().merge(intervals))
