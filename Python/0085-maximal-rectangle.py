# time complexity: O(n^2 * m)
# space complexity: O(nm)
from typing import List
from itertools import accumulate


# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         maxArea = 0
#         dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == '0':
#                     continue
#                 width = dp[i][j] = dp[i][j-1] + 1 if j else 1
#                 for k in range(i, -1, -1):
#                     width = min(width, dp[k][j])
#                     maxArea = max(maxArea, width * (i-k+1))
#         return maxArea




class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        arr = [list(map(int, x)) for x in matrix]
        n = len(matrix[0])
        up, left, right = [0] * n, [0] * n, [0] * n
        ans = 0
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
                ans = max(ans, u * (l + r - 1))
        return ans


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
