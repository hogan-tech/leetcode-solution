# time complexity: O(r^2 * c^2)
# space complexity: O(r*c)
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        ROW = len(grid)
        COL = len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)

        hit = [[0] * COL for _ in range(ROW)]
        dist = [[0] * COL for _ in range(ROW)]

        def BFS(startR, startC):
            visited = [[False] * COL for _ in range(ROW)]
            visited[startR][startC] = True
            count = 1
            queue = deque([(startR, startC, 0)])
            while queue:
                currR, currC, currDist = queue.popleft()
                for dR, dC in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and not visited[nextR][nextC]:
                        visited[nextR][nextC] = True
                        if not grid[nextR][nextC]:
                            queue.append((nextR, nextC, currDist + 1))
                            hit[nextR][nextC] += 1
                            dist[nextR][nextC] += currDist + 1
                        elif grid[nextR][nextC] == 1:
                            count += 1
            return count == buildings

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    if not BFS(r, c):
                        return -1

        return min([dist[r][c] for r in range(ROW) for c in range(COL) if not grid[r][c] and hit[r][c] == buildings] or [-1])


grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print(Solution().shortestDistance(grid))
grid = [[1, 0]]
print(Solution().shortestDistance(grid))
grid = [[1]]
print(Solution().shortestDistance(grid))
