# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        remainder = total % k
        if remainder == 0:
            return 0

        mods = []
        for num in nums:
            mods.append(num % k)
        mods.sort(reverse=True)

        result = 0
        for m in mods:
            if remainder == 0:
                break
            take = min(remainder, m)
            result += take
            remainder -= take
        return result


nums = [3, 9, 7]
k = 5
print(Solution().minOperations(nums, k))
nums = [4, 1, 3]
k = 4
print(Solution().minOperations(nums, k))
nums = [3, 2]
k = 6
print(Solution().minOperations(nums, k))
