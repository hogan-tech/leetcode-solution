# time complexity: O(n*s)
# space complexity: O(s)
from functools import lru_cache
from typing import List

# Bottom Up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1

# Top Down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(currAmount: int):
            if currAmount < 0:
                return -1
            if currAmount == 0:
                return 0
            minCost = float('inf')
            for coin in coins:
                result = dp(currAmount - coin)
                if result != -1:
                    minCost = min(minCost, result + 1)
            return minCost if minCost != float('inf') else -1
        return dp(amount)


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
coins = [2147483647]
amount = 2
print(Solution().coinChange(coins, amount))
