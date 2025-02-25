# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW = len(mat)
        COL = len(mat[0])
        diagonalDict = defaultdict(list)
        for r in range(ROW):
            for c in range(COL):
                diagonalDict[r + c].append(mat[r][c])

        result = []
        for key, nums in diagonalDict.items():
            if key % 2 == 0:
                result.extend(nums[::-1])
            else:
                result.extend(nums)
        return result


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(mat))
mat = [[1, 2], [3, 4]]
print(Solution().findDiagonalOrder(mat))


'''
00 01 02
10 11 12
20 21 22

x + y = 0
x + y = 1
x + y = 2
'''
