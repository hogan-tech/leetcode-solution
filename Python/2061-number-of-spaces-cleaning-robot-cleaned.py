# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        DIRECTIONS = (0, 1, 0, -1, 0)
        rows, cols = len(room), len(room[0])
        visited = [[0] * cols for _ in range(rows)]
        cleaned = 0

        queue = deque([(0, 0, 0)])
        while queue:
            row, col, direction = queue.popleft()

            if visited[row][col] == 0:
                cleaned += 1

            visited[row][col] |= 1 << direction

            for d in range(4):
                nextDir = (direction + d) % 4
                nextRow = row + DIRECTIONS[nextDir]
                nextCol = col + DIRECTIONS[nextDir + 1]

                if (
                    0 <= nextRow < len(room)
                    and 0 <= nextCol < len(room[0])
                    and room[nextRow][nextCol] == 0
                ):
                    if visited[nextRow][nextCol] >> nextDir & 1:
                        return cleaned
                    else:
                        queue.append((nextRow, nextCol, nextDir))
                        break

        return cleaned


room = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
print(Solution().numberOfCleanRooms(room))
