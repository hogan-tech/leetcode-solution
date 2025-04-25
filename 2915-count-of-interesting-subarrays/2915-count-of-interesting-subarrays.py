# time complexity: O(n)
# space complexity: O(min(n, modulo))
from typing import Counter, List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        cnt = Counter([0])
        result = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            result += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return result


nums = [3, 2, 4]
modulo = 2
k = 1
print(Solution().countInterestingSubarrays(nums, modulo, k))
nums = [3, 1, 9, 6]
modulo = 3
k = 0
print(Solution().countInterestingSubarrays(nums, modulo, k))
