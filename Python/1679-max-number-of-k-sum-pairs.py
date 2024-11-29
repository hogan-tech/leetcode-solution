# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                result += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            elif nums[right] + nums[left] > k:
                right -= 1
        return result


nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
k = 2
print(Solution().maxOperations(nums, k))
