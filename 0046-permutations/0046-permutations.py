from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, item in enumerate(list(permutations(nums))):
            result.append(list(item))
        return result