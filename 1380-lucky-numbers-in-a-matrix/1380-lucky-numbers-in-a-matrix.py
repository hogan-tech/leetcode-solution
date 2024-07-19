# time complexity: O(n*m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rowMin = {min(row) for row in matrix}
        colMax = {max(col) for col in zip(*matrix)}

        return list(rowMin & colMax)


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(Solution().luckyNumbers(matrix))
