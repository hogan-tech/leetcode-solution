# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
        return ans


nums = [5, 1, 3]
print(Solution().reductionOperations(nums))
