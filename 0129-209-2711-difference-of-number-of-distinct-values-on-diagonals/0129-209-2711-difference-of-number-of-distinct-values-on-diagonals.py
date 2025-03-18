# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        ROW = len(grid)
        COL = len(grid[0])
        diagonalMap = defaultdict(list)
        for r in range(ROW):
            for c in range(COL):
                diagonalMap[r-c].append(grid[r][c])

        for key, arr in diagonalMap.items():
            for i in range(len(arr)):
                if key < 0:
                    r = i
                    c = i - key
                elif key > 0:
                    r = i + key
                    c = i
                else:
                    r = i
                    c = i
                leftArrSetLen = len(set(arr[:i]))
                rightArrSetLen = len(set(arr[i + 1:]))
                grid[r][c] = abs(leftArrSetLen - rightArrSetLen)

        return grid


''' 
    0  1  2
 0 00 11 22
-1 01 12
-2 02
 1 10 21
 2 20

00 01 02 
10 11 12
20 21 22

 1  2  3
 3  1  5
 3  2  1
'''
grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
print(Solution().differenceOfDistinctValues(grid))
grid = [[1]]
print(Solution().differenceOfDistinctValues(grid))
