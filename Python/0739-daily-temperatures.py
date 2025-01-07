# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                result[prevDay] = currDay - prevDay
            stack.append(currDay)
        return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
temperatures = [30, 40, 50, 60]
print(Solution().dailyTemperatures(temperatures))
temperatures = [30, 60, 90]
print(Solution().dailyTemperatures(temperatures))
