from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        for _, item in enumerate(list(permutations(nums))):
            temp = list(item)
            if temp not in result:
                result.append(temp)
        return result


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
