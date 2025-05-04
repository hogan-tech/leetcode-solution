# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def build(num):
            if num == 0:
                return [[0]]
            ROW = COL = 2 ** (num - 1)
            prevMatrix = build(num - 1)
            curr = [[0 for _ in range(2 * COL)] for _ in range(2 * ROW)]
            for r in range(ROW):
                for c in range(COL):
                    val = prevMatrix[r][c]
                    curr[r][c + COL] = val + 0 * ROW * COL
                    curr[r + ROW][c + COL] = val + 1 * ROW * COL
                    curr[r + ROW][c] = val + 2 * ROW * COL
                    curr[r][c] = val + 3 * ROW * COL
            return curr

        return build(N)


N = 0
print(Solution().specialGrid((N)))
N = 1
print(Solution().specialGrid((N)))
N = 2
print(Solution().specialGrid((N)))
