# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import deque
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [-1, 0, 1]
        queue = deque()
        seen = set()
        for i in range(ROW):
            queue.append(((i, 0), 0))
        seen.add((0, 0))
        result = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                (currR, currC), currVal = queue.popleft()
                result = max(result, currVal)
                for dir in dirs:
                    nextR = currR + dir
                    nextC = currC + 1
                    if (0 <= nextR < ROW
                        and 0 <= nextC < COL
                        and grid[currR][currC] < grid[nextR][nextC]
                            and (nextR, nextC) not in seen):
                        queue.append(((nextR, nextC), currVal + 1))
                        seen.add((nextR, nextC))
        return result


grid = [[2, 4, 3, 5],
        [5, 4, 9, 3],
        [3, 4, 2, 11],
        [10, 9, 13, 15]]
print(Solution().maxMoves(grid))
