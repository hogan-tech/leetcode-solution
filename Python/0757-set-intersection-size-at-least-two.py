# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = []
        result.append(intervals[0][1] - 1)
        result.append(intervals[0][1])
        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]
            last = result[-1]
            secLast = result[-2]
            if start > last:
                result.append(end - 1)
                result.append(end)
            elif start == last:
                result.append(end)
            elif start > secLast:
                result.append(end)
        return len(result)


intervals = [[1, 3], [3, 7], [8, 9]]
print(Solution().intersectionSizeTwo(intervals))
intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
print(Solution().intersectionSizeTwo(intervals))
intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
print(Solution().intersectionSizeTwo(intervals))
