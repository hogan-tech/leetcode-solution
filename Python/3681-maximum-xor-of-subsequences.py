# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:

        basis = [0] * 32
        for num in nums:
            for i in reversed(range(32)):
                if (num >> i) & 1:
                    if basis[i] == 0:
                        basis[i] = num
                        break
                    num ^= basis[i]

        maxXor = 0
        for b in reversed(basis):
            if (maxXor ^ b) > maxXor:
                maxXor ^= b

        return maxXor


nums = [1, 2, 3]
print(Solution().maxXorSubsequences(nums))
nums = [5, 2]
print(Solution().maxXorSubsequences(nums))
