# time complexity: O(n*n^0.5)
# space complexity: O(n)
import math


class Solution:
    def numSquares(self, n: int) -> int:
        squareNums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squareNums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[-1]


n = 13
print(Solution().numSquares(n))
