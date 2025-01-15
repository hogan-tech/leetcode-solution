# time complexity: O(mn)
# space complexity: O(mn)
from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '*':
                    queue.append((1, (r, c)))
                    visited.add((r, c))
        minDistance = float('inf')
        while queue:
            currDis, (currR, currC) = queue.popleft()

            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in visited:
                    if grid[nextR][nextC] != 'X' and grid[nextR][nextC] == 'O':
                        queue.append((currDis + 1, (nextR, nextC)))
                        visited.add((nextR, nextC))
                if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == '#':
                    minDistance = min(minDistance, currDis)
        return minDistance if minDistance != float('inf') else -1


grid = [["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"],
        ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]
print(Solution().getFood(grid))
grid = [["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"],
        ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]
print(Solution().getFood(grid))
grid = [["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O", "O",
                                                                                             "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]
print(Solution().getFood(grid))
