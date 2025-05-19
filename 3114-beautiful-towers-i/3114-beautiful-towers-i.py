# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        result = float('-inf')
        for i in range(len(heights)):
            tempHeights = list(heights)
            total = heights[i]
            for j in range(i - 1, -1, -1):
                tempHeights[j] = min(tempHeights[j + 1], tempHeights[j])
                total += tempHeights[j]
            for j in range(i + 1, len(heights)):
                tempHeights[j] = min(tempHeights[j - 1], tempHeights[j])
                total += tempHeights[j]
            result = max(result, total)
        return result


heights = [5, 3, 4, 1, 1]
print(Solution().maximumSumOfHeights(heights))
heights = [6, 5, 3, 9, 2, 7]
print(Solution().maximumSumOfHeights(heights))
heights = [3, 2, 5, 5, 2, 3]
print(Solution().maximumSumOfHeights(heights))
heights = [2, 4, 5, 2, 5, 5, 2, 1, 1, 3]
print(Solution().maximumSumOfHeights(heights))
heights = [5, 5, 3, 2, 6]
print(Solution().maximumSumOfHeights(heights))
