# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop
from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        maxPizzas = [-pizza for pizza in pizzas]
        heapify(maxPizzas)
        total = 0
        n = len(pizzas) // 4
        odd = n - n // 2
        even = n // 2
        for _ in range(odd):
            currPizza = -heappop(maxPizzas)
            total += currPizza
        for _ in range(even):
            heappop(maxPizzas)
            currPizza = -heappop(maxPizzas)
            total += currPizza

        return total


pizzas = [1, 2, 3, 4, 5, 6, 7, 8]
print(Solution().maxWeight(pizzas))
pizzas = [2, 1, 1, 1, 1, 1, 1, 1]
print(Solution().maxWeight(pizzas))
pizzas = [5, 2, 2, 4, 3, 3, 1, 3, 2, 5, 4, 2]
print(Solution().maxWeight(pizzas))  # 14
