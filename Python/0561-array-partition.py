from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i+1])
        return result


nums = [1, 4, 3, 2]


print(Solution().arrayPairSum(nums))
