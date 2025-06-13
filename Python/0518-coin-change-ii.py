# time complexity: O(n*m)
# space complexity: O(n*m)
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for coinIdx in range(n):
            dp[coinIdx][0] = 1

        for coinIdx in range(n - 1, -1, -1):
            for currAmount in range(1, amount + 1):
                if coins[coinIdx] > currAmount:
                    dp[coinIdx][currAmount] = dp[coinIdx + 1][currAmount]
                else:
                    dp[coinIdx][currAmount] = dp[coinIdx + 1][currAmount] + \
                        dp[coinIdx][currAmount - coins[coinIdx]]
        return dp[0][amount]


'''
  
   0  1  2  3  4  5  <- amountIdx
1 [1, 1, 2, 2, 3, 4]
2 [1, 0, 1, 0, 1, 1] 
5 [1, 0, 0, 0, 0, 1] 
  [0, 0, 0, 0, 0, 0]
'''

# time complexity: O(n*m)
# space complexity: O(n*m)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = dp(i + 1, amount)
            else:
                memo[i][amount] = dp(i + 1, amount) + \
                    dp(i, amount - coins[i])

            return memo[i][amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        return dp(0, amount)


'''
[-1, 1, 2, 2, 3, 4]
[-1, 0, 1, 0, 1, 1]
[-1, 0, 0, 0, 0, 1]
'''

amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))
amount = 3
coins = [2]
print(Solution().change(amount, coins))
amount = 10
coins = [10]
print(Solution().change(amount, coins))
