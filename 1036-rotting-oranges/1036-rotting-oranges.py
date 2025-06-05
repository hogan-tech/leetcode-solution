# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        freshCount = 0
        for nextR in range(ROW):
            for nextC in range(COL):
                if grid[nextR][nextC] == 2:
                    queue.append((nextR, nextC))
                if grid[nextR][nextC] == 1:
                    freshCount += 1
                    
        if freshCount == 0:
            return 0
        
        
        minutes = -1
        while queue:
            size = len(queue)
            while size > 0:
                currR, currC = queue.popleft()
                size -= 1
                for dR, dC in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == 1:
                        grid[nextR][nextC] = 2
                        freshCount -= 1
                        queue.append((nextR, nextC))
            minutes += 1
        
        if freshCount == 0:
            return minutes
        
        return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
