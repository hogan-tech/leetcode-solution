# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        prev = 0
        for num in nums:
            if num < prev:
                ans = num + prev
            prev += num
        return ans


nums = [5, 5, 5]

print(Solution().largestPerimeter(nums))
