# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        numsSum = sum(nums)
        total = sum([i*nums[i] for i in range(n)])
        result = total
        for idx in range(len(nums)-1, -1, -1):
            total = total + numsSum - (nums[idx] * n)
            result = max(result, total)
        return result


nums = [4, 3, 2, 6]
print(Solution().maxRotateFunction(nums))
nums = [100]
print(Solution().maxRotateFunction(nums))
