# time complexity: O(mn)
# space complexity: O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW = m
        COL = n
        dp = [[1 for _ in range(COL)] for _ in range(ROW)]
        for r in range(1, ROW):
            for c in range(1, COL):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]

'''
1 1 1
1 2 3
1 3 6

'''