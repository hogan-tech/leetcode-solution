from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1,len(nums)):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index


nums = [1,1,2]
print(Solution().removeDuplicates(nums))
