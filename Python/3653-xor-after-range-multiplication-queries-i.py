# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for left, right, k, v in queries:
            mult = v % MOD
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * mult) % MOD
        result = 0
        for num in nums:
            result ^= num
        return result


nums = [1, 1, 1]
queries = [[0, 2, 1, 4]]
print(Solution().xorAfterQueries(nums, queries))
nums = [2, 3, 1, 5, 4]
queries = [[1, 4, 2, 3], [0, 2, 1, 2]]
print(Solution().xorAfterQueries(nums, queries))
