# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = [False] * len(queries)
        prefixSum = [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                prefixSum[i] = prefixSum[i-1] + 1
            else:
                prefixSum[i] = prefixSum[i-1]

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]
            result[i] = prefixSum[end] - prefixSum[start] == 0
        return result


nums = [3, 4, 1, 2, 6]
queries = [[0, 4]]
print(Solution().isArraySpecial(nums, queries))
nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]
print(Solution().isArraySpecial(nums, queries))
