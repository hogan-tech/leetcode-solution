class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        def totalWays(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in memo:
                return memo[i]
            memo[i] = (k-1) * (totalWays(i-1) + totalWays(i-2))
            return memo[i]

        return totalWays(n)


n = 7
k = 2
print(Solution().numWays(n, k))
