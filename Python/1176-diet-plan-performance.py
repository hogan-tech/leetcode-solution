# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        performance = 0
        currSum = 0
        for i in range(k):
            currSum += calories[i]

        if currSum < lower:
            performance -= 1
        if currSum > upper:
            performance += 1

        for i in range(k, len(calories)):
            currSum += calories[i]
            currSum -= calories[i - k]
            if currSum < lower:
                performance -= 1
            if currSum > upper:
                performance += 1

        return performance


calories = [1, 2, 3, 4, 5]
k = 1
lower = 3
upper = 3
print(Solution().dietPlanPerformance(calories, k, lower, upper))
calories = [3, 2]
k = 2
lower = 0
upper = 1
print(Solution().dietPlanPerformance(calories, k, lower, upper))
calories = [6, 5, 0, 0]
k = 2
lower = 1
upper = 5
print(Solution().dietPlanPerformance(calories, k, lower, upper))
