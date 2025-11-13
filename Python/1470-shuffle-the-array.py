# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(Solution().shuffle(nums, n))
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(Solution().shuffle(nums, n))
nums = [1, 1, 2, 2]
n = 2
print(Solution().shuffle(nums, n))
