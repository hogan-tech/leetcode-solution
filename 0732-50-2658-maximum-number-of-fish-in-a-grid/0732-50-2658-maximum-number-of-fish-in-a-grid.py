# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        def bfs(queue: deque, visited: List[List[int]], row: int, col: int):
            queue.append((row, col))
            visited[row][col] = True
            total = 0
            while queue:
                currR, currC = queue.popleft()
                total += grid[currR][currC]
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and not visited[nextR][nextC] and grid[nextR][nextC]:
                        visited[nextR][nextC] = True
                        queue.append((nextR, nextC))
            return total
        result = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] and not visited[r][c]:
                    result = max(result, bfs(queue, visited, r, c))
        return result


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
print(Solution().findMaxFish(grid))
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
print(Solution().findMaxFish(grid))
