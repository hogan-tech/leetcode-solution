# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = 0
        operations = [0 for _ in range(n + 1)]
        for i in range(n):
            prefix += operations[i]
            current = nums[i] - prefix

            if current < 0:
                return False

            if current > 0:
                if i + k > n:
                    return False
                operations[i + k] -= current
            prefix += current
        print(operations)
        return True


nums = [2, 2, 3, 1, 1, 0]
k = 3
print(Solution().checkArray(nums, k))
nums = [1, 3, 1, 1]
k = 2
print(Solution().checkArray(nums, k))
