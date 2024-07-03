# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 4:
            return 0
        res = float("inf")
        res = min(res, nums[n-4] - nums[0])
        res = min(res, nums[n-3] - nums[1])
        res = min(res, nums[n-2] - nums[2])
        res = min(res, nums[n-1] - nums[3])
        return res


nums = [5, 3, 2, 4]
print(Solution().minDifference(nums))
