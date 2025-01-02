# time complexity: O(n^m) = O(9^9) = O(1)
# space complexity: O(9+9) = O(1)
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeros = []
        extras = []
        minMoves = float('inf')

        totalStones = sum(sum(row) for row in grid)
        if totalStones != 9:
            return -1
        
        def backtrack(i: int, count: int):
            if i >= len(zeros):
                nonlocal minMoves
                minMoves = min(minMoves, count)
                return
            for k in range(len(extras)):
                if extras[k][2] != 0:
                    extras[k][2] -= 1
                    distance = abs(extras[k][0] - zeros[i][0]) + abs(extras[k][1] - zeros[i][1])
                    backtrack(i + 1, distance + count)
                    extras[k][2] += 1
        
        for r in range(3):
            for c in range(3):
                if grid[r][c] == 0:
                    zeros.append([r, c])
                else:
                    extras.append([r, c, grid[r][c] - 1])
        if len(zeros) == 0:
            return 0
        
        backtrack(0, 0)
        return minMoves


grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]
print(Solution().minimumMoves(grid))
grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]
print(Solution().minimumMoves(grid))
