from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        m = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            k = (nums[i] - 1) // m
            ans += k
            m = nums[i] // (k+1)
        return ans


nums = [3, 9, 3]
print(Solution().minimumReplacement(nums))
