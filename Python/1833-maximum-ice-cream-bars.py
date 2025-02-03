# time complexity: O(nlogn)
# space complexity: O(1)
from heapq import heapify, heappop
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        result = 0
        while costs or coins:
            currCost = heappop(costs)
            if currCost > coins:
                break
            else:
                coins -= currCost
                result += 1
            if len(costs) == 0:
                return result
        return result


costs = [1, 3, 2, 4, 1]
coins = 7
print(Solution().maxIceCream(costs, coins))
costs = [10, 6, 8, 7, 7, 8]
coins = 5
print(Solution().maxIceCream(costs, coins))
costs = [1, 6, 3, 1, 2, 5]
coins = 20
print(Solution().maxIceCream(costs, coins))
