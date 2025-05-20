# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniqueSet = set()
        left = 0
        result = 0
        currSum = 0
        for right in range(len(nums)):
            while nums[right] in uniqueSet:
                uniqueSet.remove(nums[left])
                currSum -= nums[left]
                left += 1
            currSum += nums[right]
            uniqueSet.add(nums[right])
            result = max(result, currSum)

        return result


nums = [4, 2, 4, 5, 6]
print(Solution().maximumUniqueSubarray(nums))
nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
print(Solution().maximumUniqueSubarray(nums))
