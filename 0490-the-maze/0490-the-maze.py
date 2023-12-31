from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visit = [[False] * n for _ in range(m)]
        queue = deque()

        queue.append(start)
        visit[start[0]][start[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [1, 0, -1, 0]

        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            for i in range(4):
                r = curr[0]
                c = curr[1]
                while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                    r += dirX[i]
                    c += dirY[i]
                r -= dirX[i]
                c -= dirY[i]
                if not visit[r][c]:
                    queue.append([r, c])
                    visit[r][c] = True
        return False


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(Solution().hasPath(maze, start, destination))
