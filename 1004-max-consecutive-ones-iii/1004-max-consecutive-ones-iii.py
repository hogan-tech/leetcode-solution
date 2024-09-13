# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        result = 0
        ones = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ones += 1
            while left <= right and right - left + 1 - ones > k:
                if nums[left] == 1:
                    ones -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1
        return result


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(Solution().longestOnes(nums, k))
