from itertools import chain, combinations, permutations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list(chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1)))
        for i,item in enumerate(result):
            result[i] = list(item)
        return result