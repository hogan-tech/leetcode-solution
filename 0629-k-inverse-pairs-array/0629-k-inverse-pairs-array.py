# time complexity: O(nk)
# space complexity: O(nk)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        M = 1000000007
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] + M - (dp[i - 1]
                           [j - i] if j - i >= 0 else 0)) % M
                    dp[i][j] = (dp[i][j - 1] + val) % M

        return (dp[n][k] + M - (dp[n][k - 1] if k > 0 else 0)) % M


n = 3
k = 0
print(Solution().kInversePairs(n, k))
