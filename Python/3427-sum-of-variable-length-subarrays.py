# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            arr[i] = sum(nums[start: i + 1])
        return sum(arr)


nums = [2, 3, 1]
print(Solution().subarraySum(nums))
nums = [3, 1, 1, 2]
print(Solution().subarraySum(nums))
