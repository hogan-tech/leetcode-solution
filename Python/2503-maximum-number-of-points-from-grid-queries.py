# time complexity: O(klogk + n*mlog(n*m))
# space complexity: O(n*m + k)
from typing import List
from queue import PriorityQueue


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROW, COL = len(grid), len(grid[0])
        result = [0] * len(queries)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        minHeap = PriorityQueue()
        visited = [[False] * COL for _ in range(ROW)]
        totalPoints = 0
        minHeap.put((grid[0][0], 0, 0))
        visited[0][0] = True

        for val, idx in queries:
            while not minHeap.empty() and minHeap.queue[0][0] < val:
                _, currR, currC = minHeap.get()

                totalPoints += 1

                for dR, dC in DIRECTIONS:
                    nextR, nextC = (
                        currR + dR,
                        currC + dC,
                    )

                    if (
                        nextR >= 0
                        and nextC >= 0
                        and nextR < ROW
                        and nextC < COL
                        and not visited[nextR][nextC]
                    ):
                        minHeap.put((grid[nextR][nextC], nextR, nextC))
                        visited[nextR][nextC] = True
            result[idx] = totalPoints

        return result


grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
print(Solution().maxPoints(grid, queries))
grid = [[5, 2, 1], [1, 1, 2]]
queries = [3]
print(Solution().maxPoints(grid, queries))
