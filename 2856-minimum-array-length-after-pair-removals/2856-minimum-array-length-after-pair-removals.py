# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        count = len(nums)
        left = 0
        right = (len(nums) + 1)//2
        while left < len(nums) // 2 and right < len(nums):
            if nums[right] > nums[left]:
                count -= 2
            left += 1
            right += 1

        return count


nums = [1, 2, 3, 4]
print(Solution().minLengthAfterRemovals(nums))
