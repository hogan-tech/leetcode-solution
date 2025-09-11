# time complexity: O(m * n)
# space complexity: O(m * n)
from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROW = len(maze)
        COL = len(maze[0])
        visited = [[False for _ in range(COL)] for _ in range(ROW)]
        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = True
        while queue:
            currR, currC = queue.popleft()
            if [currR, currC] == destination:
                return True
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR
                nextC = currC
                while 0 <= nextR + dR < ROW and 0 <= nextC + dC < COL and maze[nextR + dR][nextC + dC] == 0:
                    nextR += dR
                    nextC += dC
                if not visited[nextR][nextC]:
                    queue.append([nextR, nextC])
                    visited[nextR][nextC] = True
        return False


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(Solution().hasPath(maze, start, destination))
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]
print(Solution().hasPath(maze, start, destination))
maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
    0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]
print(Solution().hasPath(maze, start, destination))
