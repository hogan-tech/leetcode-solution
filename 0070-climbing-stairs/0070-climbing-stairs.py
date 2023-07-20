class Solution:
# Cashe with brute force
    # def climbStairs(self, n: int) -> int:
    #     memo = [0] * (n+1)
    #     return self.climb_Stairs(0, n, memo)

    # def climb_Stairs(self, i: int, n: int, memo: list) -> int:
    #     if (i > n):
    #         return 0
    #     if (i == n):
    #         return 1
    #     if (memo[i]):
    #         return memo[i]
    #     memo[i] = self.climb_Stairs(i+1, n, memo) + \
    #         self.climb_Stairs(i+2, n, memo)
    #     return memo[i]

    # Dynamic Programming
    # def climbStairs(self, n: int):
    #     if n == 1:
    #         return 1
    #     dp = [0] * (n + 1)
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

    # Fibonacci Number
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        third = 0
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second