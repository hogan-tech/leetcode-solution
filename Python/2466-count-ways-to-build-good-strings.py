# time complexity: O(high)
# space complexity: O(high)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        MOD = 10**9 + 7
        dp[0] = 1
        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] % MOD
        return sum(dp[low:high+1]) % MOD


low = 3
high = 3
zero = 1
one = 1
print(Solution().countGoodStrings(low, high, zero, one))
low = 2
high = 3
zero = 1
one = 2
print(Solution().countGoodStrings(low, high, zero, one))
