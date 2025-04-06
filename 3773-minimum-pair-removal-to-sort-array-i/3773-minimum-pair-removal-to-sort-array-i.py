# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isNonDecreasing(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        result = 0
        while not isNonDecreasing(nums):
            minSum = float('inf')
            minIdx = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    minIdx = i

            merged = nums[minIdx] + nums[minIdx + 1]
            nums = nums[:minIdx] + [merged] + nums[minIdx + 2:]
            result += 1
        return result


nums = [5, 2, 3, 1]
print(Solution().minimumPairRemoval(nums))
nums = [1, 2, 2]
print(Solution().minimumPairRemoval(nums))
