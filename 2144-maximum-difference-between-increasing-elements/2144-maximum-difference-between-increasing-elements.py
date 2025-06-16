# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] > 0:
                    result = max(result, nums[j] - nums[i])
        return result


nums = [7, 1, 5, 4]
print(Solution().maximumDifference(nums))
nums = [9, 4, 3, 2]
print(Solution().maximumDifference(nums))
nums = [1, 5, 2, 10]
print(Solution().maximumDifference(nums))
