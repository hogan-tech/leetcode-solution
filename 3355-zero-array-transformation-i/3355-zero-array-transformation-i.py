# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for left, right in queries:
            diff[left] += 1
            if right + 1 < n:
                diff[right + 1] -= 1

        decrement = 0
        for i in range(n):
            decrement += diff[i]
            nums[i] -= decrement
            if nums[i] < 0:
                nums[i] = 0
        return all(num == 0 for num in nums)


nums = [1, 0, 1]
queries = [[0, 2]]
print(Solution().isZeroArray(nums, queries))
nums = [4, 3, 2, 1]
queries = [[1, 3], [0, 2]]
print(Solution().isZeroArray(nums, queries))
