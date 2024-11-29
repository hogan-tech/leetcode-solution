# time complexity: O(mn)
# space complexity: O(mn)
from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        def getRowFlip(i):
            result = []
            flip = matrix[i][0] == 1
            for c in range(COL):
                result.append(str(1 - matrix[i][c])
                              if flip else str(matrix[i][c]))
            return ''.join(result)

        return max(Counter(getRowFlip(i) for i in range(ROW)).values())


matrix = [[0, 1], [1, 1]]
print(Solution().maxEqualRowsAfterFlips(matrix))
matrix = [[0, 1], [1, 0]]
print(Solution().maxEqualRowsAfterFlips(matrix))
matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(Solution().maxEqualRowsAfterFlips(matrix))
