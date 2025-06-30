# time complexity: O(n^2*k)
# space complexity: O(nk)
from functools import lru_cache
from typing import List


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:

        def canPartition(limit):
            @lru_cache(None)
            def dp(index: int, cuts: int) -> bool:
                if cuts == 0:
                    return index == len(nums)
                xor = 0
                for j in range(index, len(nums) - (cuts - 1)):
                    xor ^= nums[j]
                    if xor <= limit:
                        if dp(j + 1, cuts - 1):
                            return True
                return False

            return dp(0, k)

        left, right = 0, 0
        for num in nums:
            right ^= num

        right = (1 << 31) - 1

        result = right
        while left <= right:
            mid = (left + right) // 2
            if canPartition(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result


nums = [1, 2, 3]
k = 2
print(Solution().minXor(nums, k))
nums = [2, 3, 3, 2]
k = 3
print(Solution().minXor(nums, k))
nums = [1, 1, 2, 3, 1]
k = 2
print(Solution().minXor(nums, k))
