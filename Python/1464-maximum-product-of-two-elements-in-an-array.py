# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1)*(nums[-2]-1)


nums = [1, 5, 4, 5]

print(Solution().maxProduct(nums))
