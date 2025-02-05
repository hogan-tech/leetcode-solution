# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        COL = len(words)
        ROW = 0
        for word in words:
            ROW = max(ROW, len(word))

        grid = [["" for _ in range(COL)] for _ in range(ROW)]

        for r in range(ROW):
            for c in range(COL):
                if r < len(words[c]):
                    grid[r][c] = words[c][r]
                else:
                    grid[r][c] = " "

            grid[r] = ''.join(grid[r]).rstrip()

        return grid


s = "HOW ARE YOU"
print(Solution().printVertically(s))
s = "TO BE OR NOT TO BE"
print(Solution().printVertically(s))
s = "CONTEST IS COMING"
print(Solution().printVertically(s))
