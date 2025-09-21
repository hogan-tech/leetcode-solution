# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = -1
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum < k:
                result = max(result, currSum)
                left += 1
            else:
                right -= 1
        return result


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(Solution().twoSumLessThanK(nums, k))
nums = [10, 20, 30]
k = 15
print(Solution().twoSumLessThanK(nums, k))
