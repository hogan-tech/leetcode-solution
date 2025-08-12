# time complexity: O(n * n (1/x))
# space complexity: O(n)
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = i**x
            if val > n:
                break
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]


n = 10
x = 2
print(Solution().numberOfWays(n, x))
n = 4
x = 1
print(Solution().numberOfWays(n, x))
