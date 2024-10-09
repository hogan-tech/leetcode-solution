from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        seen = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "*":
                    queue.append((1, (i, j)))
                    seen.add((i, j))
                    break
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minDistance = float('inf')
        while queue:
            currDistance, (currR, currC) = queue.popleft()
            for dR, dC in directions:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] != "X" and grid[nextR][nextC] == "O" and (nextR, nextC) not in seen:
                    queue.append((currDistance + 1, (nextR, nextC)))
                    seen.add((nextR, nextC))
                if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == "#":
                    minDistance = min(minDistance, currDistance)

        if minDistance == float("inf"):
            return -1
        return minDistance


grid = [["O", "*"], ["#", "O"]]
print(Solution().getFood(grid))
