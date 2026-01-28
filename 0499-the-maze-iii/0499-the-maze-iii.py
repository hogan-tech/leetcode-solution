# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == 0

        def getNeighbors(row, col):
            directions = [(0, -1, 'l'), (-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd')]
            neighbors = []

            for dy, dx, direction in directions:
                currRow = row
                currCol = col
                dist = 0

                while valid(currRow + dy, currCol + dx):
                    currRow += dy
                    currCol += dx
                    dist += 1
                    if [currRow, currCol] == hole:
                        break

                neighbors.append((currRow, currCol, dist, direction))

            return neighbors

        m = len(maze)
        n = len(maze[0])
        heap = [(0, "", ball[0], ball[1])]
        seen = set()

        while heap:
            curr_dist, path, row, col = heappop(heap)

            if (row, col) in seen:
                continue

            if [row, col] == hole:
                return path

            seen.add((row, col))

            for next_row, next_col, dist, direction in getNeighbors(row, col):
                heappush(heap, (curr_dist + dist, path +
                         direction, next_row, next_col))

        return "impossible"


maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
    0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [0, 1]
print(Solution().findShortestWay(maze, ball, hole))
maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
    0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [3, 0]
print(Solution().findShortestWay(maze, ball, hole))
maze = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]]
ball = [0, 4]
hole = [3, 5]
print(Solution().findShortestWay(maze, ball, hole))
