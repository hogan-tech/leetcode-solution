# time complexity: O(n^2logn)
# space complexity: O(n^2)
from collections import deque
from typing import List


class Solution:

    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        multiSourceQueue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    multiSourceQueue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        while multiSourceQueue:
            size = len(multiSourceQueue)
            while size > 0:
                curr = multiSourceQueue.popleft()
                for d in self.dir:
                    di, dj = curr[0] + d[0], curr[1] + d[1]
                    val = grid[curr[0]][curr[1]]
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        multiSourceQueue.append((di, dj))
                size -= 1
        start, end, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                end = max(end, grid[i][j])
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValidSafeness(grid, mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res

    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

    def isValidSafeness(self, grid, minSafeness) -> bool:
        n = len(grid)
        if grid[0][0] < minSafeness or grid[n - 1][n - 1] < minSafeness:
            return False
        traversalQueue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        while traversalQueue:
            curr = traversalQueue.popleft()
            if curr[0] == n - 1 and curr[1] == n - 1:
                return True
            for d in self.dir:
                di, dj = curr[0] + d[0], curr[1] + d[1]
                if self.isValidCell(grid, di, dj) and not visited[di][dj] and grid[di][dj] >= minSafeness:
                    visited[di][dj] = True
                    traversalQueue.append((di, dj))
        return False


grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
print(Solution().maximumSafenessFactor(grid))
