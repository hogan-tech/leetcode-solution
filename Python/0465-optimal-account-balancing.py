# time complexity: O((n-1)!)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(current: int, n: int, balance: List[int]):
            while current < n and not balance[current]:
                current += 1
            if current == n:
                return 0
            cost = float('inf')

            for next in range(current + 1, n):
                if balance[next] * balance[current]  < 0:
                    balance[next] += balance[current]
                    cost = min(cost, 1 + backtrack(current + 1, n, balance))
                    balance[next] -= balance[current]
            return cost

        balanceMap = defaultdict(int)
        for start, end, amount in transactions:
            balanceMap[start] -= amount
            balanceMap[end] += amount
        
        balance = [amount for amount in balanceMap.values() if amount]
        n = len(balance)
        

        return backtrack(0, n, balance)


transactions = [[0, 1, 10], [2, 0, 5]]
print(Solution().minTransfers(transactions))
transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
print(Solution().minTransfers(transactions))
transactions = [[0, 1, 10], [0, 2, 30], [1, 0, 20], [2, 0, 5]]
print(Solution().minTransfers(transactions))
