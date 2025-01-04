# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        result = []
        for query in queries:
            left = 0
            right = len(prefixSum) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if prefixSum[mid] <= query:
                    left = mid + 1
                else:
                    right = mid - 1
            result.append(left)
        return result


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(Solution().answerQueries(nums, queries))
nums = [2, 3, 4, 5]
queries = [1]
print(Solution().answerQueries(nums, queries))
