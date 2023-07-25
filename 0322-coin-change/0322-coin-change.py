from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(amount - coin)
                if res != -1:
                    min_cost = min(min_cost, res+1)
            return -1 if min_cost == float('inf') else min_cost

        return dfs(amount)
