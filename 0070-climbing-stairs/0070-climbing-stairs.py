class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i: int, n: int, memo: list) -> int:
        if (i > n):
            return 0
        if (i == n):
            return 1
        if (memo[i]):
            return memo[i]
        memo[i] = self.climb_Stairs(i+1, n, memo) + \
            self.climb_Stairs(i+2, n, memo)
        return memo[i]