# time complexity: O(nlogm)
# space complexity: O(1)
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(nums, k, mid):
            subArrays = 1
            currentSum = 0
            for num in nums:
                if currentSum + num > mid:
                    subArrays += 1
                    currentSum = num
                    if subArrays > k:
                        return False
                else:
                    currentSum += num
            return True

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left


nums = [7, 2, 5, 10, 8]
k = 2
print(Solution().splitArray(nums, k))
nums = [1, 2, 3, 4, 5]
k = 2
print(Solution().splitArray(nums, k))
