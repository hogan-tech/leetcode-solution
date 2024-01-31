# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                answer[prevDay] = currDay - prevDay
            stack.append(currDay)
        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
