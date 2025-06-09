# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def traverse(r: int, c: int):
            count = 0
            queue = deque()
            queue.append((r, c))
            grid[r][c] = 0

            while queue:
                currR, currC = queue.popleft()
                count += 1

                for dR, dC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == 1:
                        grid[nextR][nextC] = 0
                        queue.append((nextR, nextC))

            return count

        result = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    result = max(result, traverse(r, c))

        return result


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))
grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))
