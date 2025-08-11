# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums[i] == i for i in range(n)):
            return 0

        result = (1 << max(1, (n - 1).bit_length())) - 1
        for i, num in enumerate(nums):
            if num != i:
                result &= (i & num)
        return result


nums = [0, 3, 2, 1]
print(Solution().sortPermutation(nums))
nums = [0, 1, 3, 2]
print(Solution().sortPermutation(nums))
nums = [3, 2, 1, 0]
print(Solution().sortPermutation(nums))
