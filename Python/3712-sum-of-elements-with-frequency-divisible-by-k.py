# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = 0
        for num, freq in Counter(nums).items():
            if freq % k == 0:
                count += (num * freq)
        return count


nums = [1, 2, 2, 3, 3, 3, 3, 4]
k = 2
print(Solution().sumDivisibleByK(nums, k))
nums = [1, 2, 3, 4, 5]
k = 2
print(Solution().sumDivisibleByK(nums, k))
nums = [4, 4, 4, 1, 2, 3]
k = 3
print(Solution().sumDivisibleByK(nums, k))
