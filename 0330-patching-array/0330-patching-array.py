# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result


nums = [1, 3]
n = 6
print(Solution().minPatches(nums, n))
