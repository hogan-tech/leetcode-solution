# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    result += 1
        return result


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(Solution().countPairs(nums, k))
nums = [1, 2, 3, 4]
k = 1
print(Solution().countPairs(nums, k))
