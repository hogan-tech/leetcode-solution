# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        k = -float("inf")
        ans = 0
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        return ans


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(Solution().eraseOverlapIntervals(intervals))
