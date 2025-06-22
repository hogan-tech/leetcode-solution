# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        coins = []

        def check(coinSet):
            dp = [0] * (n + 1)
            dp[0] = 1
            for coin in coinSet:
                for i in range(coin, n + 1):
                    dp[i] += dp[i - coin]
            return dp[1:] == numWays

        for coin in range(1, n + 1):
            testSet = coins + [coin]
            dp = [0] * (n + 1)
            dp[0] = 1
            for c in testSet:
                for i in range(c, n + 1):
                    dp[i] += dp[i - c]
            valid = True
            for i in range(1, n + 1):
                if dp[i] > numWays[i - 1]:
                    valid = False
                    break
            if valid:
                coins.append(coin)

        if check(coins):
            return coins
        return []


numWays = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
print(Solution().findCoins(numWays))
numWays = [1, 2, 2, 3, 4]
print(Solution().findCoins(numWays))
numWays = [1, 2, 3, 4, 15]
print(Solution().findCoins(numWays))
