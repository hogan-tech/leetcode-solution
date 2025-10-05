# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if i % 2:
                result -= nums[i]
            else:
                result += nums[i]
        return result


nums = [1, 3, 5, 7]
print(Solution().alternatingSum(nums))
nums = [100]
print(Solution().alternatingSum(nums))
