from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet = set(nums)
        target = original
        while target <= 1000:
            if target not in numSet:
                return target
            target *= 2
        return target


nums = [5, 3, 6, 1, 12]
original = 3
print(Solution().findFinalValue(nums, original))
nums = [2, 7, 9]
original = 4
print(Solution().findFinalValue(nums, original))
