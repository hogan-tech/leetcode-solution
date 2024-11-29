from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                currLevelCnt = len(queue)
                # iterate through the current level
                for i in range(currLevelCnt):
                    currX, currY = queue.popleft()
                    if (currX, currY) == (x, y):
                        return steps

                    for offsetX, offsetY in offsets:
                        nextX, nextY = currX + offsetX, currY + offsetY
                        if (nextX, nextY) not in visited:
                            visited.add((nextX, nextY))
                            queue.append((nextX, nextY))

                # move on to the next level
                steps += 1

        return bfs(x, y)
