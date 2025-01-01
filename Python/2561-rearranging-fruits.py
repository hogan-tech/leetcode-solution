# time complexity: O((n+m)log(n+m))
# space complexity: O(n+m)
from collections import Counter
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        combined = basket1 + basket2
        combinedCounter = Counter(combined)
        for value in combinedCounter.values():
            if value % 2:
                return -1

        excess1 = []
        excess2 = []

        counter1 = Counter(basket1)
        counter2 = Counter(basket2)

        for fruit in combinedCounter:
            diff = counter1[fruit] - counter2[fruit]
            if diff > 0:
                excess1.extend([fruit] * (diff // 2))
            elif diff < 0:
                excess2.extend([fruit] * (-diff // 2))

        excess1.sort()
        excess2.sort(reverse=True)

        minFruitCost = min(combinedCounter.keys())

        totalCost = 0
        for i in range(len(excess1)):
            totalCost += min(2 * minFruitCost, excess1[i], excess2[i])

        return totalCost


basket1 = [4, 2, 2, 2]
basket2 = [1, 4, 1, 2]
print(Solution().minCost(basket1, basket2))
basket1 = [2, 3, 4, 1]
basket2 = [3, 2, 5, 1]
print(Solution().minCost(basket1, basket2))
