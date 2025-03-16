# time complexity: O(n*k*max(nums[i])*logm)
# space complexity: O(n)
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        def canZero(k):
            temp = [[] for _ in range(n)]
            for i in range(k):
                l, r, val = queries[i]
                for idx in range(l, r + 1):
                    temp[idx].append(val)

            for i in range(n):
                target = nums[i]
                values = temp[i]
                if not self.hasSubsetSumDP(values, target):
                    return False
            return True

        left = 0
        right = m
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if canZero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

    def hasSubsetSumDP(self, nums, target):
        dp = set()
        dp.add(0)

        for num in nums:
            newDp = dp.copy()
            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    newDp.add(s + num)
            dp = newDp

        return target in dp


nums = [2, 0, 2]
queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
print(Solution().minZeroArray(nums, queries))
nums = [4, 3, 2, 1]
queries = [[1, 3, 2], [0, 2, 1]]
print(Solution().minZeroArray(nums, queries))
nums = [1, 2, 3, 2, 1]
queries = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 4, 1]]
print(Solution().minZeroArray(nums, queries))
nums = [1, 2, 3, 2, 6]
queries = [[0, 1, 1], [0, 2, 1], [1, 4, 2], [4, 4, 4], [3, 4, 1], [4, 4, 5]]
print(Solution().minZeroArray(nums, queries))
