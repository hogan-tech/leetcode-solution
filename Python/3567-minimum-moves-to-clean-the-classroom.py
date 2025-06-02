# time complexity: O(r*c)
# space complexity: O(r*c)
from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        ROW = len(classroom)
        COL = len(classroom[0])

        litterPos = {}
        startR = startC = -1
        litterCount = 0

        for currR in range(ROW):
            for currC in range(COL):
                cell = classroom[currR][currC]
                if cell == 'S':
                    startR, startC = currR, currC
                elif cell == 'L':
                    litterPos[(currR, currC)] = litterCount
                    litterCount += 1

        if litterCount == 0:
            return 0

        MASK = (1 << litterCount) - 1

        visited = [[[-1] * (1 << litterCount)
                    for _ in range(COL)]for _ in range(ROW)]

        queue = deque()
        startMask = 0
        startEnergy = energy
        visited[startR][startC][startMask] = startEnergy
        queue.append((startR, startC, startMask, startEnergy, 0))

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            currR, currC, currMask, currLeft, currDist = queue.popleft()

            if currMask == MASK:
                return currDist

            if currLeft <= 0:
                continue

            for dR, dC in DIRS:
                nextR, nextC = currR + dR, currC + dC
                if not (0 <= nextR < ROW and 0 <= nextC < COL):
                    continue
                cell = classroom[nextR][nextC]
                if cell == 'X':
                    continue

                nextNnergy = currLeft - 1

                if cell == 'R':
                    nextNnergy = energy

                nextMask = currMask
                if cell == 'L':
                    idx = litterPos[(nextR, nextC)]
                    nextMask = currMask | (1 << idx)

                if nextNnergy <= visited[nextR][nextC][nextMask]:
                    continue

                visited[nextR][nextC][nextMask] = nextNnergy
                queue.append(
                    (nextR, nextC, nextMask, nextNnergy, currDist + 1))

        return -1


classroom = ["S.", "XL"]
energy = 2
print(Solution().minMoves(classroom, energy))
classroom = ["LS", "RL"]
energy = 4
print(Solution().minMoves(classroom, energy))
classroom = ["L.S", "RXL"]
energy = 3
print(Solution().minMoves(classroom, energy))
