# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import deque
from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        freshOranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        queue.append((-1, -1))
        minutesElapsed = -1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutesElapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    nextRow = row + d[0]
                    nextCol = col + d[1]
                    if rows > nextRow >= 0 and cols > nextCol >= 0:
                        if grid[nextRow][nextCol] == 1:
                            grid[nextRow][nextCol] = 2
                            freshOranges -= 1
                            queue.append((nextRow, nextCol))

        return minutesElapsed if freshOranges == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
