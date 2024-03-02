from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2    
        return sorted(nums)


nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))
