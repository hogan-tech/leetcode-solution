# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = 0
        minNum = float('inf')
        maxIdx = 0
        maxNum = -float('inf')
        for i, num in enumerate(nums):
            if num < minNum:
                minNum = num
                minIdx = i
            if num > maxNum:
                maxNum = num
                maxIdx = i

        n = len(nums)
        if minIdx > maxIdx:
            minIdx, maxIdx = maxIdx, minIdx

        a = minIdx
        b = maxIdx
        return min(a + n - b + 1, b + 1, n - a) if a != b else 1

        '''
        case 1:
            <- a b -> 
            a + 1 + n - b 
        case 2:
            <- a <- b
            b + 1
        case 3:
            a -> b ->
            n - a + 1
        case 4:
            a == b:
            a - b + 1
        '''

        return 0


nums = [-14, 61, 29, -18, 59, 13, -67, -16, 55, -57, 7, 74]
print(Solution().minimumDeletions(nums))
nums = [2, 10, 7, 5, 4, 1, 8, 6]
print(Solution().minimumDeletions(nums))
nums = [0, -4, 19, 1, 8, -2, -3, 5]
print(Solution().minimumDeletions(nums))
nums = [101]
print(Solution().minimumDeletions(nums))
