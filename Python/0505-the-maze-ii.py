# time complexity: O(m*n*log(m*n))
# space complexity: O(m*n)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ROW = len(maze)
        COL = len(maze[0])
        visited = defaultdict(lambda: float('inf'))
        minHp = [(0, start[0], start[1])]
        visited[(start[0], start[1])] = 0
        while minHp:
            currDist, currR, currC = heappop(minHp)
            if [currR, currC] == destination:
                return currDist
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR
                nextC = currC
                nextDist = currDist
                while 0 <= nextR + dR < ROW and 0 <= nextC + dC < COL and maze[nextR + dR][nextC + dC] == 0:
                    nextR += dR
                    nextC += dC
                    nextDist += 1
                if nextDist < visited[(nextR, nextC)]:
                    heappush(minHp, (nextDist, nextR, nextC))
                    visited[(nextR, nextC)] = nextDist
        return -1


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(Solution().shortestDistance(maze, start, destination))
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]
print(Solution().shortestDistance(maze, start, destination))
maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
    0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]
print(Solution().shortestDistance(maze, start, destination))
