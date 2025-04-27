# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        componentIdx = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                component[i] = componentIdx
            else:
                componentIdx += 1
                component[i] = componentIdx

        result = []
        for u, v in queries:
            result.append(component[u] == component[v])
        return result


n = 2
nums = [1, 3]
maxDiff = 1
queries = [[0, 0], [0, 1]]
print(Solution().pathExistenceQueries(n, nums, maxDiff, queries))
n = 4
nums = [2, 5, 6, 8]
maxDiff = 2
queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
print(Solution().pathExistenceQueries(n, nums, maxDiff, queries))
