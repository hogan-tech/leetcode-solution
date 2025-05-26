# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonalList = defaultdict(list)
        ROW = len(mat)
        COL = len(mat[0])
        for r in range(ROW):
            for c in range(COL):
                diagonalList[r - c].append(mat[r][c])
        for key in diagonalList.keys():
            diagonalList[key].sort()
        for r in range(ROW):
            for c in range(COL):
                mat[r][c] = diagonalList[r-c].pop(0)
        return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(Solution().diagonalSort(mat))
mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [
    75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
print(Solution().diagonalSort(mat))
