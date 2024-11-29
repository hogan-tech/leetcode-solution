# time complexity: O(row * col * maxMove)
# space complexity: O(row * col * maxMove)
class Solution:
    def findPaths(self, row: int, col: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1000000007
        memo = [[[-1 for _ in range(maxMove + 1)]
                 for _ in range(col)] for _ in range(row)]

        def dp(row, col, maxMove, i, j):
            if i == row or j == col or i < 0 or j < 0:
                return 1
            if maxMove == 0:
                return 0
            if memo[i][j][maxMove] >= 0:
                return memo[i][j][maxMove]

            memo[i][j][maxMove] = (
                (dp(row, col, maxMove - 1, i - 1, j) + dp(row, col, maxMove - 1, i + 1, j)) % MOD +
                (dp(row, col, maxMove - 1, i, j - 1) +
                 dp(row, col, maxMove - 1, i, j + 1)) % MOD
            ) % MOD

            return memo[i][j][maxMove]

        return dp(row, col, maxMove, startRow, startColumn)


m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

print(Solution().findPaths(m, n, maxMove, startRow, startColumn))
