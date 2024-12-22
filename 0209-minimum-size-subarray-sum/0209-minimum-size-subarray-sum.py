# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tempSum = 0
        left = 0
        windowSize = float('inf')
        for right in range(len(nums)):
            tempSum += nums[right]
            while tempSum >= target:
                windowSize = min(right - left +1, windowSize)
                tempSum -= nums[left]
                left +=1
        return windowSize if windowSize != float('inf') else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
