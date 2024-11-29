class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * (n + 1)

        if n == 0:
            memo[0] = 0
            return 0
        if n == 1:
            memo[1] = 1
            return 1
        if memo[n]:
            return memo[n]
        else:
            memo[n] = self.fib(n-1) + self.fib(n-2)
            return memo[n]


print(Solution().fib(3))
