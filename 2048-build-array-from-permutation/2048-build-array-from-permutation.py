# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result


nums = [0, 2, 1, 5, 3, 4]
print(Solution().buildArray(nums))
