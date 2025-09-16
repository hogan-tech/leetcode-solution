# time complexity: O(n^2 * m)
# space complexity: O(nm)
from typing import List
from itertools import accumulate


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        maxArea = 0
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == '0':
                    continue
                width = dp[r][c] = dp[r][c-1] + 1 if c else 1
                for k in range(r, -1, -1):
                    width = min(width, dp[k][c])
                    maxArea = max(maxArea, width * (r-k+1))
        return maxArea

# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        arr = [list(map(int, row)) for row in matrix]
        COL = len(matrix[0])
        up, left, right = [0] * COL, [0] * COL, [0] * COL
        result = 0
        for row in arr:
            rowLeft = list(accumulate(row, lambda val, x: (val + x) * x))
            rowRight = list(accumulate(
                row[::-1], lambda val, x: (val + x) * x))[::-1]
            up = [(val + x) * x for val, x in zip(up, row)]
            left = [min(x, y) if u > 1 else y for x, y,
                    u in zip(left, rowLeft, up)]
            right = [min(x, y) if u > 1 else y for x, y,
                     u in zip(right, rowRight, up)]
            for u, l, r in zip(up, left, right):
                result = max(result, u * (l + r - 1))
        return result


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
matrix = [["0"]]
print(Solution().maximalRectangle(matrix))
matrix = [["1"]]
print(Solution().maximalRectangle(matrix))
