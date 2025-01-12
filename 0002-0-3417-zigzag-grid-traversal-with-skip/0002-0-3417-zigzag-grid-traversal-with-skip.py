# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        flattenNum = []
        for i, row in enumerate(grid):
            if i % 2:
                flattenNum.extend(row[::-1])
            else:
                flattenNum.extend(row)
        result = []
        for i, num in enumerate(flattenNum):
            if i % 2 == 0:
                result.append(num)
        return result


grid = [[1, 2], [3, 4]]
print(Solution().zigzagTraversal(grid))
grid = [[2, 1], [2, 1], [2, 1]]
print(Solution().zigzagTraversal(grid))
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().zigzagTraversal(grid))
