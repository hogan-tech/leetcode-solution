# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        rightMax = [0] * n
        rightMax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])
        maxRamp = 0
        print(rightMax)
        while right < n:
            while left < right and nums[left] > rightMax[right]:
                left += 1
            maxRamp = max(maxRamp, right - left)
            right += 1
        return maxRamp


nums = [6, 0, 8, 2, 1, 5]
print(Solution().maxWidthRamp(nums))
