from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        xLine = []
        yLine = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xLine.append(i)
                    yLine.append(j)

        xLine = sorted(xLine)
        yLine = sorted(yLine)

        medianX = xLine[len(xLine) // 2]
        medianY = yLine[len(yLine) // 2]

        travelX = [abs(medianX - x) for x in xLine]
        travelY = [abs(medianY - y) for y in yLine]
        return sum(travelX) + sum(travelY)


grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print(Solution().minTotalDistance(grid))
