# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if not all(nums[i] < nums[i+1] for i in range(0, p)):
                    continue
                if not all(nums[i] > nums[i+1] for i in range(p, q)):
                    continue
                if not all(nums[i] < nums[i+1] for i in range(q, n - 1)):
                    continue
                return True
        return False


nums = [1, 3, 5, 4, 2, 6]
print(Solution().isTrionic(nums))
nums = [2, 1, 3]
print(Solution().isTrionic(nums))
