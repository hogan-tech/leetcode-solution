# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(k, len(nums)-k + 1):
            if nums[i-k:i] == sorted(nums[i-k:i]) and nums[i:i+k] == sorted(nums[i:i+k]) and len(nums[i-k:i]) == len(set(nums[i-k:i])) and len(nums[i:i+k]) == len(set(nums[i:i+k])):
                return True
        return False


nums = [-15, 19]
k = 1
print(Solution().hasIncreasingSubarrays(nums, k))
nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
k = 5
print(Solution().hasIncreasingSubarrays(nums, k))
nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
k = 3
print(Solution().hasIncreasingSubarrays(nums, k))
