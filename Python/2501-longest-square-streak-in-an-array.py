# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        result = 0
        numSet = set(nums)
        for curr in nums:
            temp = 0
            current = curr
            while current in numSet:
                temp += 1
                if current * current > 10**5:
                    break
                current *= current

            result = max(result, temp)

        return -1 if result == 1 else result


nums = [3, 9, 81, 6561]
print(Solution().longestSquareStreak(nums))
