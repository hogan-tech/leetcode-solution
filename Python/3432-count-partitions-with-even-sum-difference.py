# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
                count += 1
        return count


nums = [10, 10, 3, 7, 6]
print(Solution().countPartitions(nums))
nums = [1, 2, 2]
print(Solution().countPartitions(nums))
nums = [2, 4, 6, 8]
print(Solution().countPartitions(nums))
