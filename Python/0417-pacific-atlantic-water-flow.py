# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        if not ROW or not COL:
            return []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacificQueue = deque()
        atlanticQueue = deque()

        for i in range(ROW):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, COL - 1))

        for i in range(COL):
            pacificQueue.append((0, i))
            atlanticQueue.append((ROW - 1, i))

        def bfs(queue):
            reachable = set()
            while queue:
                currX, currY = queue.popleft()
                reachable.add((currX, currY))
                for (dX, dY) in directions:
                    nextX = currX + dX
                    nextY = currY + dY
                    if nextX < 0 or nextX >= ROW or nextY < 0 or nextY >= COL:
                        continue
                    if (nextX, nextY) in reachable:
                        continue
                    if heights[currX][currY] > heights[nextX][nextY]:
                        continue

                    queue.append((nextX, nextY))
            return reachable
        pacificSet = bfs(pacificQueue)
        atlanticSet = bfs(atlanticQueue)
        return list(pacificSet.intersection(atlanticSet))


heights = [[1, 1], [1, 1], [1, 1]]
print(Solution().pacificAtlantic(heights))
