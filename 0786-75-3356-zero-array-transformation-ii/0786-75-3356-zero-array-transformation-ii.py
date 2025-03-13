# time complexity: O(logm * (n + m))
# space complexity: O(n)
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)
        if not self.canFormZeroArray(nums, queries, right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2
            if self.canFormZeroArray(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left

    def canFormZeroArray(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        totalSum = 0
        diffArr = [0] * (n + 1)

        for i in range(k):
            left, right, val = queries[i]

            diffArr[left] += val
            diffArr[right + 1] -= val

        for i in range(n):
            totalSum += diffArr[i]
            if totalSum < nums[i]:
                return False

        return True


'''
1 0 0
1 0 0
0 3 -3



'''
nums = [2, 0, 2]
queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
print(Solution().minZeroArray(nums, queries))
'''
0 2 0 0
1 0 0 -1

1 2 0 -1

1 3 3 2
'''
nums = [4, 3, 2, 1]
queries = [[1, 3, 2], [0, 2, 1]]
print(Solution().minZeroArray(nums, queries))
