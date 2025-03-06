# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        n = len(grid)
        for i in range(1, n ** 2 + 1):
            freq[i] = 0

        for r in range(n):
            for c in range(n):
                freq[grid[r][c]] += 1

        result = [0, 0]
        for key, value in freq.items():
            if value == 0:
                result[1] = key
            if value == 2:
                result[0] = key
        return result


grid = [[1, 3], [2, 2]]
print(Solution().findMissingAndRepeatedValues(grid))
grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(Solution().findMissingAndRepeatedValues(grid))
