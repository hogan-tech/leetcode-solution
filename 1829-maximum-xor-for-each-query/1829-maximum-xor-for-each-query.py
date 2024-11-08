# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixXor = [0] * len(nums)
        prefixXor[0] = nums[0]
        for i in range(1, len(nums)):
            prefixXor[i] = prefixXor[i-1] ^ nums[i]
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):
            currXor = prefixXor[len(prefixXor) - 1 - i]
            ans[i] = currXor ^ mask
        return ans


nums = [0, 1, 1, 3]
maximumBit = 2
print(Solution().getMaximumXor(nums, maximumBit))
