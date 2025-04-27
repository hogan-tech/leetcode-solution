# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            arr = nums[i:i+3]
            if len(arr) == 3 and (2*(arr[0] + arr[2]) == arr[1]):
                count += 1
        return count


nums = [1, 2, 1, 4, 1]
print(Solution().countSubarrays(nums))
nums = [1, 1, 1]
print(Solution().countSubarrays(nums))
nums = [0, -4, -4]
print(Solution().countSubarrays(nums))
