class Solution:
    def countOrders(self, n: int) -> int:
        Mod = 1_000_000_007
        dp = [[0] * (n+1) for i in range(n+1)]

        for unpicked in range(n+1):
            for undelivered in range(unpicked, n+1):
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue

                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * \
                        dp[unpicked-1][undelivered]
                dp[unpicked][undelivered] %= Mod

                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered -
                                                  unpicked) * dp[unpicked][undelivered-1]
                dp[unpicked][undelivered] %= Mod
        return dp[n][n]


print(Solution().countOrders(3))
