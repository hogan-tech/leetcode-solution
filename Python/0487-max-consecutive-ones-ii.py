# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longestSequence = 0
        left, right = 0, 0
        numZeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                numZeroes += 1

            while numZeroes == 2:
                if nums[left] == 0:
                    numZeroes -= 1
                left += 1

            longestSequence = max(longestSequence, right - left + 1)
            right += 1

        return longestSequence


nums = [1, 0, 1, 1, 0]
print(Solution().findMaxConsecutiveOnes(nums))
