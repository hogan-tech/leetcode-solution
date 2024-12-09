# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] > 0:
                result[i] = nums[(i+nums[i]) % n]
            elif nums[i] < 0:
                result[i] = nums[(i - abs(nums[i])) % n]
            else:
                result[i] = nums[i]
        return result


nums = [3, -2, 1, 1]
print(Solution().constructTransformedArray(nums))
nums = [-1, 4, -1]
print(Solution().constructTransformedArray(nums))
