# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 0
        decreasing = 0
        result = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                increasing += 1
                decreasing = 0
            elif nums[i - 1] < nums[i]:
                increasing = 0
                decreasing += 1
            else:
                increasing = 0
                decreasing = 0
            result = max(result, increasing, decreasing)
        return result + 1


nums = [1, 4, 3, 3, 2]
print(Solution().longestMonotonicSubarray(nums))
nums = [3, 3, 3, 3]
print(Solution().longestMonotonicSubarray(nums))
nums = [3, 2, 1]
print(Solution().longestMonotonicSubarray(nums))
nums = [1, 1, 5]
print(Solution().longestMonotonicSubarray(nums))
