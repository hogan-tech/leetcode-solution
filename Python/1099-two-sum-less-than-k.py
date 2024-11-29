# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = -1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                ans = max(ans, sum)
                left += 1
            else:
                right -= 1
        return ans


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60

print(Solution().twoSumLessThanK(nums, k))
