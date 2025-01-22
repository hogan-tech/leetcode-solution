# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW = len(isWater)
        COL = len(isWater[0])
        cellHeights = [[-1 for _ in range(COL)] for _ in range(ROW)]
        queue = deque()
        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    cellHeights[r][c] = 0

        nextLevel = 1
        while queue:
            layerSize = len(queue)
            for _ in range(layerSize):
                currR, currC = queue.popleft()
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and cellHeights[nextR][nextC] == -1:
                        cellHeights[nextR][nextC] = nextLevel
                        queue.append((nextR, nextC))
            nextLevel += 1
        return cellHeights


isWater = [[0, 1], [0, 0]]
print(Solution().highestPeak(isWater))
isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(Solution().highestPeak(isWater))
