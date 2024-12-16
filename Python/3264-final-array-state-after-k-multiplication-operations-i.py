# time complexity: O(n*k)
# space complexity: O(1)
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            currMin = min(nums)
            for i in range(len(nums)):
                if nums[i] == currMin:
                    nums[i] *= multiplier
                    break
        return nums


nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
print(Solution().getFinalState(nums, k, multiplier))
nums = [1, 2]
k = 3
multiplier = 4
print(Solution().getFinalState(nums, k, multiplier))
