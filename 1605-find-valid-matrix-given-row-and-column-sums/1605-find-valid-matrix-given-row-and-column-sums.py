# time complexity: O(n*m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rowLen = len(rowSum)
        colLen = len(colSum)
        currRowSum = [0] * rowLen
        currColSum = [0] * colLen
        matrix = [[0] * colLen for _ in range(rowLen)]
        for i in range(rowLen):
            for j in range(colLen):
                matrix[i][j] = min(rowSum[i] - currRowSum[i],
                                   colSum[j] - currColSum[j])
                currRowSum[i] += matrix[i][j]
                currColSum[j] += matrix[i][j]
        return matrix

    def findSumMatrix(self, matrix: List[List[int]]) -> List[int]:
        rowSum = [sum(row) for row in matrix]
        colSum = [sum(col) for col in zip(*matrix)]
        return [rowSum, colSum]


rowSum = [3, 8]
colSum = [4, 7]

sumMatrix = [[3, 0],
             [1, 7]]
# print(Solution().findSumMatrix(sumMatrix))
print(Solution().restoreMatrix(rowSum, colSum))
