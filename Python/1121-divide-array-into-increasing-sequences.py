# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        previous = nums[0]
        count = 0
        for n in nums:
            if previous == n:
                count += 1
            else:
                previous = n
                count = 1
            if count * k > len(nums):
                return False
        return True


nums = [1, 2, 2, 3, 3, 4, 4]
k = 3
print(Solution().canDivideIntoSubsequences(nums, k))
nums = [5, 6, 6, 7, 8]
k = 3
print(Solution().canDivideIntoSubsequences(nums, k))
