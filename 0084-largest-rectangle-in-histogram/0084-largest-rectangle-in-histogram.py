# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monoStack = []
        maxArea = 0
        for i in range(len(heights)):
            while monoStack and heights[monoStack[-1]] >= heights[i]:
                currHeight = heights[monoStack.pop()]
                currWidth = i if not monoStack else i - monoStack[-1] - 1
                maxArea = max(maxArea, currHeight * currWidth)
            monoStack.append(i)
        
        n = len(heights)
        while monoStack:
            currHeight = heights[monoStack.pop()]
            currWidth = n if not monoStack else n - monoStack[-1] - 1
            maxArea = max(maxArea, currHeight * currWidth)
        return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
heights = [2,4]
print(Solution().largestRectangleArea(heights))