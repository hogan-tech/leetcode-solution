# time complexity: O(nlogn)
# space compelxity: O(n)
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


nums = [90]
k = 1
print(Solution().minimumDifference(nums, k))
nums = [9, 4, 1, 7]
k = 2
print(Solution().minimumDifference(nums, k))
