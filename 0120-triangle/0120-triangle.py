# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for c in range(r + 1):
                smallestAbove = float('inf')
                if c > 0:
                    smallestAbove = triangle[r-1][c-1]
                if c < r:
                    smallestAbove = min(smallestAbove, triangle[r-1][c])
                triangle[r][c] += smallestAbove
        return min(triangle[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))
