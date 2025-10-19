# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for left in range(n):
            evens, odds = set(), set()
            for right in range(left, n):
                if nums[right] % 2 == 0:
                    evens.add(nums[right])
                else:
                    odds.add(nums[right])
                if len(evens) == len(odds):
                    result = max(result, right - left + 1)
        return result


nums = [2, 5, 4, 3]
print(Solution().longestBalanced(nums))
nums = [3, 2, 2, 5, 4]
print(Solution().longestBalanced(nums))
nums = [1, 2, 3, 2]
print(Solution().longestBalanced(nums))
