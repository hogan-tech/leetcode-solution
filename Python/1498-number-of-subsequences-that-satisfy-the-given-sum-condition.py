# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1
        return result


nums = [3, 5, 6, 7]
target = 9
print(Solution().numSubseq(nums, target))
nums = [3, 3, 6, 8]
target = 10
print(Solution().numSubseq(nums, target))
nums = [2, 3, 3, 4, 6, 7]
target = 12
print(Solution().numSubseq(nums, target))
