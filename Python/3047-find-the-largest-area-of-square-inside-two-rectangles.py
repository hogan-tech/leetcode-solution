# time complexity: O(n^2)
# space complexity: O(1)
from itertools import combinations
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxSize = 0
        for (bottomLeftI, topRightI), (bottomLeftJ, topRightJ,) in combinations(zip(bottomLeft, topRight), 2):
            w = min(topRightI[0], topRightJ[0]) - \
                max(bottomLeftI[0], bottomLeftJ[0])
            h = min(topRightI[1], topRightJ[1]) - \
                max(bottomLeftI[1], bottomLeftJ[1])
            maxSize = max(maxSize, min(w, h))
        return maxSize * maxSize


bottomLeft = [[1, 1], [2, 2], [3, 1]]
topRight = [[3, 3], [4, 4], [6, 6]]
print(Solution().largestSquareArea(bottomLeft, topRight))
bottomLeft = [[1, 1], [1, 3], [1, 5]]
topRight = [[5, 5], [5, 7], [5, 9]]
print(Solution().largestSquareArea(bottomLeft, topRight))
bottomLeft = [[1, 1], [2, 2], [1, 2]]
topRight = [[3, 3], [4, 4], [3, 4]]
print(Solution().largestSquareArea(bottomLeft, topRight))
bottomLeft = [[1, 1], [3, 3], [3, 1]]
topRight = [[2, 2], [4, 4], [4, 2]]
print(Solution().largestSquareArea(bottomLeft, topRight))
