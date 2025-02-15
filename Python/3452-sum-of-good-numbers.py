# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if i - k >= 0 and i + k <= len(nums) - 1:
                if nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                    count += nums[i]
            if i - k < 0:
                if nums[i] > nums[i + k]:
                    count += nums[i]
            if i + k > len(nums) - 1:
                if nums[i] > nums[i - k]:
                    count += nums[i]
        return count


'''
case 1:
    i - k >= 0 and i + k <= len(nums) - 1 and nums[i] > nums[i-k] and nums[i] > nums[i + k]
case 2:
    i - k < 0 and nums[i] > nums[i + k]
case 3:
    if i + k > len(nums) - 1 and nums[i] > nums[i - k]
    
'''


nums = [1, 3, 2, 1, 5, 4]
k = 2
print(Solution().sumOfGoodNumbers(nums, k))
nums = [2, 1]
k = 1
print(Solution().sumOfGoodNumbers(nums, k))
