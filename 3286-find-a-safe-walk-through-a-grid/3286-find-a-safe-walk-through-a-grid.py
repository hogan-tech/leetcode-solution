# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if grid[0][0] == 1:
            health -= 1

        queue = deque([(0, 0, health)])

        visited = set((0, 0, health))
        while queue:
            x, y, curHealth = queue.popleft()
            if (x, y) == (rows - 1, cols - 1) and curHealth >= 1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    newHealth = curHealth - grid[nx][ny]

                    if newHealth > 0 and (nx, ny, newHealth) not in visited:
                        visited.add((nx, ny, newHealth))
                        queue.append((nx, ny, newHealth))

        return False


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
health = 5
print(Solution().findSafeWalk(grid, health))
