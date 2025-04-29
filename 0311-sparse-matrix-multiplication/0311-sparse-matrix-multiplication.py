# time complexity: O(n^3)
# space complexity: O(n^2)
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ROW = len(mat1)
        COL = len(mat2[0])
        result = [[0 for _ in range(COL)] for _ in range(ROW)]

        mat2R = len(mat2)
        for r in range(ROW):
            for c in range(COL):
                result[r][c] = sum(mat1[r][i] * mat2[i][c]
                                   for i in range(mat2R))

        return result


'''


r c    ri * jc
0 0 -> 00 * 00 + 01 * 10 + 02*20
0 1 -> 00 * 01 + 01 * 11 + 02*21

1 0 -> 10 * 00 + 11 * 10 + 12*20


'''
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(Solution().multiply(mat1, mat2))
mat1 = [[0]]
mat2 = [[0]]
print(Solution().multiply(mat1, mat2))
mat1 = [[1, -5]]
mat2 = [[12], [-1]]
print(Solution().multiply(mat1, mat2))
