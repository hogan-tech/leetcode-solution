# time complexity: O(n*m)
# space complexity: O(n*m)
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        ROW = len(mat)
        COL = len(mat[0])
        prefixSumMat = [[0 for _ in range(COL)] for _ in range(ROW)]

        for r in range(0, ROW):
            temp = 0
            for c in range(0, COL):
                temp += mat[r][c]
                prefixSumMat[r][c] = temp
                if r > 0:
                    prefixSumMat[r][c] += prefixSumMat[r-1][c]

        result = [[0 for _ in range(COL)] for _ in range(ROW)]

        for r in range(ROW):
            for c in range(COL):

                minR, maxR = max(0, r-K), min(ROW-1, r+K)
                minC, maxC = max(0, c-K), min(COL-1, c+K)

                result[r][c] = prefixSumMat[maxR][maxC]

                if minR > 0:
                    result[r][c] -= prefixSumMat[minR-1][maxC]

                if minC > 0:
                    result[r][c] -= prefixSumMat[maxR][minC-1]

                if minC > 0 and minR > 0:
                    result[r][c] += prefixSumMat[minR-1][minC-1]

        return result


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
print(Solution().matrixBlockSum(mat, k))
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
print(Solution().matrixBlockSum(mat, k))
