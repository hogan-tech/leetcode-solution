# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = nums[i] + prefixSum[i]

        for query in queries:
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < query:
                    left = mid + 1
                else:
                    right = mid - 1

            leftCost = query * left - prefixSum[left]
            rightCost = prefixSum[n] - prefixSum[left] - query * (n - left)
            result.append(leftCost + rightCost)
        return result


nums = [3, 1, 6, 8]
queries = [1, 5]
print(Solution().minOperations(nums, queries))
nums = [2, 9, 6, 3]
queries = [10]
print(Solution().minOperations(nums, queries))
