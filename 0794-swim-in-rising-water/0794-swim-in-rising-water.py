class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        visited.add((0, 0))
        pq = []
        pq.append((grid[0][0], 0, 0))
        while pq:
            currWeight, currR, currC = heappop(pq)
            if (currR, currC) == (ROW - 1, COL - 1):
                return currWeight
            for dR, dC in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in visited:
                    heappush(pq, (max(grid[nextR][nextC], currWeight), nextR, nextC))
                    visited.add((nextR, nextC))
        return 0


        