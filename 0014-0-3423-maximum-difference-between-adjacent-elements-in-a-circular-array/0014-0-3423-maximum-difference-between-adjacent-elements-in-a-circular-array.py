# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        result = float('-inf')
        for i in range(len(nums) - 1):
            result = max(result, abs(nums[i] - nums[i + 1]))
        return result


nums = [1, 2, 4]
print(Solution().maxAdjacentDistance(nums))
nums = [-5, -10, -5]
print(Solution().maxAdjacentDistance(nums))
