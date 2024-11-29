from bisect import bisect_left
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        size = len(nums)
        if size < 2:
            return False
        minArray = [-1] * size
        minArray[0] = nums[0]
        for i in range(1, size):
            minArray[i] = min(minArray[i-1], nums[i])

        k = size
        for j in range(size-1, -1, -1):
            if nums[j] <= minArray[j]:
                continue
            k = bisect_left(nums, minArray[j] + 1, k, len(nums))
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False


nums = [-1, 3, 2, 0]
print(Solution().find132pattern(nums))
