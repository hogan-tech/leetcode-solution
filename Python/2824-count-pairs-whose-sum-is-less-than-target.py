# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[i] + nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            count += left - (i + 1)

        return count


nums = [-1, 1, 2, 3, 1]
target = 2
print(Solution().countPairs(nums, target))
nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2
print(Solution().countPairs(nums, target))
