from collections import deque
from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        queue.append((-1, -1))
        minutes_elapsed = -1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes_elapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    neighbor_row = row + d[0]
                    neighbor_col = col + d[1]
                    if rows > neighbor_row >= 0 and cols > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))

        return minutes_elapsed if fresh_oranges == 0 else -1