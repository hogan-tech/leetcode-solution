# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.append(0)
        return len(set(nums)) - 1


nums = [1, 5, 0, 3, 5]
print(Solution().minimumOperations(nums))
nums = [0]
print(Solution().minimumOperations(nums))
