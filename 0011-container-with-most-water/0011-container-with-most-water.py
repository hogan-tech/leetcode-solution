from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSum = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxSum = max(maxSum, (right - left) *
                         min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxSum


Height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(Height))
