# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ROW = len(coins)
        COL = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(COL + 1)]
              for _ in range(ROW + 1)]

        dp[ROW][COL - 1] = [0, 0, 0]
        dp[ROW - 1][COL] = [0, 0, 0]

        for r in range(ROW - 1, -1, -1):
            for c in range(COL - 1, -1, -1):
                for k in range(3):
                    if k > 0:
                        dp[r][c][k] = max(dp[r][c][k], dp[r][c][k-1])
                        dp[r][c][k] = max(dp[r][c][k], dp[r+1]
                                          [c][k-1], dp[r][c+1][k-1])
                    dp[r][c][k] = max(dp[r][c][k], coins[r]
                                      [c] + max(dp[r+1][c][k], dp[r][c+1][k]))
        return dp[0][0][2]


coins = [[0, 1, -1], [1, -2, 3], [2, -3, 4]]
print(Solution().maximumAmount(coins))
coins = [[10, 10, 10], [10, 10, 10]]
print(Solution().maximumAmount(coins))
coins = [[-4]]
print(Solution().maximumAmount(coins))
coins = [[-7, 12, 12, 13], [-6, 19, 19, -6],
         [9, -2, -10, 16], [-4, 14, -10, -9]]
print(Solution().maximumAmount(coins))  # 60
