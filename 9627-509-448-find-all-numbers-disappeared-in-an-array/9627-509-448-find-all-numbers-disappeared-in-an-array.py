# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsSet = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in numsSet:
                result.append(i)
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))
nums = [1, 1]
print(Solution().findDisappearedNumbers(nums))
