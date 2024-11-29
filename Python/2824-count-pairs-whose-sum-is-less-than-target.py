import itertools
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        numsSet = itertools.permutations(nums, 2)
        count = 0
        for item in numsSet:
            if sum(list(item)) < target:
                count += 1
        return count//2