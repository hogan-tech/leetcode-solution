# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if coins[-1] == -1:
            return []
        n = len(coins)

        cost = [float('inf') for _ in range(n)]
        cost[-1] = 0

        queue = deque([n-1])
        for i in range(n-2, -1, -1):
            if coins[i] == -1:
                continue

            while queue and queue[0] > i + maxJump:
                queue.popleft()

            if not queue:
                return []

            cost[i] = coins[i] + cost[queue[0]]

            while queue and cost[queue[-1]] >= cost[i]:
                queue.pop()
            queue.append(i)
        minCost = cost[0]
        if minCost == float('inf'):
            return []

        result = []
        for i in range(n):
            if cost[i] == minCost:
                result.append(i+1)
                minCost -= coins[i]
        return result


coins = [1, 2, 4, -1, 2]
maxJump = 2
print(Solution().cheapestJump(coins, maxJump))
coins = [1, 2, 4, -1, 2]
maxJump = 1
print(Solution().cheapestJump(coins, maxJump))
