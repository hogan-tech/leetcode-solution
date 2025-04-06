# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N = len(nums)

        minList = [None for _ in range(N)]
        minNum = float('-inf')
        for i in range(N):
            minList[i] = minNum
            minNum = max(nums[i], minNum)

        maxList = [None for _ in range(N)]
        maxNum = float('inf')
        for i in range(N-1, -1, -1):
            maxList[i] = maxNum
            maxNum = min(maxNum, nums[i])

        result = 0
        for i in range(1, N-1):
            if minList[i] < nums[i] < maxList[i]:
                result += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
        return result


nums = [1, 2, 3]
print(Solution().sumOfBeauties(nums))
nums = [2, 4, 6, 4]
print(Solution().sumOfBeauties(nums))
nums = [3, 2, 1]
print(Solution().sumOfBeauties(nums))
nums = [9, 6, 9, 8, 9, 5, 1, 1, 6]
print(Solution().sumOfBeauties(nums))
nums = [6, 8, 3, 7, 8, 9, 4, 8]
print(Solution().sumOfBeauties(nums))
