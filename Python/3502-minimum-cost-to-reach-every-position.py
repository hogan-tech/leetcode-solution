# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        answer = [0] * n
        minCost = float('inf')

        for i in range(n):
            minCost = min(minCost, cost[i])
            answer[i] = minCost

        return answer


cost = [5, 3, 4, 1, 3, 2]
print(Solution().minCosts(cost))
cost = [1, 2, 4, 6, 7]
print(Solution().minCosts(cost))
