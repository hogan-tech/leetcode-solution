# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])
        rLargestMin = float('-inf')
        for r in range(ROW):
            rMin = min(matrix[r])
            rLargestMin = max(rLargestMin, rMin)
        cSmallestMax = float('inf')
        for c in range(COL):
            cMax = max(matrix[r][c] for r in range(ROW))
            cSmallestMax = min(cSmallestMax, cMax)
        
        if rLargestMin == cSmallestMax:
            return [rLargestMin]
        
        return []


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(Solution().luckyNumbers(matrix))
matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(Solution().luckyNumbers(matrix))
matrix = [[7, 8], [1, 2]]
print(Solution().luckyNumbers(matrix))
