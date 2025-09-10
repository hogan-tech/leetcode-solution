# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tempSum = 0
        left = 0
        windowSize = float('inf')
        for right in range(len(nums)):
            tempSum += nums[right]
            while tempSum >= target:
                windowSize = min(right - left + 1, windowSize)
                tempSum -= nums[left]
                left += 1
        return windowSize if windowSize != float('inf') else 0

# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def binarySearch(length: int):
            tempSum = sum(nums[:length])
            if target <= tempSum:
                return True
            for i in range(length, len(nums)):
                tempSum -= nums[i-length]
                tempSum += nums[i]
                if target <= tempSum:
                    return True

            return False

        left, right = 1, len(nums)

        while left <= right:
            mid = (left + right) // 2
            if binarySearch(mid):
                right = mid - 1
            else:
                left = mid + 1
        return 0 if left > len(nums) else left


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
target = 4
nums = [1, 4, 4]
print(Solution().minSubArrayLen(target, nums))
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().minSubArrayLen(target, nums))
