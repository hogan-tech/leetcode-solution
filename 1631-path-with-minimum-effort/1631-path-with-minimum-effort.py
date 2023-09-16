from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])

        def canReachDestination(mid: int):
            visited = [[False]*col for _ in range(row)]
            queue = [(0, 0)]
            while queue:
                x, y = queue.pop(0)
                if x == row - 1 and y == col - 1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    adjacentX, adjacentY = x+dx, y+dy
                    if 0 <= adjacentX < row and 0 <= adjacentY < col and not visited[adjacentX][adjacentY]:
                        currentDifference = abs(heights[adjacentX][adjacentY] - heights[x][y])
                        if currentDifference <= mid:
                            visited[adjacentX][adjacentY] = True
                            queue.append((adjacentX, adjacentY))

        left, right = 0, 10000000
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1
        return left


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

print(Solution().minimumEffortPath(heights))
