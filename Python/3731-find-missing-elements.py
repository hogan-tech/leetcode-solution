# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minNum = min(nums)
        maxNum = max(nums)
        numSet = set(nums)
        result = []
        for num in range(minNum, maxNum + 1):
            if num not in numSet:
                result.append(num)
        return result


nums = [1, 4, 2, 5]
print(Solution().findMissingElements(nums))
nums = [7, 8, 6, 9]
print(Solution().findMissingElements(nums))
nums = [5, 1]
print(Solution().findMissingElements(nums))
