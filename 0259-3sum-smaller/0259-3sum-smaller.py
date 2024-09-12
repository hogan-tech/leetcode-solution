# time complexity: O(n^2)
# space completity: O(1)
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums) - 1):
            result += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return result

    def twoSumSmaller(self, nums: List[int], startIdx: int, target: int) -> int:
        left = startIdx
        right = len(nums) - 1
        result = 0
        while left < right:
            if nums[left] + nums[right] < target:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


nums = [-2, 0, 1, 3]
target = 2
print(Solution().threeSumSmaller(nums, target))
