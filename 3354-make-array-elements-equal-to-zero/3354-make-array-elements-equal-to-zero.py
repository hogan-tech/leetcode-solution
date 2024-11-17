# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def simulate(start, direction):
            n = len(nums)
            numsCopy = nums[:]
            curr = start
            moveRight = direction == 'right'

            while 0 <= curr < n:
                if numsCopy[curr] == 0:
                    curr = curr + 1 if moveRight else curr - 1
                else:
                    numsCopy[curr] -= 1
                    moveRight = not moveRight
                    curr = curr + 1 if moveRight else curr - 1
            return all(x == 0 for x in numsCopy)

        n = len(nums)
        validCount = 0

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 'right'):
                    validCount += 1
                if simulate(i, 'left'):
                    validCount += 1

        return validCount


nums1 = [1, 0, 2, 0, 3]
nums2 = [2, 3, 4, 0, 4, 1, 0]

print(Solution().countValidSelections(nums1))  # Output: 2
print(Solution().countValidSelections(nums2))  # Output: 0
