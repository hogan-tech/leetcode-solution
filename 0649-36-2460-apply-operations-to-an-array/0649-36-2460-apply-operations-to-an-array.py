# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        result = [num for num in nums if num != 0]

        result.extend(0 for _ in range(len(nums) - len(result)))

        return result


nums = [1, 2, 2, 1, 1, 0]
print(Solution().applyOperations(nums))
nums = [0, 1]
print(Solution().applyOperations(nums))
