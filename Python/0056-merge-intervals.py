# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        if intervals:
            stack.append(intervals[0])

        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            prevInterval = stack[-1]
            if prevInterval[1] < currInterval[0]:
                stack.append(currInterval)
            elif prevInterval[1] < currInterval[1]:
                    stack[-1][1] = currInterval[1]

        return stack

'''
[1, 5] -> [2, 6] -> [1, 6]
          [2, 4] -> [1, 5]
          [6, 9] -> [1, 5] [6, 9]

'''

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
intervals = [[1, 4], [4, 5]]
print(Solution().merge(intervals))
intervals = [[1, 4], [2, 3]]
print(Solution().merge(intervals))
intervals = [[1, 4], [1, 4]]
print(Solution().merge(intervals))
