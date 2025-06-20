# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                currentHeight = heights[stack.pop()]
                currentWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currentHeight * currentWidth)
            stack.append(i)

        while stack[-1] != -1:
            currentHeight = heights[stack.pop()]
            currentWidth = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, currentHeight * currentWidth)

        return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
heights = [2,4]
print(Solution().largestRectangleArea(heights))