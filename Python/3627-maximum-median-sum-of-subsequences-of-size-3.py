# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums) // 3
        return sum(nums[i * 2 + 1] for i in range(n))


nums = [2, 1, 3, 2, 1, 3]
print(Solution().maximumMedianSum(nums))
nums = [1, 1, 10, 10, 10, 10]
print(Solution().maximumMedianSum(nums))
