# time complexity: O(m*n)
# space complexity: O(max(m,n))
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        startRow, startCol = entrance
        maze[startRow][startCol] = "+"
        queue = deque()
        queue.append([startRow, startCol, 0])
        while queue:
            curRow, curCol, curDistance = queue.popleft()
            for d in dirs:
                nextRow = curRow + d[0]
                nextCol = curCol + d[1]
                if 0 <= nextRow < rows and 0 <= nextCol < cols and maze[nextRow][nextCol] == '.':
                    if nextRow == 0 or nextRow == rows - 1 or nextCol == 0 or nextCol == cols - 1:
                        return curDistance + 1
                    maze[nextRow][nextCol] = "+"
                    queue.append([nextRow, nextCol, curDistance + 1])
        return -1


maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]
print(Solution().nearestExit(maze, entrance))
