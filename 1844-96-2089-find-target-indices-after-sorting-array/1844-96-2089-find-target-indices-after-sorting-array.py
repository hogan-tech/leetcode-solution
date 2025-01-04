# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result


nums = [1, 2, 5, 2, 3]
target = 2
print(Solution().targetIndices(nums, target))
nums = [1, 2, 5, 2, 3]
target = 3
print(Solution().targetIndices(nums, target))
nums = [1, 2, 5, 2, 3]
target = 5
print(Solution().targetIndices(nums, target))
