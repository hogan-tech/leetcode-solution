from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        MaxSum = 0
        while left < right:
            MaxSum = max(MaxSum, (right - left) *
                         min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return MaxSum