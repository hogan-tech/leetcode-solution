from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        R = len(rooms)
        C = len(rooms[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    queue.append((1, (i, j)))

        while queue:
            distance, (currR, currC) = queue.popleft()
            for (dR, dC) in directions:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < R and 0 <= nextC < C and rooms[nextR][nextC] == INF:
                    rooms[nextR][nextC] = distance
                    queue.append((distance + 1, (nextR, nextC)))


rooms = [[2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]
print(Solution().wallsAndGates(rooms))
