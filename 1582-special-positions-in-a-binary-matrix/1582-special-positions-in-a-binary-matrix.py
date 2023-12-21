# time complexity: O(m+n)
# space complexity: O(m+n)
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowCount = [0] * len(mat)
        colCount = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rowCount[i] += mat[i][j]
                colCount[j] += mat[i][j]

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if rowCount[i] == 1 and colCount[j] == 1:
                        ans += 1

        return ans


mat = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [
    0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().numSpecial(mat))
