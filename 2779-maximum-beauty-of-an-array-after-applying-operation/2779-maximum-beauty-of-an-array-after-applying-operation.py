# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        def binarySearch(nums: List[int], val: int) -> int:
            left = 0
            right = len(nums) - 1
            upperBound = 0
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= val:
                    upperBound = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return upperBound

        nums.sort()
        result = 0
        for i, num in enumerate(nums):
            upperBound = binarySearch(nums, num + 2*k)
            result = max(result, upperBound - i + 1)

        return result


nums = [4, 6, 1, 2]
k = 2
print(Solution().maximumBeauty(nums, k))
nums = [1, 1, 1, 1]
k = 10
print(Solution().maximumBeauty(nums, k))
