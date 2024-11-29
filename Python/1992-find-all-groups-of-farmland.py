# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = set()
        Rows, Cols = len(land), len(land[0])
        result = []

        def dfs(x: int, y: int):
            stack = [(x, y)]
            minR, maxR, minC, maxC = x, x, y, y
            visited.add((x, y))

            while stack:
                curX, curY = stack.pop()
                for dX, dY in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nX, nY = curX + dX, curY + dY
                    if 0 <= nX < Rows and 0 <= nY < Cols and (nX, nY) not in visited and land[nX][nY] == 1:
                        visited.add((nX, nY))
                        stack.append((nX, nY))
                        minR = min(nX, minR)
                        minC = min(nY, minC)
                        maxR = max(nX, maxR)
                        maxC = max(nY, maxC)

            return (minR, maxR, minC, maxC)

        for i in range(Rows):
            for j in range(Cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    minR, maxR, minC, maxC = dfs(i, j)
                    result.append([minR, minC, maxR, maxC])
        return result


land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
print(Solution().findFarmland(land))
