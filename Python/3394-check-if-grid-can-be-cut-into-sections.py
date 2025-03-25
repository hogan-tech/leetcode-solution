# time complexity: O(nlogn)
# space complexity: O(s)
from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def checkCuts(rectangles: List[List[int]], dim: int) -> bool:
            gapCount = 0

            rectangles.sort(key=lambda rect: rect[dim])

            furthestEnd = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]
                if furthestEnd <= rect[dim]:
                    gapCount += 1
                furthestEnd = max(furthestEnd, rect[dim + 2])

            return gapCount >= 2

        return checkCuts(rectangles, 0) or checkCuts(rectangles, 1)


'''
2, 2, 3, 2, 3, 4, 4


1 3 
'''
n = 5
rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
print(Solution().checkValidCuts(n, rectangles))
n = 4
rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
print(Solution().checkValidCuts(n, rectangles))
n = 4
rectangles = [[0, 2, 2, 4], [1, 0, 3, 2], [
    2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]
print(Solution().checkValidCuts(n, rectangles))
