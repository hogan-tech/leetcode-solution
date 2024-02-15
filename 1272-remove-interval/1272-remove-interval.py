# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        removeStart, removeEnd = toBeRemoved
        for start, end in intervals:
            if start > removeEnd or end < removeStart:
                ans.append([start, end])
            else:
                if start < removeStart:
                    ans.append([start, removeStart])
                if end > removeEnd:
                    ans.append([removeEnd, end])
        return ans


intervals = [[0, 2], [3, 4], [5, 7]]
toBeRemoved = [1, 6]
print(Solution().removeInterval(intervals, toBeRemoved))
