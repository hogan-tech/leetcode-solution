# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        currMaxTime = 0
        for i in range(len(neededTime)):
            if i > 0 and colors[i] != colors[i-1]:
                currMaxTime = 0

            totalTime += min(currMaxTime, neededTime[i])
            currMaxTime = max(currMaxTime, neededTime[i])
        return totalTime


colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
print(Solution().minCost(colors, neededTime))
