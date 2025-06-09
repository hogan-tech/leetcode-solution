# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return True

        def helper(target: int) -> int:
            arr = list(nums)
            ops = 0
            for i in range(n - 1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i+1] *= -1
                    ops += 1
            return ops if arr[-1] == target else float('inf')

        return min(helper(1), helper(-1)) <= k


nums = [1, -1, 1, -1, 1]
k = 3
print(Solution().canMakeEqual(nums, k))
nums = [-1, -1, -1, 1, 1, 1]
k = 5
print(Solution().canMakeEqual(nums, k))
nums = [-1, 1, -1, 1, 1, 1]
k = 4
print(Solution().canMakeEqual(nums, k))
