# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        finalXor = 0
        for n in nums:
            finalXor = finalXor ^ n

        return bin(finalXor ^ k).count('1')


nums = [2, 1, 3, 4]
k = 1
print(Solution().minOperations(nums, k))
