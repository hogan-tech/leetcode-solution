# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        low = i + 1
        hight = len(nums) - 1
        while (low < hight):
            sum = nums[i] + nums[low] + nums[hight]
            if sum < 0:
                low += 1
            elif sum > 0:
                hight -= 1
            else:
                result.append([nums[i], nums[low], nums[hight]])
                low += 1
                hight -= 1
                while low < hight and nums[low] == nums[low - 1]:
                    low += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, item in enumerate(nums):
            if item > 0:
                break
            if item != nums[i-1] or i == 0:
                self.twoSum(nums, i, result)

        return result
