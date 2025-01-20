# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numRows, numCols = len(mat), len(mat[0])
        rowCount, colCount = [0] * numRows, [0] * numCols
        numToPos = {}

        for row in range(numRows):
            for col in range(numCols):
                numToPos[mat[row][col]] = [row, col]

        for i in range(len(arr)):
            num = arr[i]
            row, col = numToPos[num]

            rowCount[row] += 1
            colCount[col] += 1

            if rowCount[row] == numCols or colCount[col] == numRows:
                return i

        return -1


arr = [1, 3, 4, 2]
mat = [[1, 4], [2, 3]]
print(Solution().firstCompleteIndex(arr, mat))
arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
print(Solution().firstCompleteIndex(arr, mat))
