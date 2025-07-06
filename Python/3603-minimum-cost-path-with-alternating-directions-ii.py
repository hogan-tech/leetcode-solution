# time complexity: O(n*m)
# space complexity: O(n*M)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        heap = [(1, 0, 0, 1)]
        visited = {}
        visited[(0, 0, 1 % 2)] = 1
        ROW, COL = m, n

        while heap:
            currCost, r, c, time = heappop(heap)

            if r == ROW - 1 and c == COL - 1:
                return currCost

            if currCost > visited.get((r, c, time % 2), float('inf')):
                continue

            if time % 2 == 0:
                nextTime = time + 1
                nextCost = currCost + waitCost[r][c]
                key = (r, c, nextTime % 2)
                if nextCost < visited.get(key, float('inf')):
                    visited[key] = nextCost
                    heappush(heap, (nextCost, r, c, nextTime))
            else:
                for dR, dC in [(0, 1), (1, 0)]:
                    nextR, nextC = r + dR, c + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL:
                        nextTime = time + 1
                        entryCost = (nextR + 1) * (nextC + 1)
                        nextCost = currCost + entryCost
                        key = (nextR, nextC, nextTime % 2)
                        if nextCost < visited.get(key, float('inf')):
                            visited[key] = nextCost
                            heappush(heap, (nextCost, nextR, nextC, nextTime))
        return -1


m = 1
n = 2
waitCost = [[1, 2]]
print(Solution().minCost(m, n, waitCost))
m = 2
n = 2
waitCost = [[3, 5], [2, 4]]
print(Solution().minCost(m, n, waitCost))
m = 2
n = 3
waitCost = [[6, 1, 4], [3, 2, 5]]
print(Solution().minCost(m, n, waitCost))
