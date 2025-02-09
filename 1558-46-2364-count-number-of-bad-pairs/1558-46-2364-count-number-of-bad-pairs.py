# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        def calculate(num):
            return (num + 1) * num // 2
        diff = [nums[i] - i for i in range(len(nums))]
        freq = defaultdict(int)
        total = calculate(len(nums) - 1)
        for num in diff:
            freq[num] += 1
        for count in freq.values():
            if count > 1:
                total -= calculate(count - 1)

        return total


nums = [4, 1, 3, 3]
print(Solution().countBadPairs(nums))
nums = [1, 2, 3, 4, 5]
print(Solution().countBadPairs(nums))
