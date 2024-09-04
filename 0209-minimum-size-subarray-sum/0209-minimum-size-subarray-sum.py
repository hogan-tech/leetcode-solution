# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tempSum = 0
        result = float('inf')
        left = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            while tempSum >= target:
                result = min(result, i - left + 1)
                tempSum -= nums[left]
                left += 1
        return result if result != float('inf') else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
