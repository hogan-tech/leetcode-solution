from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        minVal = min(nums)
        return k * (maxVal - minVal)


nums = [1,3,2]
k = 2
print(Solution().maxTotalValue(nums, k))
nums = [4,2,5,1]
k = 3
print(Solution().maxTotalValue(nums, k))