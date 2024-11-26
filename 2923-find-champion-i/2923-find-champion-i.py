from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        championPoint = 0
        champion = 0
        for i, row in enumerate(grid):
            if championPoint < sum(row):
                championPoint = sum(row)
                champion = i
        return champion


grid = [[0, 1], [0, 0]]
print(Solution().findChampion(grid))
grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
print(Solution().findChampion(grid))
